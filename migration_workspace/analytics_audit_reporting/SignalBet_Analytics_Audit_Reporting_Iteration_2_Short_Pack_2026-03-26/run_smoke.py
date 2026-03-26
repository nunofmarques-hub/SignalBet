#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'examples' / 'source_inputs'


def load_json(name: str):
    return json.loads((SRC / name).read_text(encoding='utf-8'))


def write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')


def output_ownership(raw_producers, consolidated_by, primary_consumers):
    return {
        'raw_producers': raw_producers,
        'consolidated_by': consolidated_by,
        'primary_consumers': primary_consumers,
    }


def main():
    gps = load_json('gps_bankroll_export_case_main.json')
    bank = load_json('bank_resp_batch_v24.json')
    bank_exec = load_json('exec_payload_v24.json')
    ex_analytics = load_json('execution_analytics.json')
    ex_audit = load_json('execution_audit.json')
    ex_ledger = load_json('execution_ledger.json')
    orch_sum = load_json('orchestrator_last_sum.json')
    orch_health = load_json('orchestrator_last_health.json')
    orch_ui = load_json('orchestrator_last_ui.json')
    orch_proof = load_json('orchestrator_proof_stdout.json')

    now = datetime.now(timezone.utc).isoformat()
    approved = sum(1 for d in bank['decisions'] if d['decision_status'] == 'APPROVED')
    approved_reduced = sum(1 for d in bank['decisions'] if d['decision_status'] == 'APPROVED_REDUCED')
    blocked = sum(1 for d in bank['decisions'] if d['decision_status'] == 'BLOCKED')
    reserve = sum(1 for d in bank['decisions'] if d['decision_status'] == 'RESERVE')
    modules = sorted({p['module_id'] for p in gps['picks']})

    run_summary = {
        'schema_version': 'analytics_audit_reporting.run_summary.v1_1',
        'generated_at': now,
        'run_id': orch_sum['run_id'],
        'selector_run_id': gps.get('selector_run_id'),
        'orchestrator_runtime_context': {
            'run_profile': orch_sum.get('run_profile'),
            'target_intent': orch_sum.get('target_intent'),
            'readiness_level': orch_sum.get('readiness_level'),
            'preflight_status': orch_sum.get('preflight_status'),
            'official_trunk_status': orch_sum.get('official_trunk_status'),
            'project_feed_coverage_ratio': orch_sum.get('project_feed_coverage_ratio'),
            'health_overall_status': orch_health.get('overall_status'),
            'cta_state': orch_ui.get('cta_state'),
            'ui_screen_status': orch_ui.get('screen_status'),
            'proof_note': orch_proof.get('note')
        },
        'modules_run': orch_sum.get('modules_run', modules),
        'modules_failed': orch_sum.get('modules_failed', []),
        'candidates_seen_gps_export': len(gps['picks']),
        'candidates_generated_orchestrator': orch_sum.get('candidates_generated'),
        'sent_to_bank': len(bank['decisions']),
        'sent_to_execution': len(bank_exec['execution_candidates']),
        'decision_breakdown': {
            'approved': approved,
            'approved_reduced': approved_reduced,
            'blocked': blocked,
            'reserve': reserve
        },
        'pipeline_status': {
            'gps_status': orch_sum.get('gps_status'),
            'bankroll_status': orch_sum.get('bankroll_status'),
            'execution_status': orch_sum.get('execution_status')
        },
        'ownership': output_ownership(
            ['Orchestrator', 'Execution'],
            'Analytics / Audit / Reporting',
            ['operação interna', 'PM']
        ),
        'limitations': [
            'Run summary consolidado a partir de artefactos de out do Orchestrator, não de interface dedicada desta frente.'
        ]
    }

    by_module = {}
    for p in gps['picks']:
        by_module[p['module_id']] = by_module.get(p['module_id'], 0) + 1
    by_status = {}
    for d in bank['decisions']:
        key = d['decision_status'].lower()
        by_status[key] = by_status.get(key, 0) + 1
    by_origin = {
        'gps_export_picks': len(gps['picks']),
        'bank_decisions': len(bank['decisions']),
        'execution_candidates': len(bank_exec['execution_candidates']),
        'orchestrator_modules_run': len(orch_sum.get('modules_run', []))
    }
    system_snapshot = {
        'schema_version': 'analytics_audit_reporting.system_analytics_snapshot.v1_1',
        'generated_at': now,
        'period': 'sample_from_real_project_sources_iter2',
        'sources_used': {
            'gps': 'examples/source_inputs/gps_bankroll_export_case_main.json',
            'bank': 'examples/source_inputs/bank_resp_batch_v24.json',
            'bank_exec': 'examples/source_inputs/exec_payload_v24.json',
            'execution_analytics': 'examples/source_inputs/execution_analytics.json',
            'execution_ledger': 'examples/source_inputs/execution_ledger.json',
            'orchestrator_last_sum': 'examples/source_inputs/orchestrator_last_sum.json',
            'orchestrator_last_ui': 'examples/source_inputs/orchestrator_last_ui.json'
        },
        'total_candidates': len(gps['picks']),
        'by_module': by_module,
        'by_status': by_status,
        'by_origin': by_origin,
        'approvals': approved,
        'reductions': approved_reduced,
        'blocked': blocked,
        'reserve': reserve,
        'executed': len(bank_exec['execution_candidates']),
        'settled': 1 if ex_ledger.get('settlement_status') else 0,
        'orchestrator_counts': orch_ui.get('counts', {}),
        'ownership': output_ownership(
            ['Execution', 'Banca', 'GPS', 'Orchestrator'],
            'Analytics / Audit / Reporting',
            ['operação interna', 'QA', 'governance']
        )
    }

    first_exec = bank_exec['execution_candidates'][0]
    related_bank = next((d for d in bank['decisions'] if d['match_label'] == first_exec['match_label'] and d['decision_status'] == first_exec['decision_status']), None)
    related_gps = next((p for p in gps['picks'] if p['match_label'] == first_exec['match_label']), None)
    trace1 = {
        'schema_version': 'analytics_audit_reporting.audit_trace_sample.v1_1',
        'trace_id': 'trace_sample_001',
        'case_type': 'execution_backed_fact',
        'pick_id': first_exec['pick_id'],
        'event_id': first_exec['event_id'],
        'match_label': first_exec['match_label'],
        'gps_event': {
            'pick_id': related_gps['pick_id'] if related_gps else None,
            'module_id': related_gps['module_id'] if related_gps else None,
            'global_score': related_gps['global_score'] if related_gps else None,
            'selection_status': related_gps['selection_status'] if related_gps else None
        },
        'bank_event': {
            'decision_id': related_bank['decision_id'] if related_bank else None,
            'decision_status': related_bank['decision_status'] if related_bank else None,
            'stake_approved': related_bank['stake_approved'] if related_bank else None
        },
        'execution_event': {
            'execution_id': ex_ledger['execution_id'],
            'execution_status': ex_ledger['execution_status'],
            'settlement_status': ex_ledger['settlement_status'],
            'executed_odds': ex_ledger['executed_odds']
        },
        'run_context': {
            'run_id': orch_sum['run_id'],
            'readiness_level': orch_sum['readiness_level'],
            'cta_state': orch_ui['cta_state']
        },
        'final_status': ex_ledger['settlement_status'],
        'ownership': output_ownership(
            ['GPS', 'Banca', 'Execution', 'Orchestrator'],
            'Analytics / Audit / Reporting',
            ['governance', 'revisão operacional']
        )
    }

    first_module = related_gps['module_id'] if related_gps else None
    second_bank = next((d for d in bank['decisions'] if d['decision_status'] == 'BLOCKED' and d['module_origin'] != first_module), None)
    if second_bank is None:
        second_bank = next((d for d in bank['decisions'] if d['decision_status'] == 'BLOCKED'), bank['decisions'][0])
    second_gps = next((p for p in gps['picks'] if p['pick_id'] == second_bank['pick_id']), None)
    trace2 = {
        'schema_version': 'analytics_audit_reporting.audit_trace_case_2.v1_1',
        'trace_id': 'trace_case_002',
        'case_type': 'blocked_non_execution_case',
        'pick_id': second_bank['pick_id'],
        'event_id': second_bank.get('event_id'),
        'match_label': second_bank['match_label'],
        'gps_event': {
            'pick_id': second_gps['pick_id'] if second_gps else None,
            'module_id': second_gps['module_id'] if second_gps else second_bank.get('module_origin'),
            'global_score': second_gps['global_score'] if second_gps else None,
            'selection_status': second_gps['selection_status'] if second_gps else None
        },
        'bank_event': {
            'decision_id': second_bank['decision_id'],
            'decision_status': second_bank['decision_status'],
            'stake_approved': second_bank.get('stake_approved'),
            'rules_triggered': second_bank.get('rules_triggered', [])
        },
        'execution_event': None,
        'run_context': {
            'run_id': orch_sum['run_id'],
            'run_mode': orch_sum['run_mode'],
            'pipeline_execution_status': orch_sum['execution_status']
        },
        'final_status': 'blocked_pre_execution',
        'ownership': output_ownership(
            ['GPS', 'Banca', 'Orchestrator'],
            'Analytics / Audit / Reporting',
            ['governance', 'revisão operacional']
        )
    }

    modules_block = '\n'.join(f'- {m}' for m in orch_sum['modules_run'])
    daily_reporting = (
        '# Daily Reporting Summary\n\n'
        '## Estado geral da run\n'
        f"- run_id: {orch_sum['run_id']}\n"
        f"- readiness_level: {orch_sum['readiness_level']}\n"
        f"- preflight_status: {orch_sum['preflight_status']}\n"
        f"- official_trunk_status: {orch_sum['official_trunk_status']}\n"
        f"- project_feed_coverage_ratio: {orch_sum['project_feed_coverage_ratio']}\n"
        f"- cta_state: {orch_ui['cta_state']}\n\n"
        '## Módulos ativos\n'
        + modules_block + '\n\n'
        '## Contagens principais\n'
        f"- candidatos gerados pelo Orchestrator: {orch_sum['candidates_generated']}\n"
        f"- candidatos vistos no export GPS: {len(gps['picks'])}\n"
        f"- decisões da Banca: {len(bank['decisions'])}\n"
        f"- enviadas para Execution: {len(bank_exec['execution_candidates'])}\n"
        f"- approved: {approved}\n"
        f"- approved_reduced: {approved_reduced}\n"
        f"- blocked: {blocked}\n"
        f"- reserve: {reserve}\n\n"
        '## Bloqueios / exceções relevantes\n'
        f"- execution_status do Orchestrator: {orch_sum['execution_status']}\n"
        f"- modules_failed: {len(orch_sum['modules_failed'])}\n"
        f"- warnings do Orchestrator: {len(orch_sum.get('warnings', []))}\n"
        f"- errors do Orchestrator: {len(orch_sum.get('errors', []))}\n"
        f"- caso de trace bloqueado incluído nesta iteração: {trace2['pick_id']} ({trace2['gps_event']['module_id']})\n\n"
        '## Nota curta de auditabilidade\n'
        '- trace factual com Execution preservado em `audit/audit_trace_sample.json`\n'
        '- trace bloqueado pré-execution preservado em `audit/audit_trace_case_2.json`\n'
        '- ownership por output explicitado nos artefactos técnicos desta frente\n\n'
        '## Ownership deste output\n'
        '- bruto produzido por: Orchestrator, Execution, Banca, GPS\n'
        '- consolidado por: Analytics / Audit / Reporting\n'
        '- lido por: PM, operação, futura UI quando fizer sentido\n\n'
        '## Limitação remanescente\n'
        '- o contexto do Orchestrator já entra por artefactos runtime do pack `sbo9/out`, mas ainda não existe uma interface dedicada desta frente para consumo desse contexto\n'
    )

    write_json(ROOT / 'analytics' / 'run_summary.json', run_summary)
    write_json(ROOT / 'analytics' / 'system_analytics_snapshot.json', system_snapshot)
    write_json(ROOT / 'audit' / 'audit_trace_sample.json', trace1)
    write_json(ROOT / 'audit' / 'audit_trace_case_2.json', trace2)
    (ROOT / 'reporting' / 'daily_reporting_summary.md').write_text(daily_reporting, encoding='utf-8')

    required = [
        ROOT / 'analytics' / 'run_summary.json',
        ROOT / 'analytics' / 'system_analytics_snapshot.json',
        ROOT / 'audit' / 'audit_trace_sample.json',
        ROOT / 'audit' / 'audit_trace_case_2.json',
        ROOT / 'reporting' / 'daily_reporting_summary.md',
    ]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise SystemExit('Missing outputs: ' + ', '.join(missing))
    print('SMOKE_OK_ITER2')
    for p in required:
        print(p.relative_to(ROOT))


if __name__ == '__main__':
    main()
