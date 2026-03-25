from __future__ import annotations

from typing import Any, Dict


def run_global_pick_selector(opportunity_pool: Dict[str, Any], run_context: Dict[str, Any]) -> Dict[str, Any]:
    shortlist = opportunity_pool.get("candidates", [])[:3]
    return {
        "status": "PASS" if shortlist else "WARN",
        "shortlist_count": len(shortlist),
        "approved_candidates": shortlist,
        "opportunity_pool_ref": opportunity_pool,
    }


def run_bankroll_manager(gps_output: Dict[str, Any], run_context: Dict[str, Any]) -> Dict[str, Any]:
    approved = []
    reduced = []
    blocked = []
    reserve = []
    for candidate in gps_output.get("approved_candidates", []):
        confidence = candidate.get("confidence", 0)
        if confidence >= 0.8:
            approved.append(candidate)
        elif confidence >= 0.7:
            reduced.append(candidate)
        else:
            reserve.append(candidate)
    return {
        "status": "PASS" if (approved or reduced or reserve) else "WARN",
        "approved": approved,
        "reduced": reduced,
        "blocked": blocked,
        "reserve": reserve,
        "gps_ref": gps_output,
    }
