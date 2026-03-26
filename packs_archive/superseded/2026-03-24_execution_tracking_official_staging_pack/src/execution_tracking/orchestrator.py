
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class ExecutionOrchestrator:
    def load_example_intake(self) -> dict:
        path = ROOT / 'examples' / 'intake' / 'bankroll_execution_intake_real_v1.json'
        return json.loads(path.read_text(encoding='utf-8'))

    def load_example_fixture(self) -> dict:
        path = ROOT / 'examples' / 'fixture' / 'fixture_payload_official_trunk_v1.json'
        return json.loads(path.read_text(encoding='utf-8'))

    def build_ledger(self) -> dict:
        path = ROOT / 'examples' / 'ledger' / 'execution_ledger_settled_win_official_v1.json'
        return json.loads(path.read_text(encoding='utf-8'))

    def build_analytics_output(self) -> dict:
        path = ROOT / 'examples' / 'analytics' / 'execution_analytics_output_settled_win_official_v1.json'
        return json.loads(path.read_text(encoding='utf-8'))
