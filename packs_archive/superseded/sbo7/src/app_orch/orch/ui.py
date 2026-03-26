from __future__ import annotations

def build(summary: dict):
    blocked = summary['preflight_status'] == 'FAIL'
    realish = summary['project_mode'] != 'demo'
    real_feeds = any(v.get('mode') == 'project' for v in summary['module_feed_sources'].values())
    cta_state = 'blocked' if blocked else ('ready_real' if realish and real_feeds else 'ready_demo')
    return {
        'screen_status': 'BLOCKED' if blocked else 'COMPLETED',
        'run_id': summary['run_id'],
        'system_health': summary['preflight_status'],
        'data_api_health': summary['official_trunk_status'],
        'project_mode': summary['project_mode'],
        'project_root': summary['project_root'],
        'button_context': {
            'label': 'Pôr tudo a correr',
            'cta_state': cta_state,
            'pipeline_ready': not blocked,
            'real_project_attached': realish,
            'real_module_feeds_detected': real_feeds,
        },
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
        'pipeline_steps': summary['pipeline_steps'],
        'last_run_summary': summary['final_summary'],
        'cta_state': cta_state,
        'warnings': summary['warnings'],
        'errors': summary['errors'],
    }
