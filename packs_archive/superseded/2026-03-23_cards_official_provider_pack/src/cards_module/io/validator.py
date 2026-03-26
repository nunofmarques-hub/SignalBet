from __future__ import annotations

from typing import Any, Dict, List

REQUIRED_FIELDS = [
    "schema_version", "pick_id", "created_at", "module_id", "module_version", "event_id",
    "match_label", "competition", "market_family", "market", "selection", "line", "odds",
    "eligibility", "score_raw", "confidence_raw", "risk_raw", "edge_raw", "rationale_summary",
    "main_drivers", "penalties", "data_quality_flag"
]

ALLOWED_DQ = {"clean", "partial", "fragile", "invalid"}


def validate_market_pick(payload: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"missing:{field}")
    if payload.get("schema_version") != "market_pick.v1.1":
        errors.append("invalid:schema_version")
    if payload.get("module_id") != "cards":
        errors.append("invalid:module_id")
    if payload.get("market_family") != "cards":
        errors.append("invalid:market_family")
    if payload.get("data_quality_flag") not in ALLOWED_DQ:
        errors.append("invalid:data_quality_flag")
    if not isinstance(payload.get("main_drivers", []), list):
        errors.append("invalid:main_drivers")
    if not isinstance(payload.get("penalties", []), list):
        errors.append("invalid:penalties")
    if "module_specific_payload" not in payload:
        errors.append("missing:module_specific_payload")
    return errors
