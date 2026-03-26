
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict
from app_core_orchestrator.launcher.bootstrap import bootstrap
from app_core_orchestrator.orchestrators.daily_orchestrator import run_daily_orchestration

def run_daily_pipeline(run_request: Dict[str, Any], pack_root: Path) -> Dict[str, Any]:
    run_context = bootstrap(run_request, pack_root)
    return run_daily_orchestration(run_context)
