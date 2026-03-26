from __future__ import annotations

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


def main() -> int:
    try:
        payload = run_cards_pipeline(140, 2024)
    except OfficialProviderUnavailable as exc:
        print(f'OFFICIAL_PROVIDER_UNAVAILABLE: {exc}')
        return 2
    out_path = write_output(payload, BASE / 'out')
    errors = validate_pick(payload)
    print(f'Output written to: {out_path}')
    print(f'Validation errors: {errors}')
    return 0 if not errors else 1


if __name__ == '__main__':
    raise SystemExit(main())
