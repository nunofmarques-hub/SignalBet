from __future__ import annotations

from typing import Any, Dict


def map_central_input_to_engine(payload: Dict[str, Any]) -> Dict[str, Any]:
    fixture = payload["fixture"]
    teams = payload["teams"]
    discipline = payload["discipline_context"]
    market = payload["market_context"]
    competition = payload["competition_context"]
    data_quality = payload["data_quality"]

    home = discipline["home_profile"]
    away = discipline["away_profile"]
    referee = discipline.get("referee_profile", {})
    tension = competition.get("match_tension_flag", "medium")

    return {
        "fixture": fixture,
        "teams": teams,
        "market": market,
        "data_quality_flag": data_quality.get("data_quality_flag", "partial"),
        "sample_depth_flag": data_quality.get("sample_depth_flag", "medium"),
        "discipline_profile": {
            "home_cards_avg": home.get("cards_avg", 0.0),
            "away_cards_avg": away.get("cards_avg", 0.0),
            "home_fouls_avg": home.get("fouls_avg", 0.0),
            "away_fouls_avg": away.get("fouls_avg", 0.0),
            "referee_cards_avg": referee.get("cards_avg", 0.0),
            "referee_used": referee.get("known", False),
            "match_tension_flag": tension,
            "competitive_pressure": competition.get("competitive_pressure", "medium"),
            "home_away_asymmetry": competition.get("home_away_asymmetry", "balanced"),
            "recent_intensity_signal": discipline.get("recent_intensity_signal", "neutral"),
        },
    }
