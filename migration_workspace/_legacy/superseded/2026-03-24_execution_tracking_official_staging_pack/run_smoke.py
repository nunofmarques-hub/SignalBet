
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'src'))
from execution_tracking.orchestrator import ExecutionOrchestrator


def main():
    orch = ExecutionOrchestrator()
    intake = orch.load_example_intake()
    fixture = orch.load_example_fixture()
    ledger = orch.build_ledger()
    analytics = orch.build_analytics_output()

    assert intake['source_system'] == 'BANKROLL_RISK_MANAGER'
    assert intake['decision_status'] in {'APPROVED', 'APPROVED_REDUCED'}
    assert fixture['provider_name'] == 'Data_API_Official_Trunk_v1'
    assert ledger['execution_status'] == 'SETTLED'
    assert analytics['settlement_status'] == 'WIN'

    out = ROOT / 'tests' / 'smoke_outputs'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'ledger.json').write_text(json.dumps(ledger, indent=2, ensure_ascii=False), encoding='utf-8')
    (out / 'analytics.json').write_text(json.dumps(analytics, indent=2, ensure_ascii=False), encoding='utf-8')
    print('SMOKE OK')


if __name__ == '__main__':
    main()
