"""Simple contract validator.

This is intentionally lightweight and stdlib-only.
"""

from __future__ import annotations

from typing import Any, Dict, List

ALLOWED_DATA_QUALITY = {"clean", "partial", "fragile", "invalid"}
REQUIRED_FIELDS = {
    "schema_version",
    "pick_id",
    "created_at",
    "module_id",
    "module_version",
    "event_id",
    "match_label",
    "competition",
    "market_family",
    "market",
    "selection",
    "eligibility",
    "score_raw",
    "confidence_raw",
    "risk_raw",
    "edge_raw",
    "rationale_summary",
    "main_drivers",
    "penalties",
    "data_quality_flag",
}


def validate_payload(payload: Dict[str, Any]) -> List[str]:
    errors: List[str] = []

    missing = sorted(REQUIRED_FIELDS - set(payload.keys()))
    if missing:
        errors.append(f"missing_fields:{','.join(missing)}")

    if payload.get("market_family") != "cards":
        errors.append("invalid_market_family")

    if payload.get("data_quality_flag") not in ALLOWED_DATA_QUALITY:
        errors.append("invalid_data_quality_flag")

    if not isinstance(payload.get("eligibility"), bool):
        errors.append("eligibility_must_be_boolean")

    if not isinstance(payload.get("main_drivers", []), list):
        errors.append("main_drivers_must_be_list")

    if not isinstance(payload.get("penalties", []), list):
        errors.append("penalties_must_be_list")

    if "module_specific_payload" in payload and not isinstance(payload["module_specific_payload"], dict):
        errors.append("module_specific_payload_must_be_object")

    return errors
