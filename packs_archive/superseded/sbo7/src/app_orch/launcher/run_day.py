from __future__ import annotations
from pathlib import Path
from app_orch.launcher.boot import bootstrap
from app_orch.orch.core import run_validation

def run_daily_pipeline(run_request: dict, pack_root: Path):
    ctx = bootstrap(run_request, pack_root)
    ctx['run_profile'] = 'daily_run'
    return run_validation(ctx)
