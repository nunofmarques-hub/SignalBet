from __future__ import annotations

from typing import Any, Dict

from app_core.orchestrators.daily_orchestrator import run_daily_orchestration


def run_validation_orchestration(run_context: Dict[str, Any], run_request: Dict[str, Any]) -> Dict[str, Any]:
    validation_request = dict(run_request)
    validation_request.setdefault("dry_run", True)
    validation_request.setdefault("run_profile", "validation_run")
    run_context["dry_run"] = True
    run_context["run_profile"] = "validation_run"
    return run_daily_orchestration(run_context, validation_request)
