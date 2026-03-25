from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .contracts import (
    REQUIRED_TOP_LEVEL,
    REQUIRED_MARKET_CONTEXT,
    REQUIRED_DISCIPLINE_CONTEXT,
    REQUIRED_QUALITY_CONTEXT,
    VALID_MARKETS,
    VALID_DISCIPLINE_PROFILE,
    VALID_TENSION,
    VALID_PRESSURE,
    VALID_CONSISTENCY,
    VALID_SAMPLE_DEPTH,
    VALID_DATA_QUALITY,
    VALID_REF_BIAS,
)
from .mappers import to_engine_input


def _missing(required: set[str], payload: Dict[str, Any]) -> List[str]:
    return sorted([key for key in required if key not in payload])


def load_central_payload(path: str | Path) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_central_payload(payload: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    errors.extend([f"missing_top_level:{x}" for x in _missing(REQUIRED_TOP_LEVEL, payload)])

    market = payload.get("market_context", {})
    discipline = payload.get("discipline_context", {})
    quality = payload.get("quality_context", {})
    referee = payload.get("referee_context", {})

    errors.extend([f"missing_market_context:{x}" for x in _missing(REQUIRED_MARKET_CONTEXT, market)])
    errors.extend([f"missing_discipline_context:{x}" for x in _missing(REQUIRED_DISCIPLINE_CONTEXT, discipline)])
    errors.extend([f"missing_quality_context:{x}" for x in _missing(REQUIRED_QUALITY_CONTEXT, quality)])

    if market.get("market") and market["market"] not in VALID_MARKETS:
        errors.append("invalid_market")
    if discipline.get("discipline_profile") and discipline["discipline_profile"] not in VALID_DISCIPLINE_PROFILE:
        errors.append("invalid_discipline_profile")
    if discipline.get("match_tension_flag") and discipline["match_tension_flag"] not in VALID_TENSION:
        errors.append("invalid_match_tension_flag")
    if discipline.get("competitive_pressure") and discipline["competitive_pressure"] not in VALID_PRESSURE:
        errors.append("invalid_competitive_pressure")
    if discipline.get("signal_consistency") and discipline["signal_consistency"] not in VALID_CONSISTENCY:
        errors.append("invalid_signal_consistency")
    if discipline.get("sample_depth_flag") and discipline["sample_depth_flag"] not in VALID_SAMPLE_DEPTH:
        errors.append("invalid_sample_depth_flag")
    if quality.get("data_quality_flag") and quality["data_quality_flag"] not in VALID_DATA_QUALITY:
        errors.append("invalid_data_quality_flag")
    if referee.get("bias") and referee["bias"] not in VALID_REF_BIAS:
        errors.append("invalid_referee_bias")

    try:
        if "line" in market:
            float(market["line"])
        if "odds" in market:
            float(market["odds"])
    except (TypeError, ValueError):
        errors.append("invalid_market_numeric_fields")

    return errors


def map_to_engine_input(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    errors = validate_central_payload(payload)
    if errors:
        return {}, errors
    return to_engine_input(payload), []
