from __future__ import annotations

from typing import Any, Dict

from app_core.launcher.bootstrap import bootstrap
from app_core.orchestrators.daily_orchestrator import run_daily_orchestration


def run_dry_pipeline(run_request: Dict[str, Any]) -> Dict[str, Any]:
    dry_request = dict(run_request)
    dry_request["dry_run"] = True
    run_context = bootstrap(dry_request)
    return run_daily_orchestration(run_context, dry_request)
