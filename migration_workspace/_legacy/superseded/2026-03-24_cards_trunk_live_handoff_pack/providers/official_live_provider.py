from __future__ import annotations

from importlib import import_module
from typing import Any, Dict, List

from .contracts import EVENTS_SERVICE, FIXTURES_SERVICE, OFFICIAL_OBJECT, OFFICIAL_SOURCE


class OfficialProviderUnavailable(RuntimeError):
    pass


def _import_callable(path: str):
    module_path, fn_name = path.rsplit('.', 1)
    try:
        module = import_module(module_path)
    except Exception as exc:
        raise OfficialProviderUnavailable(
            f"Falha ao importar provider oficial '{path}'. Garanta que o tronco Data_API_Official_Trunk_v1 está disponível em data_api/."
        ) from exc
    try:
        return getattr(module, fn_name)
    except AttributeError as exc:
        raise OfficialProviderUnavailable(f"Função oficial em falta: {path}") from exc


def load_cards_context(league_id: int, season: int) -> Dict[str, Any]:
    get_fixtures_by_league_season = _import_callable(FIXTURES_SERVICE)
    get_fixture_events = _import_callable(EVENTS_SERVICE)

    fixtures = get_fixtures_by_league_season(league_id, season)
    if not isinstance(fixtures, list):
        raise ValueError("O provider oficial devolveu fixtures num formato inválido; esperado: list")

    fixture_contexts: List[Dict[str, Any]] = []
    for fixture in fixtures:
        fixture_id = fixture.get('fixture', {}).get('id')
        if fixture_id is None:
            continue
        events = get_fixture_events(fixture_id, league_id, season)
        if not isinstance(events, list):
            events = []
        fixture_contexts.append({
            'fixture': fixture,
            'events': events,
        })

    return {
        'source': OFFICIAL_SOURCE,
        'official_object': OFFICIAL_OBJECT,
        'league_id': league_id,
        'season': season,
        'fixtures_count': len(fixtures),
        'fixture_contexts': fixture_contexts,
    }
