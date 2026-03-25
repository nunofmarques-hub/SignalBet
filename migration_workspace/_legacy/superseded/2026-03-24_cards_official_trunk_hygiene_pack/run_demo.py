from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))

from cards_module.core.orchestrator import run_cards_pipeline
from cards_module.io.exporter import write_output
from cards_module.io.validator import validate_pick
from providers.official_live_provider import OfficialProviderUnavailable
from tests.test_short_pipeline import install_official_service_doubles


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['live', 'contract-smoke'], default='live')
    parser.add_argument('--league', type=int, default=140)
    parser.add_argument('--season', type=int, default=2024)
    args = parser.parse_args()

    if args.mode == 'contract-smoke':
        install_official_service_doubles()

    try:
        payload = run_cards_pipeline(args.league, args.season)
    except OfficialProviderUnavailable as exc:
        blocked = {
            'status': 'blocked_live_run',
            'reason': str(exc),
            'provider_name': 'Data_API_Official_Trunk_v1',
            'provider_object': 'fixtures + fixture_events'
        }
        out = BASE / 'out'
        out.mkdir(exist_ok=True)
        path = out / 'blocked_live_run.json'
        path.write_text(json.dumps(blocked, indent=2, ensure_ascii=False), encoding='utf-8')
        print(str(exc))
        print(f'Blocked output: {path}')
        return 2

    errors = validate_pick(payload)
    path = write_output(payload, BASE / 'out')
    print(f'Output: {path}')
    print(f'Validation errors: {errors}')
    return 0 if not errors else 1


if __name__ == '__main__':
    raise SystemExit(main())
