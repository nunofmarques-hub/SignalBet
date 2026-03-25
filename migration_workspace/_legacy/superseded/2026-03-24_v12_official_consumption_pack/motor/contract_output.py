from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict


def build_market_pick_v11(data: Dict, scored: Dict) -> Dict:
    return {
        "schema_version": "market_pick.v1.1",
        "module_id": "v12",
        "module_version": "v12.10",
        "pick_id": f"v12_{data['fixture_id']}_{scored['market_variant'].lower()}",
        "event_id": data["fixture_id"],
        "match_label": scored["match_label"],
        "competition": scored["competition"],
        "kickoff_datetime": scored["kickoff_datetime"],
        "market_family": scored["market_family"],
        "market": scored["market"],
        "selection": scored["selection"],
        "line": scored["line"],
        "odds": 1.85,
        "eligibility": scored["eligibility"],
        "score_raw": scored["score_raw"],
        "confidence_raw": scored["confidence_raw"],
        "risk_raw": scored["risk_raw"],
        "edge_raw": scored["edge_raw"],
        "rationale_summary": (
            f"Output gerado pela v12 com consumo "
            f"{data['provider_name']} ({data['provider_source']})."
        ),
        "main_drivers": scored["main_drivers"],
        "penalties": scored["penalties"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "data_quality_flag": (
            "clean" if data["provider_source"] == "official_default" else "partial"
        ),
        "module_rank_internal": 1,
        "expiry_context": "refresh_if_provider_snapshot_changes",
        "module_specific_payload": {
            "motor_id": scored["motor_id"],
            "motor_family": (
                "team_over"
                if scored["motor_id"] == "TEAM_OVER_ENGINE"
                else "match_over"
                if scored["motor_id"] == "MATCH_OVER_ENGINE"
                else "match_under"
            ),
            "market_variant": scored["market_variant"],
            "goal_profile": scored["goal_profile"],
            "model_window": "season_plus_last5",
            "current_core_status": "active_core",
        },
    }