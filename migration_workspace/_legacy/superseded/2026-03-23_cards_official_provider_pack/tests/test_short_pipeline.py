from __future__ import annotations

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "src"))

from providers.central_cards_provider import CentralCardsProvider
from providers.mappers import map_central_input_to_engine
from cards_module.core.orchestrator import build_pick
from cards_module.io.validator import validate_market_pick


def run() -> None:
    provider = CentralCardsProvider()
    examples = sorted((BASE / "examples" / "central_inputs").glob("*.json"))
    assert examples, "No examples found"
    has_candidate = False
    for path in examples:
        payload = provider.load_json(path)
        payload["fixture"]["provider_name"] = provider.get_provider_name()
        engine_input = map_central_input_to_engine(payload)
        pick = build_pick(engine_input)
        errors = validate_market_pick(pick)
        assert not errors, f"Validation failed for {path.name}: {errors}"
        if pick["eligibility"]:
            has_candidate = True
    assert has_candidate, "Expected at least one eligible candidate"
    print("Short pipeline tests passed.")


if __name__ == "__main__":
    run()
