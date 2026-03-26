from __future__ import annotations

from typing import Any, Dict

from app_core.launcher.run_validation_pipeline import run_validation_pipeline


def run_dry_pipeline(run_request: Dict[str, Any]) -> Dict[str, Any]:
    dry_request = dict(run_request)
    dry_request["run_profile"] = "dry_run"
    dry_request["dry_run"] = True
    return run_validation_pipeline(dry_request)
