from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "src"))

from providers.central_cards_provider import CentralCardsProvider
from providers.mappers import map_central_input_to_engine
from cards_module.core.orchestrator import build_pick
from cards_module.io.validator import validate_market_pick
from cards_module.io.exporter import write_output


def main() -> None:
    provider = CentralCardsProvider()
    examples_dir = BASE / "examples" / "central_inputs"
    out_dir = BASE / "out"
    for path in sorted(examples_dir.glob('*.json')):
        payload = provider.load_json(path)
        payload["fixture"]["provider_name"] = provider.get_provider_name()
        engine_input = map_central_input_to_engine(payload)
        pick = build_pick(engine_input)
        kind = 'candidate' if pick['eligibility'] else 'rejected'
        target = write_output(out_dir, f"{path.stem}__{kind}.json", pick)
        errors = validate_market_pick(pick)
        print(f"[{path.name}] -> {target.name} | validation={errors}")


if __name__ == "__main__":
    main()
