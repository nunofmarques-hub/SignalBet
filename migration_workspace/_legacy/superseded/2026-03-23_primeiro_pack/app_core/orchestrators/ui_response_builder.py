from __future__ import annotations

from typing import Any, Dict


def build_ui_status(run_summary: Dict[str, Any]) -> Dict[str, Any]:
    screen_status = "COMPLETED" if run_summary.get("preflight_status") != "FAIL" else "FAIL"
    return {
        "screen_status": screen_status,
        "run_id": run_summary.get("run_id"),
        "system_health": run_summary.get("preflight_status"),
        "data_api_health": run_summary.get("data_api_status"),
        "module_overview": [{"module_id": m, "status": "READY"} for m in run_summary.get("modules_run", [])] + [{"module_id": m, "status": "SKIPPED"} for m in run_summary.get("modules_skipped", [])],
        "last_run_summary": run_summary.get("final_summary"),
        "blocking_message": None if run_summary.get("preflight_status") != "FAIL" else "Corrida bloqueada por preflight.",
        "cta_state": "enabled" if run_summary.get("preflight_status") != "FAIL" else "disabled",
    }
