from __future__ import annotations

from typing import Any, Dict


def run_global_pick_selector(opportunity_pool: Dict[str, Any], run_context: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "status": "PASS",
        "shortlist_count": 0,
        "approved_candidates": [],
        "opportunity_pool_ref": opportunity_pool,
    }


def run_bankroll_manager(gps_output: Dict[str, Any], run_context: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "status": "PASS",
        "approved": [],
        "reduced": [],
        "blocked": [],
        "reserve": [],
        "gps_ref": gps_output,
    }
