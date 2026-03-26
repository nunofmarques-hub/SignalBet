from __future__ import annotations

from typing import Any, Dict

TENSION_BONUS = {"low": -4, "medium": 0, "high": 6, "very_high": 10}
PRESSURE_BONUS = {"low": -2, "medium": 0, "high": 4}
RECENT_BONUS = {"negative_for_over": -5, "neutral": 0, "positive_for_over": 5}
ASYM_BONUS = {"home_disciplined": -1, "balanced": 0, "away_more_cards_likely": 3, "home_more_cards_likely": 3}


def compute_projection(engine_input: Dict[str, Any]) -> Dict[str, float]:
    profile = engine_input["discipline_profile"]
    team_base = profile["home_cards_avg"] + profile["away_cards_avg"]
    referee_adj = max(profile["referee_cards_avg"] - 4.5, -1.0)
    tension_adj = TENSION_BONUS.get(profile["match_tension_flag"], 0) / 10.0
    pressure_adj = PRESSURE_BONUS.get(profile["competitive_pressure"], 0) / 10.0
    recent_adj = RECENT_BONUS.get(profile["recent_intensity_signal"], 0) / 10.0
    projection = round(team_base + referee_adj + tension_adj + pressure_adj + recent_adj, 2)
    return {
        "match_cards_projection": projection,
        "home_cards_projection": round(profile["home_cards_avg"] + max(referee_adj, 0) * 0.3, 2),
        "away_cards_projection": round(profile["away_cards_avg"] + max(referee_adj, 0) * 0.3, 2),
    }


def compute_score(engine_input: Dict[str, Any], projection: Dict[str, float]) -> Dict[str, Any]:
    market = engine_input["market"]
    profile = engine_input["discipline_profile"]
    line = float(market["line"])
    odds = float(market["odds"])
    diff = projection["match_cards_projection"] - line
    base_score = 62 + int(diff * 8)
    base_score += TENSION_BONUS.get(profile["match_tension_flag"], 0)
    base_score += PRESSURE_BONUS.get(profile["competitive_pressure"], 0)
    base_score += RECENT_BONUS.get(profile["recent_intensity_signal"], 0)
    base_score += ASYM_BONUS.get(profile["home_away_asymmetry"], 0)
    base_score = max(25, min(95, base_score))

    edge = round((projection["match_cards_projection"] - line) / max(line, 1.0) * 100, 1)
    confidence = 4 if base_score >= 80 else 3 if base_score >= 70 else 2 if base_score >= 60 else 1
    risk = 1 if base_score >= 82 and odds <= 2.00 else 2 if base_score >= 70 else 3
    structural_bias = "over" if projection["match_cards_projection"] > line else "under"
    return {
        "score_raw": base_score,
        "confidence_raw": confidence,
        "risk_raw": risk,
        "edge_raw": f"{edge}%",
        "structural_bias": structural_bias,
    }
