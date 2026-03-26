
from __future__ import annotations
from datetime import datetime, timezone
from typing import Any, Dict, List
from app_core_orchestrator.health_checks.config_checks import run_config_checks
from app_core_orchestrator.health_checks.env_checks import run_environment_checks
from app_core_orchestrator.health_checks.data_api_checks import run_data_api_checks
from app_core_orchestrator.health_checks.module_checks import run_module_checks
from app_core_orchestrator.health_checks.pipeline_checks import run_pipeline_checks
from app_core_orchestrator.orchestrators.module_runner import discover_modules, run_modules
from app_core_orchestrator.orchestrators.candidate_collector import collect_candidates
from app_core_orchestrator.orchestrators.shortlist_flow import run_global_pick_selector, run_bankroll_manager
from app_core_orchestrator.orchestrators.execution_bridge import register_execution

def _combine(*groups: List[Dict[str, object]]) -> List[Dict[str, object]]:
    checks: List[Dict[str, object]] = []
    for group in groups:
        checks.extend(group)
    return checks

def _status(checks: List[Dict[str, object]]) -> str:
    if any(c['status'] == 'FAIL' and c.get('blocking') for c in checks):
        return 'FAIL'
    if any(c['status'] in ('FAIL','WARN') for c in checks):
        return 'WARN'
    return 'PASS'

def run_daily_orchestration(run_context: Dict[str, Any]) -> Dict[str, Any]:
    pack_root = run_context['pack_root']
    project_root = run_context['project_root']
    config = run_config_checks(pack_root)
    env = run_environment_checks(project_root)
    data_api = run_data_api_checks(project_root)
    modules = run_module_checks(pack_root)
    pipeline = run_pipeline_checks(pack_root)
    all_checks = _combine(config, env, data_api, modules, pipeline)
    preflight_status = _status(all_checks)
    modules_run = []
    modules_skipped = []
    candidates_generated = 0
    gps_output = {'status':'SKIPPED'}
    bankroll_output = {'status':'SKIPPED'}
    execution_output = {'status':'SKIPPED'}
    warnings = [c['message'] for c in all_checks if c['status'] == 'WARN']
    errors = [c['message'] for c in all_checks if c['status'] == 'FAIL' and c.get('blocking')]
    if preflight_status != 'FAIL':
        eligible, skipped = discover_modules(pack_root, run_context.get('forced_modules') or None)
        modules_skipped = skipped
        module_outputs = run_modules(pack_root, eligible)
        modules_run = [m['module_id'] for m in eligible]
        opportunity_pool = collect_candidates(run_context['run_id'], module_outputs)
        candidates_generated = opportunity_pool['candidate_count']
        gps_output = run_global_pick_selector(opportunity_pool)
        bankroll_output = run_bankroll_manager(gps_output)
        execution_output = register_execution(bankroll_output, run_context['dry_run'])
    finished_at = datetime.now(timezone.utc).isoformat()
    return {
        'run_id': run_context['run_id'],
        'run_profile': run_context['run_profile'],
        'started_at': run_context['started_at'],
        'finished_at': finished_at,
        'preflight_status': preflight_status,
        'data_api_reference': 'Data_API_Official_Trunk_v1',
        'data_api_status': _status(data_api),
        'official_trunk_status': _status(data_api),
        'modules_run': modules_run,
        'modules_skipped': modules_skipped,
        'candidates_generated': candidates_generated,
        'gps_status': gps_output['status'],
        'bankroll_status': bankroll_output['status'],
        'execution_status': execution_output['status'],
        'warnings': warnings,
        'errors': errors,
        'health_report': {
            'run_id': run_context['run_id'],
            'overall_status': preflight_status,
            'checks': all_checks,
        },
        'final_summary': f"Validation run concluído. Trunk oficial={_status(data_api)}; módulos corridos={len(modules_run)}; candidatas={candidates_generated}; execution={execution_output['status']}."
    }
