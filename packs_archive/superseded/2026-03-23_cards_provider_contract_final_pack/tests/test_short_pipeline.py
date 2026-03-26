from __future__ import annotations

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "src"))

from providers.official_cards_provider import load_central_payload, map_to_engine_input
from cards_module.core.orchestrator import run_pipeline


INPUT_DIR = BASE / "examples" / "official_base_inputs"


def run_case(filename: str) -> tuple[dict, list, list]:
    payload = load_central_payload(INPUT_DIR / filename)
    engine_input, provider_errors = map_to_engine_input(payload)
    if provider_errors:
        return {}, provider_errors, []
    result, validation_errors = run_pipeline(engine_input)
    return result, provider_errors, validation_errors


def test_hot_over_candidate() -> None:
    result, provider_errors, validation_errors = run_case("official_hot_over.json")
    assert provider_errors == []
    assert validation_errors == []
    assert result["eligibility"] is True
    assert result["module_version"] == "cards.1.3.0"


def test_partial_team_rejected_by_tighter_rules() -> None:
    result, provider_errors, validation_errors = run_case("official_partial_team.json")
    assert provider_errors == []
    assert validation_errors == []
    assert result["eligibility"] is False
    assert "referee_context_missing" not in result["penalties"]


def test_under_reject() -> None:
    result, provider_errors, validation_errors = run_case("official_under_reject.json")
    assert provider_errors == []
    assert validation_errors == []
    assert result["eligibility"] is False


def test_invalid_provider_contract_case() -> None:
    payload = {
        "event_id": 1,
        "match_label": "Bad vs Input",
        "competition": "Test League",
        "kickoff_datetime": "2026-03-23T20:00:00Z",
        "market_context": {"market": "bad_market", "selection": "Over 4.5 Cards", "line": 4.5, "odds": 1.9},
        "discipline_context": {
            "match_cards_projection": 5.0,
            "home_cards_projection": 2.4,
            "away_cards_projection": 2.6,
            "discipline_profile": "hot",
            "match_tension_flag": "high",
            "competitive_pressure": "high",
            "signal_consistency": "high",
            "sample_depth_flag": "high",
        },
        "quality_context": {"data_quality_flag": "clean"},
    }
    engine_input, provider_errors = map_to_engine_input(payload)
    assert engine_input == {}
    assert "invalid_market" in provider_errors
