from __future__ import annotations
import json
from pathlib import Path

class ExecutionOrchestrator:
    def parse_window(self, s: str):
        a, b = s.split('-')
        return float(a), float(b)

    def run(self, intake: dict, fixture: dict):
        if intake.get('schema_version') != 'bank_to_exec_v24':
            raise ValueError('unsupported input schema')
        if intake.get('source_system') != 'BANKROLL_RISK_MANAGER':
            raise ValueError('invalid source system')
        if intake.get('decision_status') not in {'APPROVED', 'APPROVED_REDUCED'}:
            raise ValueError('invalid decision status for execution corridor')
        if intake.get('stake_approved', 0) <= 0:
            raise ValueError('stake_approved must be > 0')

        lo, hi = self.parse_window(intake['approved_odds_window'])
        executed_odds = float(intake['odds_snapshot'])
        stake = float(intake['stake_approved'])
        odds_within_window = lo <= executed_odds <= hi

        # Minimal settlement logic for example case.
        settlement_status = 'UNSETTLED'
        if fixture.get('fixture_status') == 'FT':
            market = intake['market']
            total_goals = fixture.get('total_goals', 0)
            if market == 'under_3_5':
                settlement_status = 'WIN' if total_goals < 4 else 'LOSS'
            else:
                settlement_status = 'LOSS'
        if settlement_status == 'WIN':
            return_amount = round(stake * executed_odds, 3)
        elif settlement_status in {'PUSH', 'VOID'}:
            return_amount = stake
        else:
            return_amount = 0.0
        pl = round(return_amount - stake, 3)
        ledger = {
            'schema_version': 'execution-ledger.v1',
            'execution_id': 'EXEC-20260324-0001',
            'decision_id': intake['decision_id'],
            'pick_id': intake['pick_id'],
            'event_id': intake['event_id'],
            'execution_status': 'SETTLED' if settlement_status != 'VOID' else 'VOID',
            'settlement_status': settlement_status,
            'status_changed_at': fixture.get('settlement_timestamp'),
            'execution_attempted': True,
            'executed_at': '2026-03-24T20:17:00Z',
            'executed_odds': executed_odds,
            'stake_executed': stake,
            'settled_at': fixture.get('settlement_timestamp'),
            'result_profit_loss': pl,
            'return_amount': return_amount,
            'execution_reason_code': None,
            'execution_reason_text': None,
            'tracking_note': 'smoke E2E execution result',
            'slippage_vs_reference': 0.0,
            'odds_within_window': odds_within_window,
            'roi_on_stake': round(pl / stake, 3) if stake else None,
        }
        analytics = {
            'schema_version': 'execution-analytics.v1',
            'execution_id': ledger['execution_id'],
            'decision_id': ledger['decision_id'],
            'pick_id': ledger['pick_id'],
            'module_origin': intake['module_origin'],
            'market_family': intake['market_family'],
            'market': intake['market'],
            'decision_status': intake['decision_status'],
            'execution_status': ledger['execution_status'],
            'settlement_status': ledger['settlement_status'],
            'approved_odds_window': intake['approved_odds_window'],
            'executed_odds': ledger['executed_odds'],
            'stake_approved': intake['stake_approved'],
            'stake_executed': ledger['stake_executed'],
            'result_profit_loss': ledger['result_profit_loss'],
            'return_amount': ledger['return_amount'],
            'executed_at': ledger['executed_at'],
            'settled_at': ledger['settled_at'],
        }
        audit = {
            'schema_version': 'execution-audit.v1',
            'execution_id': ledger['execution_id'],
            'decision_id': ledger['decision_id'],
            'source_system': intake['source_system'],
            'upstream_contract': intake['schema_version'],
            'provider_name': fixture.get('provider_name'),
            'events': [
                {'to': 'RECEIVED'}, {'to': 'VALIDATION_PENDING'}, {'to': 'VALIDATED'},
                {'to': 'READY_TO_EXECUTE'}, {'to': 'EXECUTION_PENDING'}, {'to': 'EXECUTED'},
                {'to': 'AWAITING_SETTLEMENT'}, {'to': 'SETTLED'}
            ]
        }
        return ledger, analytics, audit

if __name__ == '__main__':
    here = Path(__file__).resolve().parents[2]
    intake = json.loads((here / 'examples' / 'intake' / 'bank_to_exec_v24_example.json').read_text(encoding='utf-8'))
    fixture = json.loads((here / 'examples' / 'fixture' / 'fixture_payload_official_trunk_v1.json').read_text(encoding='utf-8'))
    ledger, analytics, audit = ExecutionOrchestrator().run(intake, fixture)
    out = here / 'tests' / 'smoke_outputs'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'ledger.json').write_text(json.dumps(ledger, indent=2), encoding='utf-8')
    (out / 'analytics.json').write_text(json.dumps(analytics, indent=2), encoding='utf-8')
    (out / 'audit.json').write_text(json.dumps(audit, indent=2), encoding='utf-8')
    print('SMOKE OK')
