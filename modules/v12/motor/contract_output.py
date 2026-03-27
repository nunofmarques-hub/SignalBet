from datetime import datetime, timezone

def to_contract_pick(row: dict, module_version: str = "v12.10") -> dict:
    ts = datetime.now(timezone.utc).isoformat()
    market_to_family = {
        "TEAM_OVER_ENGINE": "team_over",
        "MATCH_OVER_ENGINE": "match_over",
        "MATCH_UNDER_ENGINE": "match_under",
    }
    return {
        "schema_version": "market_pick.v1.1",
        "pick_id": f"v12_{row['fixture_id']}_{row['market_variant'].lower()}",
        "created_at": ts,
        "module_id": "v12",
        "module_version": module_version,
        "event_id": row["fixture_id"],
        "match_label": row["match_label"],
        "competition": row["competition"],
        "kickoff_datetime": row["kickoff_datetime"],
        "market_family": row["market_family"],
        "market": row["market"],
        "selection": row["selection"],
        "line": row["line"],
        "odds": 1.90,
        "eligibility": row["eligibility"],
        "score_raw": row["score_raw"],
        "confidence_raw": row["confidence_raw"],
        "risk_raw": row["risk_raw"],
        "edge_raw": row["edge_raw"],
        "rationale_summary": f"{row['motor_id']} produced candidate from official Data/API trunk objects.",
        "main_drivers": row["main_drivers"],
        "penalties": row["penalties"],
        "data_quality_flag": "clean",
        "module_rank_internal": 1,
        "expiry_context": "refresh_on_provider_update",
        "module_specific_payload": {
            "motor_id": row["motor_id"],
            "motor_family": market_to_family[row["motor_id"]],
            "market_variant": row["market_variant"],
            "goal_profile": row["goal_profile"],
            "model_window": "season_plus_last5",
            "provider_name": "Data_API_Official_Trunk_v1",
            "required_objects_used": [
                "fixtures_catalog",
                "standings_snapshot",
                "fixture_statistics",
                "team_statistics",
            ],
        },
    }
