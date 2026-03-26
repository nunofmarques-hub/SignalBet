from __future__ import annotations

import sys
import types
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))


def install_official_service_doubles():
    data_api = types.ModuleType('data_api')
    services = types.ModuleType('data_api.services')
    fixtures_service = types.ModuleType('data_api.services.fixtures_service')
    events_service = types.ModuleType('data_api.services.events_service')

    def get_fixtures_by_league_season(league_id, season):
        return [
            {
                'fixture': {'id': 1001},
                'league': {'name': 'La Liga'},
                'teams': {'home': {'name': 'Osasuna'}, 'away': {'name': 'Getafe'}},
            },
            {
                'fixture': {'id': 1002},
                'league': {'name': 'La Liga'},
                'teams': {'home': {'name': 'Valencia'}, 'away': {'name': 'Sevilla'}},
            },
        ]

    def get_fixture_events(fixture_id, league_id, season):
        if fixture_id == 1001:
            return [
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Red Card'},
                {'type': 'Goal', 'detail': 'Normal Goal'},
            ]
        return [
            {'type': 'Card', 'detail': 'Yellow Card'},
            {'type': 'Card', 'detail': 'Yellow Card'},
            {'type': 'Card', 'detail': 'Yellow Card'},
            {'type': 'Card', 'detail': 'Yellow Card'},
            {'type': 'Card', 'detail': 'Yellow Card'},
        ]

    fixtures_service.get_fixtures_by_league_season = get_fixtures_by_league_season
    events_service.get_fixture_events = get_fixture_events

    sys.modules['data_api'] = data_api
    sys.modules['data_api.services'] = services
    sys.modules['data_api.services.fixtures_service'] = fixtures_service
    sys.modules['data_api.services.events_service'] = events_service


def test_short_pipeline_green(tmp_path):
    install_official_service_doubles()
    from cards_module.core.orchestrator import run_cards_pipeline
    from cards_module.io.validator import validate_pick
    from cards_module.io.exporter import write_output

    payload = run_cards_pipeline(140, 2024)
    errors = validate_pick(payload)
    path = write_output(payload, tmp_path)

    assert errors == []
    assert payload['module_id'] == 'cards'
    assert payload['module_specific_payload']['provider_official'].startswith('data_api.services')
    assert path.exists()


def test_provider_contract_names_are_official():
    from providers import contracts
    assert contracts.FIXTURES_SERVICE == 'data_api.services.fixtures_service.get_fixtures_by_league_season'
    assert contracts.EVENTS_SERVICE == 'data_api.services.events_service.get_fixture_events'
