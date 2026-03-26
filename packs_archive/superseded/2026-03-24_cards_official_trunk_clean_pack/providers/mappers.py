from __future__ import annotations

from typing import Any, Dict, List


def _is_card_event(event: Dict[str, Any]) -> bool:
    event_type = str(event.get('type', '')).lower()
    detail = str(event.get('detail', '')).lower()
    return event_type == 'card' or 'card' in detail


def map_context_to_engine_input(context: Dict[str, Any]) -> Dict[str, Any]:
    fixture_rows: List[Dict[str, Any]] = []
    all_card_events = 0
    for item in context.get('fixture_contexts', []):
        fixture = item.get('fixture', {})
        events = item.get('events', [])
        card_events = [e for e in events if _is_card_event(e)]
        all_card_events += len(card_events)
        fixture_rows.append({
            'fixture_id': fixture.get('fixture', {}).get('id'),
            'match_label': f"{fixture.get('teams', {}).get('home', {}).get('name', 'Home')} vs {fixture.get('teams', {}).get('away', {}).get('name', 'Away')}",
            'competition': fixture.get('league', {}).get('name', 'Unknown Competition'),
            'cards_count': len(card_events),
        })

    sample_size = len(fixture_rows)
    avg_cards = round(all_card_events / sample_size, 2) if sample_size else 0.0
    hottest = max(fixture_rows, key=lambda row: row['cards_count'], default={
        'fixture_id': None,
        'match_label': 'Unknown vs Unknown',
        'competition': 'Unknown Competition',
        'cards_count': 0,
    })
    return {
        'source': context.get('source'),
        'official_object': context.get('official_object'),
        'official_provider': context.get('official_provider'),
        'league_id': context.get('league_id'),
        'season': context.get('season'),
        'sample_size': sample_size,
        'avg_cards': avg_cards,
        'top_fixture': hottest,
        'fixtures_cards_summary': fixture_rows,
    }
