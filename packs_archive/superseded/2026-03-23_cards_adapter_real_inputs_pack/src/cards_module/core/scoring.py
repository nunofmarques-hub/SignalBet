
from __future__ import annotations

from typing import Any, Dict


def _importance_score(value: str) -> float:
    return {"low": 0.5, "medium": 1.0, "high": 1.6}.get(value, 1.0)


def compute_scores(data: Dict[str, Any]) -> Dict[str, Any]:
    combined_cards = data["home_context_cards_avg"] + data["away_context_cards_avg"]
    combined_fouls = data["home_fouls_avg"] + data["away_fouls_avg"]
    over_rate_mean = (data["home_over_rate"] + data["away_over_rate"]) / 2.0
    recent_cards = data["home_recent_cards_avg"] + data["away_recent_cards_avg"]
    tension = _importance_score(data["importance"]) + (0.8 if data["rivalry_flag"] else 0.0)

    referee_bonus = 0.0
    if data["referee_known"] and data["referee_cards_avg"] is not None:
        referee_bonus = (data["referee_cards_avg"] - data["league_cards_avg"]) * 0.7

    projection = (combined_cards * 0.45) + (recent_cards * 0.25) + (combined_fouls / 10.0 * 0.20) + (over_rate_mean * 6.0 * 0.10)
    projection += tension + referee_bonus

    structural_bias = "over" if projection >= data["line"] + 0.35 else "under" if projection <= data["line"] - 0.35 else "neutral"
    edge = round(projection - data["line"], 2)

    base_score = 50.0 + (edge * 8.5)
    if data["data_quality_flag"] == "partial":
        base_score -= 6.0
    if not data["referee_known"]:
        base_score -= 3.0
    if data["sample_depth"] < 10:
        base_score -= 4.0

    score_raw = max(0, min(100, round(base_score)))
    confidence_raw = 4 if score_raw >= 78 else 3 if score_raw >= 68 else 2 if score_raw >= 58 else 1
    risk_raw = 1 if data["data_quality_flag"] == "clean" and data["sample_depth"] >= 12 else 2 if data["data_quality_flag"] in {"clean", "partial"} else 3

    discipline_profile = "hot" if projection >= data["league_cards_avg"] + 0.7 else "cold" if projection <= data["league_cards_avg"] - 0.7 else "balanced"
    match_tension_flag = "high" if tension >= 2.2 else "medium" if tension >= 1.2 else "low"
    signal_consistency = "high" if data["sample_depth"] >= 12 and data["data_quality_flag"] == "clean" else "medium" if data["sample_depth"] >= 9 else "low"

    drivers = [
        f"projection={projection:.2f}",
        f"combined_cards={combined_cards:.2f}",
        f"match_tension={match_tension_flag}",
    ]
    if data["referee_known"] and data["referee_cards_avg"] is not None:
        drivers.append(f"referee_cards_avg={data['referee_cards_avg']:.2f}")

    penalties = []
    if not data["referee_known"]:
        penalties.append("missing_referee_context")
    if data["sample_depth"] < 10:
        penalties.append("low_sample_depth")
    if data["data_quality_flag"] != "clean":
        penalties.append(f"data_quality_{data['data_quality_flag']}")

    return {
        "projection": round(projection, 2),
        "score_raw": score_raw,
        "confidence_raw": confidence_raw,
        "risk_raw": risk_raw,
        "edge_raw": edge,
        "structural_bias": structural_bias,
        "discipline_profile": discipline_profile,
        "match_tension_flag": match_tension_flag,
        "signal_consistency": signal_consistency,
        "drivers": drivers,
        "penalties": penalties,
    }
