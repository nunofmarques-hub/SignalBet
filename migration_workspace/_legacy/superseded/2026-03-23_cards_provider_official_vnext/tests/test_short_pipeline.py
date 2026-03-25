from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "src"))

from providers.official_cards_provider import load_central_payload, map_to_engine_input
from cards_module.core.orchestrator import run_pipeline


def run_case(filename: str) -> tuple[dict, list, list]:
    payload = load_central_payload(BASE / "examples" / "central_inputs" / filename)
    engine_input, provider_errors = map_to_engine_input(payload)
    result, validation_errors = run_pipeline(engine_input)
    return result, provider_errors, validation_errors


def test_hot_over_candidate() -> None:
    result, provider_errors, validation_errors = run_case("official_hot_over.json")
    assert provider_errors == []
    assert validation_errors == []
    assert result["eligibility"] is True


def test_partial_team_rejected_by_tighter_rules() -> None:
    result, provider_errors, validation_errors = run_case("official_partial_team.json")
    assert provider_errors == []
    assert validation_errors == []
    assert result["eligibility"] is False


def test_under_reject() -> None:
    result, provider_errors, validation_errors = run_case("official_under_reject.json")
    assert provider_errors == []
    assert validation_errors == []
    assert result["eligibility"] is False
