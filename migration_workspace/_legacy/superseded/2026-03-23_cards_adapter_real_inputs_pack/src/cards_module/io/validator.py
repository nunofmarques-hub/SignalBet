
from __future__ import annotations

from typing import Dict, List

from cards_module.schemas.contract import REQUIRED_FIELDS, ALLOWED_DATA_QUALITY, ALLOWED_MARKETS


def validate_output(payload: Dict) -> List[str]:
    errors: List[str] = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"missing_required:{field}")
    if payload.get("data_quality_flag") not in ALLOWED_DATA_QUALITY:
        errors.append("invalid_data_quality_flag")
    if payload.get("market") not in ALLOWED_MARKETS:
        errors.append("invalid_market")
    if payload.get("market_family") != "cards":
        errors.append("invalid_market_family")
    if not isinstance(payload.get("main_drivers", []), list):
        errors.append("main_drivers_not_list")
    if not isinstance(payload.get("penalties", []), list):
        errors.append("penalties_not_list")
    return errors
