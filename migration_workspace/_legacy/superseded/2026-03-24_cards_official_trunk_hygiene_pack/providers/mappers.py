from __future__ import annotations

from typing import Any, Dict, List


def _normalize_fixture_context(item: Dict[str, Any]) -> Dict[str, Any]:
    fixture = item.get('fixture', {})
    fixture_meta = fixture.get('fixture', {})
    teams = fixture.get('teams', {})
    league = fixture.get('league', {})
    home = teams.get('home', {}).get('name', 'Unknown')
    away = teams.get('away', {}).get('name', 'Unknown')
    cards_count = int(item.get('cards_count', 0))
    return {
        'fixture_id': fixture_meta.get('id'),
        'match_label': f'{home} vs {away}',
        'competition': league.get('name', 'Unknown Competition'),
        'cards_count': cards_count,
    }


def map_context_to_engine_input(context: Dict[str, Any]) -> Dict[str, Any]:
    normalized: List[Dict[str, Any]] = [_normalize_fixture_context(item) for item in context.get('fixture_contexts', [])]
    normalized = [item for item in normalized if item.get('fixture_id') is not None]
    normalized.sort(key=lambda x: x['cards_count'], reverse=True)
    sample_size = len(normalized)
    avg_cards = round(sum(item['cards_count'] for item in normalized) / sample_size, 2) if sample_size else 0.0
    top_fixture = normalized[0] if normalized else {
        'fixture_id': None,
        'match_label': 'Unknown vs Unknown',
        'competition': 'Unknown Competition',
        'cards_count': 0,
    }
    return {
        'source': context.get('source'),
        'official_object': context.get('official_object'),
        'official_provider': context.get('official_provider'),
        'league_id': context.get('league_id'),
        'season': context.get('season'),
        'sample_size': sample_size,
        'avg_cards': avg_cards,
        'top_fixture': top_fixture,
        'all_fixtures': normalized,
    }
