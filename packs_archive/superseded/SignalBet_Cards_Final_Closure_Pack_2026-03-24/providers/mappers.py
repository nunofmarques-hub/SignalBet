from __future__ import annotations

from typing import Any, Dict


def map_bundle_to_engine_input(bundle: Dict[str, Any]) -> Dict[str, Any]:
    fixture = bundle["fixture"]
    teams = fixture.get("teams", {})
    card_events = bundle.get("card_events", [])
    home_name = teams.get("home", {}).get("name", "Home")
    away_name = teams.get("away", {}).get("name", "Away")
    return {
        "event_id": bundle["fixture_id"],
        "match_label": f"{home_name} vs {away_name}",
        "competition": fixture.get("league", {}).get("name", "Unknown Competition"),
        "market_family": "cards",
        "market": "match_cards_over",
        "selection": "Over 2.5 Cards",
        "line": 2.5,
        "odds": 1.55,
        "card_events_count": len(card_events),
        "data_quality_flag": "clean",
        "module_specific_payload": {
            "provider": "Data_API_Official_Trunk_v1",
            "provider_object": ["fixtures_by_league_season", "fixture_events"],
            "card_events_detected": len(card_events),
            "consumption_mode": "official_live_provider",
        },
    }
