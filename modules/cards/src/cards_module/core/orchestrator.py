from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict

from .eligibility import evaluate_eligibility


def build_output(engine_input: Dict) -> Dict:
    eligible, score_raw, confidence_raw, risk_raw, edge_raw, drivers, penalties, rationale = evaluate_eligibility(engine_input)
    status = "candidate" if eligible else "rejected"
    return {
        "schema_version": "market_pick.v1.1",
        "pick_id": f"cards_{engine_input['event_id']}_{status}",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "module_id": "cards",
        "module_version": "cards.1.0.0",
        "event_id": engine_input["event_id"],
        "match_label": engine_input["match_label"],
        "competition": engine_input["competition"],
        "market_family": "cards",
        "market": engine_input["market"],
        "selection": engine_input["selection"],
        "line": engine_input["line"],
        "odds": engine_input["odds"],
        "eligibility": eligible,
        "score_raw": score_raw,
        "confidence_raw": confidence_raw,
        "risk_raw": risk_raw,
        "edge_raw": edge_raw,
        "rationale_summary": rationale,
        "main_drivers": drivers,
        "penalties": penalties,
        "data_quality_flag": engine_input["data_quality_flag"],
        "module_rank_internal": 1,
        "module_specific_payload": engine_input.get("module_specific_payload", {}),
    }
