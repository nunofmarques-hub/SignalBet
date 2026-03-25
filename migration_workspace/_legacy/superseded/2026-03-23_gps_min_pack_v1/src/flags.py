"""Minimal flags for conflicts, correlation and governance."""
from __future__ import annotations


def build_flags(payload: dict) -> dict:
    conflict_flags: list[str] = []
    correlation_flags: list[str] = []

    if payload.get("data_quality_flag") == "partial":
        correlation_flags.append("GOV_DATA_PARTIAL")
    elif payload.get("data_quality_flag") == "fragile":
        correlation_flags.append("GOV_DATA_FRAGILE")

    if not payload.get("edge_raw"):
        correlation_flags.append("GOV_EDGE_MISSING")

    if len(str(payload.get("rationale_summary", "")).strip()) < 40:
        correlation_flags.append("GOV_RATIONALE_WEAK")

    return {
        "conflict_flags": conflict_flags,
        "correlation_flags": correlation_flags,
    }
