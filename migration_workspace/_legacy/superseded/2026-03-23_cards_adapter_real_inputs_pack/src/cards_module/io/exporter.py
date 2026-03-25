
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict


def build_output(data: Dict[str, Any], scores: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    rationale = (
        f"Leitura disciplinar {scores['discipline_profile']} com projeção {scores['projection']:.2f} "
        f"para linha {data['line']:.1f}; tensão {scores['match_tension_flag']} e viés estrutural {scores['structural_bias']}."
    )
    return {
        "schema_version": "market_pick.v1.1",
        "pick_id": f"cards_{data['event_id']}_{data['market']}_{str(data['line']).replace('.', '_')}",
        "created_at": now,
        "module_id": "cards",
        "module_version": "cards.0.2.0-staging",
        "event_id": data["event_id"],
        "match_label": data["match_label"],
        "competition": data["competition"],
        "kickoff_datetime": data.get("kickoff_datetime"),
        "market_family": data["market_family"],
        "market": data["market"],
        "selection": data["selection"],
        "line": data["line"],
        "odds": data["odds"],
        "eligibility": decision["eligibility"],
        "score_raw": scores["score_raw"],
        "confidence_raw": scores["confidence_raw"],
        "risk_raw": scores["risk_raw"],
        "edge_raw": scores["edge_raw"],
        "rationale_summary": rationale,
        "main_drivers": scores["drivers"],
        "penalties": scores["penalties"] + decision["reasons"],
        "data_quality_flag": data["data_quality_flag"],
        "module_rank_internal": 1 if decision["eligibility"] else 99,
        "expiry_context": "refresh_if_odds_move_or_referee_changes",
        "module_specific_payload": {
            "discipline_profile": scores["discipline_profile"],
            "match_cards_projection": scores["projection"],
            "home_cards_projection": round(data["home_context_cards_avg"], 2),
            "away_cards_projection": round(data["away_context_cards_avg"], 2),
            "match_tension_flag": scores["match_tension_flag"],
            "competitive_pressure": data["importance"],
            "referee_used": data["referee_known"],
            "referee_bias": data["referee_bias_vs_league"],
            "home_away_asymmetry": round(abs(data["home_context_cards_avg"] - data["away_context_cards_avg"]), 2),
            "recent_intensity_signal": round(data["home_recent_cards_avg"] + data["away_recent_cards_avg"], 2),
            "structural_bias": scores["structural_bias"],
            "signal_consistency": scores["signal_consistency"],
            "sample_depth_flag": "strong" if data["sample_depth"] >= 12 else "medium" if data["sample_depth"] >= 9 else "weak",
            "source_missing_blocks": data.get("missing_blocks", []),
            "status_at_source": decision["status"],
        },
    }
