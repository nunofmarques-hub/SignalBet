"""Eligibility rules."""

from __future__ import annotations

from typing import List, Tuple

from cards_module.config import DEFAULT_THRESHOLDS


def evaluate_eligibility(
    score_raw: float,
    confidence_raw: int,
    risk_raw: int,
    drivers: List[str],
    data_quality_flag: str,
) -> Tuple[bool, str]:
    if data_quality_flag == "invalid":
        return False, "invalid_data"
    if len(drivers) < DEFAULT_THRESHOLDS["min_driver_count"]:
        return False, "insufficient_driver_convergence"
    if score_raw < DEFAULT_THRESHOLDS["eligible_score_min"]:
        return False, "score_below_threshold"
    if confidence_raw < 3:
        return False, "confidence_below_threshold"
    if risk_raw > DEFAULT_THRESHOLDS["high_risk_max"]:
        return False, "risk_too_high"
    return True, "eligible"
