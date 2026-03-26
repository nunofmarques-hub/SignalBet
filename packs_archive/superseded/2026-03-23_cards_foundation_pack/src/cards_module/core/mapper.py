"""Map internal assessment to contract payload."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict

from cards_module.config import MODULE_ID, MODULE_VERSION, SCHEMA_VERSION, MARKET_FAMILY
from cards_module.types import RawAssessment


def build_pick_id(event_id: int, market: str, selection: str, created_at: str) -> str:
    compact_market = market.replace(" ", "_")
    compact_selection = selection.replace(" ", "_")
    ts = created_at.replace(":", "").replace("-", "")
    return f"{MODULE_ID}_{event_id}_{compact_market}_{compact_selection}_{ts}"


def map_to_contract(match_input: Dict[str, Any], assessment: RawAssessment) -> Dict[str, Any]:
    created_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    event_id = match_input["event_id"]
    payload = {
        "schema_version": SCHEMA_VERSION,
        "pick_id": build_pick_id(event_id, assessment.market, assessment.selection, created_at),
        "created_at": created_at,
        "module_id": MODULE_ID,
        "module_version": MODULE_VERSION,
        "event_id": event_id,
        "match_label": match_input["match_label"],
        "competition": match_input["competition"],
        "kickoff_datetime": match_input.get("kickoff_datetime"),
        "market_family": MARKET_FAMILY,
        "market": assessment.market,
        "selection": assessment.selection,
        "line": assessment.line,
        "odds": assessment.odds,
        "eligibility": assessment.eligibility,
        "score_raw": assessment.score_raw,
        "confidence_raw": assessment.confidence_raw,
        "risk_raw": assessment.risk_raw,
        "edge_raw": assessment.edge_raw,
        "rationale_summary": assessment.rationale_summary,
        "main_drivers": assessment.main_drivers,
        "penalties": assessment.penalties,
        "data_quality_flag": assessment.data_quality_flag,
        "module_rank_internal": assessment.module_rank_internal,
        "expiry_context": assessment.expiry_context,
        "module_specific_payload": assessment.module_specific_payload,
    }
    return payload
