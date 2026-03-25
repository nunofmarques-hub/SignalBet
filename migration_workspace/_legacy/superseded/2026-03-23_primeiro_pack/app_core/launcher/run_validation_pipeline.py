from __future__ import annotations

from typing import Any, Dict

from app_core.launcher.bootstrap import bootstrap
from app_core.orchestrators.validation_orchestrator import run_validation_orchestration


def run_validation_pipeline(run_request: Dict[str, Any]) -> Dict[str, Any]:
    run_context = bootstrap(run_request)
    return run_validation_orchestration(run_context, run_request)
