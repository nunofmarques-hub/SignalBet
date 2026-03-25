from __future__ import annotations


def build(summary: dict):
    blocked = summary['preflight_status'] == 'FAIL'
    realish = summary['project_mode'] != 'demo'
    real_feeds = summary['module_feed_stats'].get('project', 0) > 0
    coverage = summary.get('project_feed_coverage_ratio', 0.0)
    cta_state = 'blocked' if blocked else ('ready_real' if realish and real_feeds else 'ready_rehearsal')
    return {
        'screen_status': 'BLOCKED' if blocked else 'COMPLETED',
        'run_id': summary['run_id'],
        'system_health': summary['preflight_status'],
        'data_api_health': summary['official_trunk_status'],
        'project_mode': summary['project_mode'],
        'run_mode': summary['run_mode'],
        'project_root': summary['project_root'],
        'button_context': {
            'label': 'Pôr tudo a correr',
            'cta_state': cta_state,
            'pipeline_ready': not blocked,
            'real_project_attached': realish,
            'real_module_feeds_detected': real_feeds,
            'project_feed_coverage_ratio': coverage,
            'execution_mode': summary['execution_status'],
        },
        'module_overview': {
            'eligible': summary['modules_eligible'],
            'run': summary['modules_run'],
            'skipped': summary['modules_skipped'],
            'failed': summary['modules_failed'],
            'sources': summary['module_feed_sources'],
            'feed_stats': summary['module_feed_stats'],
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
        'integration_state': {
            'demo_vs_real': 'real' if realish else 'demo',
            'coverage_real_feeds': coverage,
            'strict_real_project': summary.get('strict_real_project', False),
            'strict_real_feeds': summary.get('strict_real_feeds', False),
        },
        'cta_state': cta_state,
        'warnings': summary['warnings'],
        'errors': summary['errors'],
    }
