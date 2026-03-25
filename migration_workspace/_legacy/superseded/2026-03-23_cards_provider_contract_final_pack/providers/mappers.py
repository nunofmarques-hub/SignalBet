from __future__ import annotations

from typing import Any, Dict


def to_engine_input(payload: Dict[str, Any]) -> Dict[str, Any]:
    market = payload["market_context"]
    discipline = payload["discipline_context"]
    quality = payload["quality_context"]
    referee = payload.get("referee_context", {})

    return {
        "event_id": payload["event_id"],
        "match_label": payload["match_label"],
        "competition": payload["competition"],
        "kickoff_datetime": payload["kickoff_datetime"],
        "market": market["market"],
        "selection": market["selection"],
        "line": market["line"],
        "odds": market["odds"],
        "projection": discipline["match_cards_projection"],
        "home_projection": discipline["home_cards_projection"],
        "away_projection": discipline["away_cards_projection"],
        "discipline_profile": discipline["discipline_profile"],
        "match_tension_flag": discipline["match_tension_flag"],
        "competitive_pressure": discipline["competitive_pressure"],
        "signal_consistency": discipline["signal_consistency"],
        "home_away_asymmetry": discipline.get("home_away_asymmetry", "unknown"),
        "sample_depth_flag": discipline["sample_depth_flag"],
        "referee_used": referee.get("used", False),
        "referee_bias": referee.get("bias", "unknown"),
        "referee_confidence": referee.get("confidence", "low"),
        "data_quality_flag": quality["data_quality_flag"],
        "source_tag": payload.get("source_tag", "data_api_export"),
    }
