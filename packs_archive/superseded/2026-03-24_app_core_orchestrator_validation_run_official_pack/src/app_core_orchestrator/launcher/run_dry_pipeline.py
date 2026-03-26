
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict
from app_core_orchestrator.launcher.bootstrap import bootstrap
from app_core_orchestrator.orchestrators.daily_orchestrator import run_daily_orchestration

def run_dry_pipeline(run_request: Dict[str, Any], pack_root: Path) -> Dict[str, Any]:
    dry_request = dict(run_request)
    dry_request['dry_run'] = True
    run_context = bootstrap(dry_request, pack_root)
    return run_daily_orchestration(run_context)
