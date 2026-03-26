
from __future__ import annotations
from typing import Any, Dict

def build_ui_status(run_summary: Dict[str, Any]) -> Dict[str, Any]:
    system_health = 'PASS' if run_summary['preflight_status'] == 'PASS' else 'WARN'
    return {
        'screen_status':'COMPLETED' if run_summary['preflight_status'] != 'FAIL' else 'BLOCKED',
        'run_id': run_summary['run_id'],
        'system_health': system_health,
        'data_api_health': run_summary['data_api_status'],
        'module_overview': {
            'modules_run': run_summary['modules_run'],
            'modules_skipped': run_summary['modules_skipped'],
        },
        'last_run_summary': run_summary,
        'blocking_message': None if run_summary['preflight_status'] != 'FAIL' else 'Falha bloqueante no preflight.',
        'cta_state': 'enabled' if run_summary['preflight_status'] != 'FAIL' else 'disabled',
    }
