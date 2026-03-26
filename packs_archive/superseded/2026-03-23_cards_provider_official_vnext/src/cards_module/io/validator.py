from __future__ import annotations

from typing import Any, Dict, List
from cards_module.schemas.contract import REQUIRED_OUTPUT_FIELDS

VALID_QUALITY = {"clean", "partial", "fragile", "invalid"}


def validate_output(payload: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for field in REQUIRED_OUTPUT_FIELDS:
        if field not in payload:
            errors.append(f"missing_output:{field}")
    if payload.get("market_family") != "cards":
        errors.append("invalid_market_family")
    if payload.get("data_quality_flag") not in VALID_QUALITY:
        errors.append("invalid_data_quality_flag")
    if not isinstance(payload.get("main_drivers", []), list):
        errors.append("main_drivers_not_list")
    if not isinstance(payload.get("penalties", []), list):
        errors.append("penalties_not_list")
    return errors
