from __future__ import annotations

from importlib import import_module
from typing import Any, Dict, List

from .contracts import EVENTS_SERVICE, FIXTURES_SERVICE, OFFICIAL_OBJECT, OFFICIAL_SOURCE


class OfficialProviderUnavailable(RuntimeError):
    """Raised when official trunk services are not available."""


def _import_callable(path: str):
    module_path, fn_name = path.rsplit('.', 1)
    try:
        module = import_module(module_path)
    except Exception as exc:
        raise OfficialProviderUnavailable(
            f"Falha ao importar provider oficial '{path}'. Garanta que o Data_API_Official_Trunk_v1 está disponível em data_api/."
        ) from exc
    try:
        return getattr(module, fn_name)
    except AttributeError as exc:
        raise OfficialProviderUnavailable(f"Função oficial em falta: {path}") from exc


def _validate_fixture_shape(fixture: Dict[str, Any]) -> None:
    if not isinstance(fixture, dict):
        raise ValueError('Fixture inválida; esperado dict')
    if 'fixture' not in fixture or 'teams' not in fixture:
        raise ValueError("Fixture inválida; faltam chaves mínimas 'fixture' e 'teams'")


def _count_card_events(events: List[Dict[str, Any]]) -> int:
    count = 0
    for event in events:
        if event.get('type') == 'Card' or 'card' in str(event.get('detail', '')).lower():
            count += 1
    return count


def load_cards_context(league_id: int, season: int) -> Dict[str, Any]:
    get_fixtures_by_league_season = _import_callable(FIXTURES_SERVICE)
    get_fixture_events = _import_callable(EVENTS_SERVICE)

    fixtures = get_fixtures_by_league_season(league_id, season)
    if not isinstance(fixtures, list):
        raise ValueError('O provider oficial devolveu fixtures num formato inválido; esperado list')

    fixture_contexts: List[Dict[str, Any]] = []
    for fixture in fixtures:
        _validate_fixture_shape(fixture)
        fixture_id = fixture.get('fixture', {}).get('id')
        if fixture_id is None:
            continue
        events = get_fixture_events(fixture_id, league_id, season)
        if not isinstance(events, list):
            raise ValueError(f'O provider oficial devolveu events inválidos para fixture {fixture_id}; esperado list')
        fixture_contexts.append(
            {
                'fixture': fixture,
                'events': events,
                'cards_count': _count_card_events(events),
            }
        )

    return {
        'source': OFFICIAL_SOURCE,
        'official_object': OFFICIAL_OBJECT,
        'official_provider': f'{FIXTURES_SERVICE} + {EVENTS_SERVICE}',
        'league_id': league_id,
        'season': season,
        'fixtures_count': len(fixtures),
        'fixture_contexts': fixture_contexts,
    }
