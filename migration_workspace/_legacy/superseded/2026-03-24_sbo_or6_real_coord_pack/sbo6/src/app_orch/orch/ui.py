from __future__ import annotations

def build(summary: dict):
    return {
        'screen_status': 'BLOCKED' if summary['preflight_status'] == 'FAIL' else 'COMPLETED',
        'run_id': summary['run_id'],
        'system_health': summary['preflight_status'],
        'data_api_health': summary['official_trunk_status'],
        'project_mode': summary['project_mode'],
        'project_root': summary['project_root'],
        'module_overview': {
            'eligible': summary['modules_eligible'],
            'run': summary['modules_run'],
            'skipped': summary['modules_skipped'],
            'failed': summary['modules_failed'],
            'sources': summary['module_feed_sources'],
        },
        'counts': {
            'candidates_generated': summary['candidates_generated'],
            'approved': summary['approved_count'],
            'reduced': summary['reduced_count'],
            'blocked': summary['blocked_count'],
        },
        'pipeline': {
            'gps_status': summary['gps_status'],
            'bankroll_status': summary['bankroll_status'],
            'execution_status': summary['execution_status'],
        },
        'last_run_summary': summary['final_summary'],
        'cta_state': 'blocked' if summary['preflight_status'] == 'FAIL' else 'ready',
        'warnings': summary['warnings'],
        'errors': summary['errors'],
    }
