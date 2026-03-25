from __future__ import annotations

from typing import Any, Dict

PROFILE_BONUS = {"cold": -6, "warm": 2, "hot": 7, "very_hot": 10}
TENSION_BONUS = {"low": -5, "medium": 1, "high": 6, "very_high": 9}
PRESSURE_BONUS = {"low": -2, "medium": 2, "high": 5}
CONSISTENCY_BONUS = {"low": -4, "medium": 2, "high": 5}
REF_BONUS = {"under_support": -4, "neutral": 0, "over_support": 4, "unknown": 0}
QUALITY_PENALTY = {"clean": 0, "partial": -6, "fragile": -12, "invalid": -30}


def compute_score(engine_input: Dict[str, Any]) -> Dict[str, Any]:
    projection = float(engine_input.get("projection") or 0.0)
    line = float(engine_input.get("line") or 0.0)
    odds = float(engine_input.get("odds") or 0.0)
    edge = round(projection - line, 2)

    base = 60
    base += PROFILE_BONUS.get(engine_input.get("discipline_profile"), 0)
    base += TENSION_BONUS.get(engine_input.get("match_tension_flag"), 0)
    base += PRESSURE_BONUS.get(engine_input.get("competitive_pressure"), 0)
    base += CONSISTENCY_BONUS.get(engine_input.get("signal_consistency"), 0)
    base += REF_BONUS.get(engine_input.get("referee_bias"), 0)
    base += QUALITY_PENALTY.get(engine_input.get("data_quality_flag"), -6)

    # Match market direction.
    selection = str(engine_input.get("selection") or "").lower()
    if selection.startswith("over"):
        base += 8 if edge >= 0.6 else (3 if edge >= 0.2 else -6)
    elif selection.startswith("under"):
        base += 8 if edge <= -0.6 else (3 if edge <= -0.2 else -6)

    if 1.70 <= odds <= 2.10:
        base += 2

    score = max(0, min(100, int(round(base))))
    confidence = 4 if score >= 82 else 3 if score >= 74 else 2 if score >= 65 else 1
    risk = 1 if engine_input.get("data_quality_flag") == "clean" and engine_input.get("signal_consistency") == "high" else 2 if score >= 70 else 3
    return {
        "score_raw": score,
        "confidence_raw": confidence,
        "risk_raw": risk,
        "edge_raw": f"{edge:+.2f}",
        "projection": projection,
    }
