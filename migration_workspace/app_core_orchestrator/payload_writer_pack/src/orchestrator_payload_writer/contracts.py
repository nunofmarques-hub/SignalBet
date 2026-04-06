from __future__ import annotations

from typing import Any, Dict, List

CONTRACT_VERSION = "signalbet.cycle_payload.v1"
ALLOWED_STATUSES: List[str] = [
    "shortlist_ready",
    "bank_decision_ready",
    "execution_tracking_live",
    "settled",
]


def base_payload(case_id: str, pick_id: str) -> Dict[str, Any]:
    return {
        "contract_version": CONTRACT_VERSION,
        "orchestrator_payload_status": "live",
        "case_id": case_id,
        "pick_id": pick_id,
        "cycle_status": "shortlist_ready",
        "shortlist": {},
        "bankroll_decision": {},
        "execution_tracking": {},
        "settlement": {},
        "audit_meta": {
            "payload_writer": "OfficialCyclePayloadWriter",
            "parallel_payloads_allowed": False,
            "manual_glue_allowed": False,
        },
    }
