from bootstrap_runtime import configure_paths

BASE = configure_paths(__file__)

from providers.official_live_provider import OfficialLiveProvider
from providers.mappers import map_bundle_to_engine_input
from cards_module.core.orchestrator import build_output
from cards_module.core.output_validator import validate_output


def test_short_pipeline_contract_smoke():
    fixtures = [{
        "fixture": {"id": 12345},
        "teams": {"home": {"name": "Porto"}, "away": {"name": "Braga"}},
        "league": {"name": "Primeira Liga"},
    }]
    events = [{"type": "Card", "detail": "Yellow Card"}, {"type": "Card", "detail": "Yellow Card"}]
    provider = OfficialLiveProvider(
        fixtures_service=lambda league, season: fixtures,
        events_service=lambda fixture_id, league, season: events,
    )
    bundle = provider.fetch_fixture_bundle(140, 2024)
    output = build_output(map_bundle_to_engine_input(bundle))
    assert output["eligibility"] is True
    assert validate_output(output) == []


def test_rejected_when_signal_is_low():
    fixtures = [{
        "fixture": {"id": 12346},
        "teams": {"home": {"name": "Benfica"}, "away": {"name": "Gil Vicente"}},
        "league": {"name": "Primeira Liga"},
    }]
    events = [{"type": "Goal", "detail": "Normal Goal"}]
    provider = OfficialLiveProvider(
        fixtures_service=lambda league, season: fixtures,
        events_service=lambda fixture_id, league, season: events,
    )
    bundle = provider.fetch_fixture_bundle(140, 2024)
    output = build_output(map_bundle_to_engine_input(bundle))
    assert output["eligibility"] is False
    assert validate_output(output) == []
