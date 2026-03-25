from __future__ import annotations

def build(summary: dict):
    return {
        'screen_status': 'BLOCKED' if summary['preflight_status'] == 'FAIL' else 'COMPLETED',
        'run_id': summary['run_id'],
        'system_health': summary['preflight_status'],
        'data_api_health': summary['official_trunk_status'],
        'module_overview': {
            'eligible': summary['modules_eligible'],
            'run': summary['modules_run'],
            'skipped': summary['modules_skipped'],
            'failed': summary['modules_failed'],
        },
        'last_run_summary': summary['final_summary'],
        'candidates_generated': summary['candidates_generated'],
        'cta_state': 'blocked' if summary['preflight_status'] == 'FAIL' else 'ready',
        'warnings': summary['warnings'],
        'errors': summary['errors'],
    }
