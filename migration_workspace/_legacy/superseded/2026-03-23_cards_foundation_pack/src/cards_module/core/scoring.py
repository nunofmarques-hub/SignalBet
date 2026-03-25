"""Scoring helpers."""

from __future__ import annotations

from typing import Dict

from cards_module.config import DEFAULT_WEIGHTS


def compute_score(indicators: Dict[str, float]) -> float:
    score = 0.0
    for key, weight in DEFAULT_WEIGHTS.items():
        score += indicators.get(key, 0.0) * weight
    return round(score, 2)


def derive_confidence(score_raw: float, data_quality_flag: str) -> int:
    base = 4 if score_raw >= 80 else 3 if score_raw >= 70 else 2 if score_raw >= 60 else 1
    if data_quality_flag == "partial":
        base = max(1, base - 1)
    if data_quality_flag in {"fragile", "invalid"}:
        base = 1
    return base


def derive_risk(indicators: Dict[str, float], data_quality_flag: str) -> int:
    risk = 2
    if indicators.get("market_adjustment", 50.0) < 45:
        risk += 1
    if indicators.get("tactical_asymmetry", 0.0) > 60:
        risk += 1
    if data_quality_flag == "partial":
        risk += 1
    if data_quality_flag in {"fragile", "invalid"}:
        risk = 4
    return min(risk, 4)


def derive_edge(projection: float, line: float | None) -> str:
    if line is None or line <= 0:
        return "0.0%"
    edge_pct = ((projection - line) / line) * 100
    return f"{edge_pct:.1f}%"
