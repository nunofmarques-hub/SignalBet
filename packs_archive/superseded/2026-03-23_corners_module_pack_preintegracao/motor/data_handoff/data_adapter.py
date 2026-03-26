from __future__ import annotations
from typing import Any

def adapt_data_layer_input(raw: dict[str, Any]) -> dict[str, Any]:
    return {
        "fixture_id": raw["fixture_context"]["fixture_id"],
        "competition": raw["fixture_context"]["competition"],
        "kickoff_datetime": raw["fixture_context"].get("kickoff_datetime"),
        "home_team_name": raw["fixture_context"]["home_team"]["name"],
        "away_team_name": raw["fixture_context"]["away_team"]["name"],
        "home": raw["home_team_window"],
        "away": raw["away_team_window"],
        "context": raw["match_context"],
    }
