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


def install_official_service_doubles() -> None:
    data_api = types.ModuleType('data_api')
    services = types.ModuleType('data_api.services')
    fixtures_service = types.ModuleType('data_api.services.fixtures_service')
    events_service = types.ModuleType('data_api.services.events_service')

    def get_fixtures_by_league_season(league_id, season):
        return [
            {'fixture': {'id': 1001}, 'league': {'name': 'La Liga'}, 'teams': {'home': {'name': 'Osasuna'}, 'away': {'name': 'Getafe'}}},
            {'fixture': {'id': 1002}, 'league': {'name': 'La Liga'}, 'teams': {'home': {'name': 'Valencia'}, 'away': {'name': 'Sevilla'}}},
            {'fixture': {'id': 1003}, 'league': {'name': 'La Liga'}, 'teams': {'home': {'name': 'Mallorca'}, 'away': {'name': 'Alaves'}}},
        ]

    def get_fixture_events(fixture_id, league_id, season):
        samples = {
            1001: [
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Red Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
            ],
            1002: [
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Goal', 'detail': 'Normal Goal'},
            ],
            1003: [
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
                {'type': 'Card', 'detail': 'Yellow Card'},
            ],
        }
        return samples[fixture_id]

    fixtures_service.get_fixtures_by_league_season = get_fixtures_by_league_season
    events_service.get_fixture_events = get_fixture_events
    sys.modules['data_api'] = data_api
    sys.modules['data_api.services'] = services
    sys.modules['data_api.services.fixtures_service'] = fixtures_service
    sys.modules['data_api.services.events_service'] = events_service


def test_short_pipeline_green(tmp_out: Path) -> None:
    install_official_service_doubles()
    from cards_module.core.orchestrator import run_cards_pipeline
    from cards_module.io.exporter import write_output
    from cards_module.io.validator import validate_pick

    payload = run_cards_pipeline(140, 2024)
    errors = validate_pick(payload)
    output_path = write_output(payload, tmp_out)

    assert errors == []
    assert payload['module_id'] == 'cards'
    assert payload['eligibility'] is True
    assert payload['module_specific_payload']['official_object_consumed'] == 'fixtures + fixture_events'
    assert output_path.exists()


def test_provider_contract_names_are_official() -> None:
    from providers import contracts

    assert contracts.FIXTURES_SERVICE == 'data_api.services.fixtures_service.get_fixtures_by_league_season'
    assert contracts.EVENTS_SERVICE == 'data_api.services.events_service.get_fixture_events'
    assert contracts.OFFICIAL_SOURCE == 'Data_API_Official_Trunk_v1'


def run_all_tests() -> tuple[int, list[str]]:
    executed: list[str] = []
    tmp_out = BASE / 'out' / 'tests'
    tmp_out.mkdir(parents=True, exist_ok=True)
    test_short_pipeline_green(tmp_out)
    executed.append('test_short_pipeline_green')
    test_provider_contract_names_are_official()
    executed.append('test_provider_contract_names_are_official')
    return len(executed), executed


if __name__ == '__main__':
    count, names = run_all_tests()
    print(f'{count} tests passed')
    for name in names:
        print(f'- {name}')
