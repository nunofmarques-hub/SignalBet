"""Normalization rules v1 for Global Pick Selector."""
from __future__ import annotations

TEXT_LEVELS = {
    "muito baixa": 1,
    "baixa": 2,
    "média": 3,
    "media": 3,
    "alta": 4,
    "muito alta": 5,
    "muito baixo": 1,
    "baixo": 2,
    "moderado": 3,
    "alto": 4,
    "muito alto": 5,
}


def _to_float(value) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    return float(str(value).strip().replace("%", "").replace(",", "."))


def normalize_score(module_id: str, score_raw) -> float:
    value = _to_float(score_raw)
    if module_id == "btts" and value <= 10:
        value *= 10
    return max(0.0, min(100.0, value))


def normalize_level(raw_value) -> int:
    if isinstance(raw_value, int):
        return max(1, min(5, raw_value))
    if isinstance(raw_value, float):
        if raw_value <= 5:
            return max(1, min(5, round(raw_value)))
        if raw_value < 25:
            return 1
        if raw_value < 45:
            return 2
        if raw_value < 65:
            return 3
        if raw_value < 85:
            return 4
        return 5
    text = str(raw_value).strip().lower()
    if text not in TEXT_LEVELS:
        raise ValueError(f"unsupported_level:{raw_value}")
    return TEXT_LEVELS[text]


def normalize_edge(edge_raw) -> str:
    if edge_raw is None or edge_raw == "":
        return "weak"
    text = str(edge_raw).strip().lower()
    if text in {"weak", "acceptable", "strong", "very_strong"}:
        return text
    value = _to_float(edge_raw)
    if value < 3:
        return "weak"
    if value < 6:
        return "acceptable"
    if value < 10:
        return "strong"
    return "very_strong"


def normalize_pick(payload: dict) -> dict:
    return {
        "score_norm_base": normalize_score(payload["module_id"], payload["score_raw"]),
        "confidence_norm": normalize_level(payload["confidence_raw"]),
        "risk_norm": normalize_level(payload["risk_raw"]),
        "edge_norm": normalize_edge(payload.get("edge_raw")),
        "normalization_version": "norm.v1.1"
    }
