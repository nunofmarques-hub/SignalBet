from __future__ import annotations
from datetime import datetime, timezone
from .models import MatchInput, MarketResult

def export_market_pick(match: MatchInput, result: MarketResult) -> dict:
    selection = "BTTS Yes" if match.selection_hint == "yes" else "BTTS No"
    return {
        "schema_version": "market_pick.v1.1",
        "pick_id": f"btts_{match.event_id}_{match.selection_hint}",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "module_id": "btts",
        "module_version": "btts_engine.v1.1",
        "event_id": match.event_id,
        "match_label": match.match_label,
        "competition": match.competition,
        "kickoff_datetime": match.kickoff_datetime,
        "market_family": "btts",
        "market": match.market,
        "selection": selection,
        "line": None,
        "odds": match.odds.get("btts_yes" if match.selection_hint == "yes" else "btts_no"),
        "eligibility": result.eligibility,
        "score_raw": result.score_raw,
        "confidence_raw": result.confidence_raw,
        "risk_raw": result.risk_raw,
        "edge_raw": result.edge_raw,
        "rationale_summary": result.rationale_summary,
        "main_drivers": result.main_drivers,
        "penalties": result.penalties,
        "data_quality_flag": result.data_quality_flag,
        "module_rank_internal": 1,
        "expiry_context": "refresh_if_odds_move_5pct",
        "module_specific_payload": result.module_specific_payload,
    }
