from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from app_orch.hc import env as hc_env, cfg as hc_cfg, data as hc_data, mods as hc_mods, pipe as hc_pipe
from app_orch.orch.mod_run import discover, run_modules
from app_orch.orch.flow import collect, gps, bank, exec_reg
from app_orch.orch.ui import build as build_ui
from app_orch.util.io import write_json

def _status(checks):
    if any(c['status'] == 'FAIL' and c.get('blocking') for c in checks):
        return 'FAIL'
    if any(c['status'] == 'WARN' for c in checks):
        return 'WARN'
    return 'PASS'

def _step(name, status, note=''):
    return {'step_id': name, 'status': status, 'note': note}

def run_validation(ctx: dict):
    pack_root = Path(ctx['pack_root'])
    project_root = ctx['project_root']
    cfg = hc_cfg.run(ctx['pack_root'])
    env = hc_env.run(project_root)
    data = hc_data.run(project_root)
    mods = hc_mods.run(ctx['pack_root'])
    pipe = hc_pipe.run(ctx['pack_root'], project_root)
    checks = cfg + env + data + mods + pipe
    preflight = _status(checks)
    steps = [
        _step('config_check', _status(cfg)),
        _step('environment_check', _status(env)),
        _step('data_api_readiness_check', _status(data), 'Data_API_Official_Trunk_v1'),
    ]
    eligible, skipped = discover(ctx['pack_root'], ctx['run_profile'], ctx.get('forced_modules') or None)
    steps.append(_step('module_discovery', 'PASS' if eligible else 'WARN', f'elegíveis={len(eligible)}'))
    if preflight != 'FAIL':
        mod_results, modules_run, modules_failed = run_modules(project_root, eligible)
        pool = collect(ctx['run_id'], mod_results)
        gps_out = gps(pool)
        bank_out = bank(gps_out)
        exec_out = exec_reg(bank_out, True)
    else:
        mod_results, modules_run, modules_failed = [], [], []
        pool = {'run_id': ctx['run_id'], 'candidate_count': 0, 'candidates': [], 'sources': {}}
        gps_out = {'status': 'SKIPPED', 'shortlist': [], 'selected_count': 0}
        bank_out = {'status': 'SKIPPED', 'approved': [], 'reduced': [], 'blocked': [], 'reserve': []}
        exec_out = {'status': 'SKIPPED', 'message': 'preflight falhou'}
    steps.extend([
        _step('run_market_modules', 'PASS' if modules_run else ('WARN' if eligible else 'SKIPPED'), f'run={len(modules_run)} failed={len(modules_failed)}'),
        _step('collect_candidates', 'PASS' if pool['candidate_count'] else 'WARN', f'cand={pool["candidate_count"]}'),
        _step('run_global_pick_selector', gps_out['status']),
        _step('run_bankroll_manager', bank_out['status']),
        _step('register_execution', exec_out['status']),
    ])
    warnings = [c['message'] for c in checks if c['status'] == 'WARN']
    errors = [c['message'] for c in checks if c['status'] == 'FAIL' and c.get('blocking')]
    for mf in modules_failed:
        warnings.append(f"Módulo {mf['module_id']} falhou: {mf['reason']}.")
    feed_sources = {
        r['module_id']: {
            'type': r.get('source_type', ''),
            'mode': r.get('source_mode', ''),
            'path': r.get('source_path', ''),
            'status': r.get('status', '')
        }
        for r in mod_results
    }
    summary = {
        'run_id': ctx['run_id'],
        'run_profile': ctx['run_profile'],
        'started_at': ctx['started_at'],
        'finished_at': datetime.now(timezone.utc).isoformat(),
        'preflight_status': preflight,
        'data_api_reference': 'Data_API_Official_Trunk_v1',
        'data_api_status': _status(data),
        'official_trunk_status': _status(data),
        'project_root': project_root,
        'project_mode': ctx['project_mode'],
        'checked_paths': ctx['checked_paths'],
        'modules_eligible': [m['module_id'] for m in eligible],
        'modules_run': modules_run,
        'modules_skipped': skipped,
        'modules_failed': modules_failed,
        'module_results': mod_results,
        'module_feed_sources': feed_sources,
        'candidates_generated': pool['candidate_count'],
        'gps_status': gps_out['status'],
        'bankroll_status': bank_out['status'],
        'execution_status': exec_out['status'],
        'approved_count': len(bank_out.get('approved', [])),
        'reduced_count': len(bank_out.get('reduced', [])),
        'blocked_count': len(bank_out.get('blocked', [])),
        'pipeline_steps': steps + [_step('build_run_summary', 'PASS'), _step('return_ui_status', 'PASS')],
        'warnings': warnings,
        'errors': errors,
        'health_report': {'run_id': ctx['run_id'], 'overall_status': preflight, 'checks': checks},
        'final_summary': (
            f"Validation run concluído. trunk={_status(data)}; mode={ctx['project_mode']}; "
            f"elegíveis={len(eligible)}; run={len(modules_run)}; skipped={len(skipped)}; failed={len(modules_failed)}; "
            f"cand={pool['candidate_count']}; gps={gps_out['status']}; banca={bank_out['status']}; exec={exec_out['status']}."
        )
    }
    ui = build_ui(summary)
    write_json(pack_root / 'out' / 'last_health.json', summary['health_report'])
    write_json(pack_root / 'out' / 'last_sum.json', summary)
    write_json(pack_root / 'out' / 'last_ui.json', ui)
    write_json(pack_root / 'examples' / 'out' / 'sample_health.json', summary['health_report'])
    write_json(pack_root / 'examples' / 'out' / 'sample_sum.json', summary)
    write_json(pack_root / 'examples' / 'out' / 'sample_ui.json', ui)
    return {'run_summary': summary, 'ui_status': ui}
