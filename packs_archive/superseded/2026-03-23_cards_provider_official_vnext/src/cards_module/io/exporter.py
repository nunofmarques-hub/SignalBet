from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict


def build_output(engine_input: Dict[str, Any], scored: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    event_id = engine_input["event_id"]
    market = engine_input["market"]
    line = engine_input["line"]
    status = decision["status"]
    drivers = [
        f"projection={scored['projection']}",
        f"discipline_profile={engine_input['discipline_profile']}",
        f"match_tension={engine_input['match_tension_flag']}",
        f"competitive_pressure={engine_input['competitive_pressure']}",
    ]
    if engine_input.get("referee_used"):
        drivers.append(f"referee_bias={engine_input['referee_bias']}")

    rationale = (
        f"Leitura disciplinar {engine_input['discipline_profile']} com tensão {engine_input['match_tension_flag']} "
        f"e pressão competitiva {engine_input['competitive_pressure']}; projeção {scored['projection']} para linha {line}."
    )

    return {
        "schema_version": "market_pick.v1.1",
        "pick_id": f"cards_{event_id}_{market}_{str(line).replace('.', '')}_{status}",
        "created_at": now,
        "module_id": "cards",
        "module_version": "cards.1.2.0",
        "event_id": event_id,
        "match_label": engine_input["match_label"],
        "competition": engine_input["competition"],
        "kickoff_datetime": engine_input["kickoff_datetime"],
        "market_family": "cards",
        "market": market,
        "selection": engine_input["selection"],
        "line": line,
        "odds": engine_input["odds"],
        "eligibility": decision["eligibility"],
        "score_raw": scored["score_raw"],
        "confidence_raw": scored["confidence_raw"],
        "risk_raw": scored["risk_raw"],
        "edge_raw": scored["edge_raw"],
        "rationale_summary": rationale,
        "main_drivers": drivers,
        "penalties": decision["penalties"],
        "data_quality_flag": engine_input["data_quality_flag"],
        "module_rank_internal": 1 if decision["eligibility"] else 999,
        "expiry_context": "refresh_if_line_or_referee_changes",
        "module_specific_payload": {
            "discipline_profile": engine_input["discipline_profile"],
            "match_cards_projection": scored["projection"],
            "home_cards_projection": engine_input["home_projection"],
            "away_cards_projection": engine_input["away_projection"],
            "match_tension_flag": engine_input["match_tension_flag"],
            "competitive_pressure": engine_input["competitive_pressure"],
            "referee_used": engine_input["referee_used"],
            "referee_bias": engine_input["referee_bias"],
            "referee_confidence": engine_input["referee_confidence"],
            "home_away_asymmetry": engine_input["home_away_asymmetry"],
            "signal_consistency": engine_input["signal_consistency"],
            "sample_depth_flag": engine_input["sample_depth_flag"],
            "source_tag": engine_input["source_tag"],
        },
    }
