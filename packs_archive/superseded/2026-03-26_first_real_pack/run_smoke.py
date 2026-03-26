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

def main():
    gps = load_json('gps_bankroll_export_case_main.json')
    bank = load_json('bank_resp_batch_v24.json')
    bank_exec = load_json('exec_payload_v24.json')
    ex_analytics = load_json('execution_analytics.json')
    ex_audit = load_json('execution_audit.json')
    ex_ledger = load_json('execution_ledger.json')

    approved = sum(1 for d in bank['decisions'] if d['decision_status'] == 'APPROVED')
    approved_reduced = sum(1 for d in bank['decisions'] if d['decision_status'] == 'APPROVED_REDUCED')
    blocked = sum(1 for d in bank['decisions'] if d['decision_status'] == 'BLOCKED')
    reserve = sum(1 for d in bank['decisions'] if d['decision_status'] == 'RESERVE')

    run_summary = {
        'schema_version': 'analytics_audit_reporting.run_summary.v1',
        'run_id': gps.get('selector_run_id', 'unknown_run'),
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'orchestrator_context': {
            'pack': 'sbo9',
            'status_note': 'discovery freeze / proof real prepared',
            'source_files': ['orchestrator_README.md', 'orchestrator_STATUS.md']
        },
        'modules_run': sorted({p['module_id'] for p in gps['picks']}),
        'modules_failed': [],
        'candidates_seen': len(gps['picks']),
        'sent_to_bank': len(bank['decisions']),
        'sent_to_execution': len(bank_exec['execution_candidates']),
        'decision_breakdown': {
            'approved': approved,
            'approved_reduced': approved_reduced,
            'blocked': blocked,
            'reserve': reserve
        },
        'warnings': [
            'Pack de consolidação baseado em fontes reais exportadas do repositório oficial.',
            'O contexto de run do Orchestrator nesta iteração vem de README/STATUS e não de um artefacto runtime dedicado.'
        ]
    }

    by_module = {}
    for p in gps['picks']:
        by_module[p['module_id']] = by_module.get(p['module_id'], 0) + 1
    by_status = {}
    for d in bank['decisions']:
        s = d['decision_status'].lower()
        by_status[s] = by_status.get(s, 0) + 1
    system_snapshot = {
        'schema_version': 'analytics_audit_reporting.system_analytics_snapshot.v1',
        'period': 'sample_from_real_project_sources',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'sources_used': {
            'gps': 'examples/source_inputs/gps_bankroll_export_case_main.json',
            'bank': 'examples/source_inputs/bank_resp_batch_v24.json',
            'bank_exec': 'examples/source_inputs/exec_payload_v24.json',
            'execution_analytics': 'examples/source_inputs/execution_analytics.json',
            'execution_ledger': 'examples/source_inputs/execution_ledger.json'
        },
        'total_candidates': len(gps['picks']),
        'by_module': by_module,
        'by_status': by_status,
        'approvals': approved,
        'reductions': approved_reduced,
        'blocked': blocked,
        'reserve': reserve,
        'executed': len(bank_exec['execution_candidates']),
        'settled': 1 if ex_ledger.get('settlement_status') else 0,
        'execution_fact_sample': {
            'pick_id': ex_analytics['pick_id'],
            'module_origin': ex_analytics['module_origin'],
            'execution_status': ex_analytics['execution_status'],
            'settlement_status': ex_analytics['settlement_status'],
            'result_profit_loss': ex_analytics['result_profit_loss']
        }
    }

    first_exec = bank_exec['execution_candidates'][0]
    related_gps = next((p for p in gps['picks'] if p['module_id'] == 'v12' and p['match_label'] == first_exec['match_label']), None)
    related_bank = next((d for d in bank['decisions'] if d['match_label'] == first_exec['match_label'] and d['decision_status'] == first_exec['decision_status']), None)
    audit_trace = {
        'schema_version': 'analytics_audit_reporting.audit_trace_sample.v1',
        'trace_id': 'trace_sample_001',
        'pick_id': first_exec['pick_id'],
        'event_id': first_exec['event_id'],
        'match_label': first_exec['match_label'],
        'gps_event': {
            'source_file': 'examples/source_inputs/gps_bankroll_export_case_main.json',
            'pick_id': related_gps['pick_id'] if related_gps else None,
            'module_id': related_gps['module_id'] if related_gps else None,
            'global_score': related_gps['global_score'] if related_gps else None,
            'selection_status': related_gps['selection_status'] if related_gps else None
        },
        'bank_event': {
            'source_file': 'examples/source_inputs/bank_resp_batch_v24.json',
            'decision_id': related_bank['decision_id'] if related_bank else None,
            'decision_status': related_bank['decision_status'] if related_bank else None,
            'stake_approved': related_bank['stake_approved'] if related_bank else None,
            'rules_triggered': related_bank['rules_triggered'] if related_bank else None
        },
        'execution_event': {
            'source_file': 'examples/source_inputs/execution_ledger.json',
            'execution_id': ex_ledger['execution_id'],
            'execution_status': ex_ledger['execution_status'],
            'settlement_status': ex_ledger['settlement_status'],
            'executed_odds': ex_ledger['executed_odds']
        },
        'audit_event': {
            'source_file': 'examples/source_inputs/execution_audit.json',
            'upstream_contract': ex_audit['upstream_contract'],
            'provider_name': ex_audit['provider_name'],
            'states': [e['to'] for e in ex_audit['events']]
        },
        'run_context': {
            'source_files': ['examples/source_inputs/orchestrator_README.md', 'examples/source_inputs/orchestrator_STATUS.md'],
            'app_core_pack': 'sbo9',
            'note': 'Orchestrator usado como contexto de run e discovery, não como owner do trace factual.'
        },
        'final_status': ex_ledger['settlement_status']
    }

    modules_text = '\n'.join(f'- {m}' for m in sorted({p['module_id'] for p in gps['picks']}))
    summary = (
        '# Daily Reporting Summary\n\n'
        '## Estado operacional\n'
        '- execução de consolidação concluída sem falha estrutural\n'
        '- fontes reais lidas de GPS, Banca, Execution e Orchestrator\n'
        '- corredor central refletido em artefactos técnicos mínimos\n\n'
        '## Módulos ativos\n' + modules_text + '\n\n'
        '## Decisões da Banca\n'
        f'- approved: {approved}\n'
        f'- approved_reduced: {approved_reduced}\n'
        f'- blocked: {blocked}\n'
        f'- reserve: {reserve}\n\n'
        '## Execution\n'
        f'- enviadas para execution: {len(bank_exec["execution_candidates"])}\n'
        f'- caso factual sample: {ex_analytics["pick_id"]} -> {ex_analytics["settlement_status"]}\n'
        f'- profit/loss sample: {ex_analytics["result_profit_loss"]}\n\n'
        '## Alertas curtos\n'
        '- esta iteração consolida fontes reais já exportadas do repositório oficial\n'
        '- o contexto de run do Orchestrator ainda entra por documentação/estado e não por feed runtime dedicado\n'
        '- a camada executiva nasce dos artefactos técnicos gerados neste pack\n'
    )

    write_json(ROOT / 'analytics' / 'run_summary.json', run_summary)
    write_json(ROOT / 'analytics' / 'system_analytics_snapshot.json', system_snapshot)
    write_json(ROOT / 'audit' / 'audit_trace_sample.json', audit_trace)
    (ROOT / 'reporting' / 'daily_reporting_summary.md').write_text(summary, encoding='utf-8')

    required = [
        ROOT / 'analytics' / 'run_summary.json',
        ROOT / 'analytics' / 'system_analytics_snapshot.json',
        ROOT / 'audit' / 'audit_trace_sample.json',
        ROOT / 'reporting' / 'daily_reporting_summary.md'
    ]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise SystemExit('Missing outputs: ' + ', '.join(missing))
    print('SMOKE_OK')
    for p in required:
        print(p.relative_to(ROOT))

if __name__ == '__main__':
    main()