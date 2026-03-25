"""Minimal schema validation for Global Pick Selector input payloads."""
from __future__ import annotations

from typing import Any

REQUIRED_FIELDS = [
    "schema_version", "pick_id", "created_at", "module_id", "module_version",
    "event_id", "match_label", "competition", "market_family", "market",
    "selection", "odds", "eligibility", "score_raw", "confidence_raw",
    "risk_raw", "rationale_summary", "data_quality_flag",
]
VALID_MODULE_IDS = {"v12", "corners", "btts", "cards"}
VALID_MARKET_FAMILIES = {"goals", "btts", "corners", "cards"}
VALID_DATA_QUALITY = {"clean", "partial", "fragile", "invalid"}


def validate_payload(payload: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"missing_required:{field}")

    if errors:
        return {"valid": False, "errors": errors, "warnings": warnings}

    if payload["module_id"] not in VALID_MODULE_IDS:
        errors.append("invalid_module_id")
    if payload["market_family"] not in VALID_MARKET_FAMILIES:
        errors.append("invalid_market_family")
    if payload["data_quality_flag"] not in VALID_DATA_QUALITY:
        errors.append("invalid_data_quality_flag")

    try:
        if float(payload["odds"]) <= 1.0:
            errors.append("invalid_odds")
    except Exception:
        errors.append("odds_not_numeric")

    if not isinstance(payload["eligibility"], bool):
        errors.append("eligibility_not_boolean")

    rationale = str(payload.get("rationale_summary", "")).strip()
    if len(rationale) < 25:
        warnings.append("weak_rationale")

    if payload.get("data_quality_flag") == "partial":
        warnings.append("data_quality_partial")
    elif payload.get("data_quality_flag") == "fragile":
        warnings.append("data_quality_fragile")
    elif payload.get("data_quality_flag") == "invalid":
        errors.append("data_quality_invalid")

    return {"valid": not errors, "errors": errors, "warnings": warnings}
