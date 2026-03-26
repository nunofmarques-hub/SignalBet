from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

from app_core.health_checks.env_checks import run_environment_checks
from app_core.health_checks.config_checks import run_config_checks
from app_core.health_checks.data_api_checks import run_data_api_checks
from app_core.health_checks.module_checks import run_module_checks
from app_core.health_checks.pipeline_checks import run_pipeline_checks
from app_core.orchestrators.module_runner import discover_modules, run_modules
from app_core.orchestrators.candidate_collector import collect_candidates
from app_core.orchestrators.shortlist_flow import run_global_pick_selector, run_bankroll_manager
from app_core.orchestrators.execution_bridge import register_execution
from app_core.orchestrators.ui_response_builder import build_ui_status

OFFICIAL_TRUNK = "Data_API_Official_Trunk_v1"


def _overall_status(checks: List[Dict[str, Any]]) -> str:
    if any(c["status"] == "FAIL" and c["blocking"] for c in checks):
        return "FAIL"
    if any(c["status"] == "WARN" for c in checks):
        return "WARN"
    return "PASS"


def _trunk_status(checks: List[Dict[str, Any]]) -> str:
    trunk_checks = [c for c in checks if c["check_id"].startswith("official_trunk_")]
    if not trunk_checks:
        return "FAIL"
    if any(c["status"] == "FAIL" and c["blocking"] for c in trunk_checks):
        return "FAIL"
    if any(c["status"] == "WARN" for c in trunk_checks):
        return "WARN"
    return "PASS"


def run_preflight_checks(project_root: str, run_context: Dict[str, Any]) -> Dict[str, Any]:
    checks: List[Dict[str, Any]] = []
    checks.extend(run_config_checks(project_root))
    checks.extend(run_environment_checks(project_root))
    checks.extend(run_data_api_checks(project_root))
    checks.extend(run_module_checks(project_root))
    checks.extend(run_pipeline_checks(project_root))
    return {
        "run_id": run_context["run_id"],
        "overall_status": _overall_status(checks),
        "data_api_reference": OFFICIAL_TRUNK,
        "checks": checks,
        "blocking_failures": [c["check_id"] for c in checks if c["status"] == "FAIL" and c["blocking"]],
        "warnings": [c["check_id"] for c in checks if c["status"] == "WARN"],
    }


def has_blocking_failure(health_report: Dict[str, Any]) -> bool:
    return bool(health_report.get("blocking_failures"))


def build_failed_summary(run_context: Dict[str, Any], health_report: Dict[str, Any]) -> Dict[str, Any]:
    finished_at = datetime.now(timezone.utc).isoformat()
    checks = health_report.get("checks", [])
    run_summary = {
        "run_id": run_context["run_id"],
        "run_profile": run_context["run_profile"],
        "started_at": run_context["started_at"],
        "finished_at": finished_at,
        "preflight_status": "FAIL",
        "data_api_reference": OFFICIAL_TRUNK,
        "official_trunk_status": _trunk_status(checks),
        "data_api_status": "FAIL",
        "modules_run": [],
        "modules_skipped": [],
        "candidates_generated": 0,
        "gps_status": "SKIPPED",
        "bankroll_status": "SKIPPED",
        "execution_status": "SKIPPED",
        "warnings": health_report.get("warnings", []),
        "errors": health_report.get("blocking_failures", []),
        "final_summary": "Corrida bloqueada por falhas no preflight/readiness do Data_API_Official_Trunk_v1.",
    }
    return {"health_report": health_report, "run_summary": run_summary, "ui_status": build_ui_status(run_summary)}


def run_daily_orchestration(run_context: Dict[str, Any], run_request: Dict[str, Any]) -> Dict[str, Any]:
    project_root = run_context["project_root"]
    health_report = run_preflight_checks(project_root, run_context)
    if has_blocking_failure(health_report):
        return build_failed_summary(run_context, health_report)

    eligible_modules, skipped_modules = discover_modules(project_root, run_context["run_profile"], run_context.get("forced_modules"))
    module_outputs = run_modules(eligible_modules, run_context)
    opportunity_pool = collect_candidates(module_outputs)
    gps_output = run_global_pick_selector(opportunity_pool, run_context)
    bankroll_output = run_bankroll_manager(gps_output, run_context)

    execution_output = (
        {"status": "SKIPPED", "registered_orders": 0, "message": "Dry/validation run sem execution real."}
        if run_context.get("dry_run")
        else register_execution(bankroll_output, run_context)
    )

    finished_at = datetime.now(timezone.utc).isoformat()
    warnings = list(dict.fromkeys(health_report.get("warnings", []) + opportunity_pool.get("warnings", [])))
    run_summary = {
        "run_id": run_context["run_id"],
        "run_profile": run_context["run_profile"],
        "started_at": run_context["started_at"],
        "finished_at": finished_at,
        "preflight_status": health_report["overall_status"],
        "data_api_reference": OFFICIAL_TRUNK,
        "official_trunk_status": _trunk_status(health_report.get("checks", [])),
        "data_api_status": _trunk_status(health_report.get("checks", [])),
        "modules_run": [m["module_id"] for m in eligible_modules],
        "modules_skipped": skipped_modules,
        "candidates_generated": opportunity_pool["candidate_count"],
        "gps_status": gps_output["status"],
        "bankroll_status": bankroll_output["status"],
        "execution_status": execution_output["status"],
        "approved_count": len(bankroll_output.get("approved", [])),
        "reduced_count": len(bankroll_output.get("reduced", [])),
        "reserve_count": len(bankroll_output.get("reserve", [])),
        "warnings": warnings,
        "errors": [],
        "final_summary": "Validation pipeline concluído em draft operacional com trunk oficial validado e subset de módulos corrido." if run_context["run_profile"] == "validation_run" else "Corrida concluída em modo draft pelo Orchestrator com o Data_API_Official_Trunk_v1 como base oficial.",
    }
    return {
        "health_report": health_report,
        "run_summary": run_summary,
        "ui_status": build_ui_status(run_summary, bankroll_output),
        "opportunity_pool": opportunity_pool,
        "gps_output": gps_output,
        "bankroll_output": bankroll_output,
        "execution_output": execution_output,
    }
