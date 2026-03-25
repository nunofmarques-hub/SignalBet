from __future__ import annotations
from pathlib import Path
from app_orch.hc import env, cfg, data, mods, pipe
from app_orch.orch.mod_run import discover, run_modules
from app_orch.orch.flow import collect, gps, bank, exec_reg
from app_orch.orch.ui import build
from app_orch.util.io import read_json, write_json


def _blocking(checks):
    return any(c['status'] == 'FAIL' and c.get('blocking') for c in checks)


def _project_gate(ctx, feed_stats):
    errors = []
    warnings = []
    if ctx.get('strict_real_project') and ctx['project_mode'] == 'demo':
        errors.append('real_project_root_required_but_demo_used')
    if ctx.get('strict_real_feeds') and feed_stats.get('project', 0) == 0:
        errors.append('real_module_feeds_required_but_not_detected')
    if ctx['project_mode'] == 'demo':
        warnings.append('Modo demo ativo: ligação ao project_root físico real não provada.')
    if feed_stats.get('project', 0) == 0:
        warnings.append('Sem feeds reais de módulo detetados.')
    return errors, warnings


def run_validation(ctx: dict):
    pack_root = Path(ctx['pack_root'])
    project_root = Path(ctx['project_root'])
    checks = []
    pipeline_steps = []

    checks += cfg.run(str(pack_root)); pipeline_steps.append({'step':'config_check','status':'PASS' if not _blocking(checks[-3:]) else 'FAIL'})
    checks += env.run(str(project_root)); pipeline_steps.append({'step':'environment_check','status':'PASS' if not _blocking(checks[-4:]) else 'FAIL'})
    checks += data.run(str(project_root)); pipeline_steps.append({'step':'data_api_readiness_check','status':'PASS' if not _blocking(checks[-8:]) else 'FAIL'})
    checks += mods.run(str(pack_root))
    checks += pipe.run(str(pack_root), str(project_root))

    eligible, skipped = discover(str(pack_root), ctx['run_profile'], ctx.get('forced_modules'))
    pipeline_steps.append({'step':'module_discovery','status':'PASS', 'meta': {'eligible_count': len(eligible), 'skipped_count': len(skipped)}})

    mod_results, ran, failed, feed_stats = run_modules(str(project_root), eligible)
    pipeline_steps.append({'step':'run_market_modules','status':'PASS' if ran else 'WARN', 'meta': {'modules_run': ran, 'modules_failed': failed, 'feed_stats': feed_stats}})

    pool = collect(ctx['run_id'], mod_results)
    pipeline_steps.append({'step':'collect_candidates','status':'PASS', 'meta': {'candidate_count': pool['candidate_count']}})
    gps_out = gps(pool)
    pipeline_steps.append({'step':'run_global_pick_selector','status': gps_out['status'], 'meta': {'selected_count': gps_out['selected_count']}})
    bank_out = bank(gps_out)
    pipeline_steps.append({'step':'run_bankroll_manager','status': bank_out['status'], 'meta': {'approved': len(bank_out['approved']), 'reduced': len(bank_out['reduced']), 'blocked': len(bank_out['blocked'])}})
    exec_out = exec_reg(bank_out, ctx.get('dry_run', True))
    pipeline_steps.append({'step':'register_execution','status': exec_out['status']})

    gate_errors, gate_warnings = _project_gate(ctx, feed_stats)
    preflight_status = 'FAIL' if (_blocking(checks) or gate_errors) else 'PASS'

    module_sources = {
        r['module_id']: {
            'mode': r.get('source_mode', ''),
            'type': r.get('source_type', ''),
            'path': r.get('source_path', ''),
            'status': r.get('status', '')
        }
        for r in mod_results
    }

    run_mode = 'realish' if ctx['project_mode'] != 'demo' else 'demo'
    summary = {
        'run_id': ctx['run_id'],
        'run_profile': ctx['run_profile'],
        'started_at': ctx['started_at'],
        'finished_at': __import__('datetime').datetime.utcnow().isoformat() + 'Z',
        'initiated_by': ctx.get('initiated_by', 'ui_button'),
        'preflight_status': preflight_status,
        'official_trunk_status': 'PASS' if not _blocking(data.run(str(project_root))) else 'FAIL',
        'project_root': str(project_root),
        'project_mode': ctx['project_mode'],
        'run_mode': run_mode,
        'checked_paths': ctx['checked_paths'],
        'strict_real_project': ctx.get('strict_real_project', False),
        'strict_real_feeds': ctx.get('strict_real_feeds', False),
        'modules_eligible': [m['module_id'] for m in eligible],
        'modules_run': ran,
        'modules_skipped': skipped,
        'modules_failed': failed,
        'module_feed_sources': module_sources,
        'module_feed_stats': feed_stats,
        'project_feed_coverage_ratio': round((feed_stats.get('project',0) / max(1, len(eligible))), 3),
        'candidates_generated': pool['candidate_count'],
        'gps_status': gps_out['status'],
        'bankroll_status': bank_out['status'],
        'execution_status': exec_out['status'],
        'approved_count': len(bank_out['approved']),
        'reduced_count': len(bank_out['reduced']),
        'blocked_count': len(bank_out['blocked']),
        'warnings': [c['message'] for c in checks if c['status'] == 'WARN'] + gate_warnings,
        'errors': [c['message'] for c in checks if c['status'] == 'FAIL'] + gate_errors,
        'pipeline_steps': pipeline_steps,
        'final_summary': f"{ctx['run_profile']} concluído em modo {run_mode}. Elegíveis={len(eligible)}, corridos={len(ran)}, failed={len(failed)}, candidatos={pool['candidate_count']}, aprovadas={len(bank_out['approved'])}, coverage_real={round((feed_stats.get('project',0) / max(1, len(eligible))) * 100, 1)}%."
    }
    pipeline_steps.append({'step':'build_run_summary','status':'PASS' if preflight_status == 'PASS' else 'FAIL'})
    ui = build(summary)
    pipeline_steps.append({'step':'return_ui_status','status':'PASS' if ui['screen_status'] != 'BLOCKED' else 'FAIL'})
    summary['pipeline_steps'] = pipeline_steps

    out = pack_root / 'out'
    write_json(out / 'last_health.json', {'run_id': ctx['run_id'], 'overall_status': preflight_status, 'checks': checks})
    write_json(out / 'last_sum.json', summary)
    write_json(out / 'last_ui.json', ui)
    return summary, ui
