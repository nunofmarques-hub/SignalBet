"""Indicator calculations for Cards v1.

This is a deliberately simple v1 skeleton.
Real production logic should plug in normalized historical inputs from the Data Layer.
"""

from __future__ import annotations

from typing import Any, Dict


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def compute_indicators(match_input: Dict[str, Any], odds_input: Dict[str, Any]) -> Dict[str, float]:
    home = match_input["teams"]["home"]
    away = match_input["teams"]["away"]
    referee = match_input.get("referee", {})
    context = match_input.get("context", {})
    market = odds_input.get("market", {})

    team_profile = (
        home.get("cards_avg", 0.0)
        + away.get("cards_avg", 0.0)
        + home.get("fouls_committed_avg", 0.0) / 10.0
        + away.get("fouls_committed_avg", 0.0) / 10.0
    ) * 10

    game_profile = (
        home.get("over45_hit_rate", 0.0) + away.get("over45_hit_rate", 0.0)
    ) * 50

    referee_score = 50.0
    if referee:
        referee_score = clamp((referee.get("cards_avg", 4.5) / 6.0) * 100)

    competitive_context = 40.0
    competitive_context += 20.0 if context.get("derby") else 0.0
    competitive_context += 20.0 if context.get("high_table_pressure") else 0.0
    competitive_context += 10.0 if context.get("must_win_side") else 0.0

    tactical_asymmetry = clamp(abs(home.get("cards_avg", 0.0) - away.get("cards_avg", 0.0)) * 20)

    recent_trend = clamp(
        ((home.get("recent_cards_avg", home.get("cards_avg", 0.0))
         + away.get("recent_cards_avg", away.get("cards_avg", 0.0))) / 8.0) * 100
    )

    market_adjustment = 50.0
    line = market.get("line")
    projection = (home.get("cards_avg", 0.0) + away.get("cards_avg", 0.0))
    if isinstance(line, (int, float)):
        diff = projection - line
        market_adjustment = clamp(50 + diff * 15)

    return {
        "team_profile": clamp(team_profile),
        "game_profile": clamp(game_profile),
        "referee": clamp(referee_score),
        "competitive_context": clamp(competitive_context),
        "tactical_asymmetry": clamp(tactical_asymmetry),
        "recent_trend": clamp(recent_trend),
        "market_adjustment": clamp(market_adjustment),
        "projection_total_cards": round(projection, 2),
        "projection_home_cards": round(home.get("cards_avg", 0.0), 2),
        "projection_away_cards": round(away.get("cards_avg", 0.0), 2),
    }
