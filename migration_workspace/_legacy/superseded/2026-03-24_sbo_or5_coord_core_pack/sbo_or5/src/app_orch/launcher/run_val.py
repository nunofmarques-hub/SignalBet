from __future__ import annotations
from pathlib import Path
from app_orch.launcher.boot import boot
from app_orch.orch.core import run_validation

def run_validation_pipeline(req: dict, pack_root: Path):
    ctx = boot(req, pack_root)
    return run_validation(ctx)
