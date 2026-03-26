
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict
from app_core_orchestrator.launcher.bootstrap import bootstrap
from app_core_orchestrator.orchestrators.validation_orchestrator import run_validation_orchestration
from app_core_orchestrator.orchestrators.ui_response_builder import build_ui_status
from app_core_orchestrator.support.io import write_json

def run_validation_pipeline(run_request: Dict[str, Any], pack_root: Path) -> Dict[str, Any]:
    run_context = bootstrap(run_request, pack_root)
    summary = run_validation_orchestration(run_context)
    ui_status = build_ui_status(summary)
    outputs = pack_root / 'examples' / 'outputs'
    write_json(outputs / 'sample_health_report.json', summary['health_report'])
    write_json(outputs / 'sample_output.json', summary)
    write_json(outputs / 'sample_ui_status.json', ui_status)
    return {'health_report': summary['health_report'], 'run_summary': summary, 'ui_status': ui_status}
