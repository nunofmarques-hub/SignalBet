
from __future__ import annotations

from typing import Any, Dict


def adapt_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    fixture = payload["fixture"]
    comp = payload["competition_context"]
    home = payload["teams"]["home"]["discipline_profile"]
    away = payload["teams"]["away"]["discipline_profile"]
    referee = payload.get("referee_profile", {})
    market = payload["market_snapshot"]
    dq = payload.get("data_quality", {"flag": "invalid", "missing_blocks": ["data_quality"]})

    return {
        "event_id": fixture["event_id"],
        "match_label": fixture["match_label"],
        "kickoff_datetime": fixture.get("kickoff_datetime"),
        "competition": comp["competition"],
        "league_cards_avg": float(comp["league_cards_avg"]),
        "importance": comp.get("importance", "medium"),
        "rivalry_flag": bool(comp.get("rivalry_flag", False)),
        "home_team_name": payload["teams"]["home"].get("name", "Home"),
        "away_team_name": payload["teams"]["away"].get("name", "Away"),
        "home_cards_avg": float(home["cards_avg"]),
        "away_cards_avg": float(away["cards_avg"]),
        "home_context_cards_avg": float(home.get("cards_home_avg", home["cards_avg"])),
        "away_context_cards_avg": float(away.get("cards_away_avg", away["cards_avg"])),
        "home_fouls_avg": float(home["fouls_committed_avg"]),
        "away_fouls_avg": float(away["fouls_committed_avg"]),
        "home_over_rate": float(home["over_4_5_match_rate"]),
        "away_over_rate": float(away["over_4_5_match_rate"]),
        "home_recent_cards_avg": float(home["recent_cards_avg"]),
        "away_recent_cards_avg": float(away["recent_cards_avg"]),
        "sample_depth": min(int(home.get("sample_depth", 0)), int(away.get("sample_depth", 0))),
        "referee_known": bool(referee.get("known", False)),
        "referee_cards_avg": float(referee["cards_avg"]) if referee.get("cards_avg") is not None else None,
        "referee_bias_vs_league": float(referee["bias_vs_league"]) if referee.get("bias_vs_league") is not None else None,
        "referee_sample_depth": int(referee.get("sample_depth", 0)),
        "market_family": market["market_family"],
        "market": market["market"],
        "selection": market["selection"],
        "line": float(market["line"]),
        "odds": float(market["odds"]),
        "data_quality_flag": dq.get("flag", "invalid"),
        "missing_blocks": dq.get("missing_blocks", []),
    }
