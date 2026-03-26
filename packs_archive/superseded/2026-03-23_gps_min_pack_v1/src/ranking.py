"""Ranking formula v1 for Global Pick Selector."""
from __future__ import annotations

CONFIDENCE_POINTS = {1: 20, 2: 40, 3: 60, 4: 80, 5: 100}
RISK_SAFETY_POINTS = {1: 100, 2: 80, 3: 60, 4: 40, 5: 20}
EDGE_POINTS = {"weak": 35, "acceptable": 55, "strong": 75, "very_strong": 90}


def compute_adjustments(payload: dict) -> dict:
    quality = payload.get("data_quality_flag", "clean")
    quality_adjustment = 0
    if quality == "partial":
        quality_adjustment = -4
    elif quality == "fragile":
        quality_adjustment = -9

    rationale_adjustment = 0 if len(str(payload.get("rationale_summary", "")).strip()) >= 40 else -1

    desirable_missing = 0
    for key in ("edge_raw", "main_drivers", "penalties"):
        if not payload.get(key):
            desirable_missing += 1
    if desirable_missing >= 3:
        completeness_adjustment = -3
    elif desirable_missing >= 1:
        completeness_adjustment = -1
    else:
        completeness_adjustment = 0

    return {
        "quality_adjustment": quality_adjustment,
        "conflict_adjustment": 0,
        "correlation_adjustment": 0,
        "rationale_adjustment": rationale_adjustment,
        "completeness_adjustment": completeness_adjustment,
    }


def compute_global_score(score_norm_base: float, confidence_norm: int, risk_norm: int, edge_norm: str, adjustments: dict) -> int:
    base = (
        0.50 * score_norm_base
        + 0.20 * CONFIDENCE_POINTS[confidence_norm]
        + 0.15 * RISK_SAFETY_POINTS[risk_norm]
        + 0.15 * EDGE_POINTS[edge_norm]
    )
    total = base + sum(adjustments.values())
    return max(0, min(100, int(round(total))))
