from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Tuple, List

from .contracts import REQUIRED_TOP_LEVEL, REQUIRED_MARKET_CONTEXT, REQUIRED_DISCIPLINE_CONTEXT


def _missing(required: set[str], payload: Dict[str, Any]) -> List[str]:
    return sorted([key for key in required if key not in payload])


def load_central_payload(path: str | Path) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def map_to_engine_input(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    errors: List[str] = []
    missing_top = _missing(REQUIRED_TOP_LEVEL, payload)
    if missing_top:
        errors.extend([f"missing_top_level:{x}" for x in missing_top])

    market = payload.get("market_context", {})
    discipline = payload.get("discipline_context", {})
    quality = payload.get("quality_context", {})
    referee = payload.get("referee_context", {})

    missing_market = _missing(REQUIRED_MARKET_CONTEXT, market)
    missing_discipline = _missing(REQUIRED_DISCIPLINE_CONTEXT, discipline)
    errors.extend([f"missing_market_context:{x}" for x in missing_market])
    errors.extend([f"missing_discipline_context:{x}" for x in missing_discipline])

    engine = {
        "event_id": payload.get("event_id"),
        "match_label": payload.get("match_label"),
        "competition": payload.get("competition"),
        "kickoff_datetime": payload.get("kickoff_datetime"),
        "market": market.get("market"),
        "selection": market.get("selection"),
        "line": market.get("line"),
        "odds": market.get("odds"),
        "projection": discipline.get("match_cards_projection"),
        "home_projection": discipline.get("home_cards_projection"),
        "away_projection": discipline.get("away_cards_projection"),
        "discipline_profile": discipline.get("discipline_profile"),
        "match_tension_flag": discipline.get("match_tension_flag"),
        "competitive_pressure": discipline.get("competitive_pressure"),
        "signal_consistency": discipline.get("signal_consistency"),
        "home_away_asymmetry": discipline.get("home_away_asymmetry", "unknown"),
        "sample_depth_flag": discipline.get("sample_depth_flag", "medium"),
        "referee_used": referee.get("used", False),
        "referee_bias": referee.get("bias", "unknown"),
        "referee_confidence": referee.get("confidence", "low"),
        "data_quality_flag": quality.get("data_quality_flag", "partial"),
        "source_tag": payload.get("source_tag", "data_api_export"),
    }
    return engine, errors
