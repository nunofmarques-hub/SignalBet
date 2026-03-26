from __future__ import annotations
from datetime import datetime, timezone
from .models import MarketResult, MatchRecord


def to_market_pick_v1_1(result: MarketResult, match: MatchRecord, odds: float | None = None) -> dict:
    return {
        'schema_version': 'market_pick.v1.1',
        'pick_id': f'btts_{match.fixture_id}_yes',
        'created_at': datetime.now(timezone.utc).isoformat(),
        'module_id': 'btts',
        'module_version': 'btts_engine.v1.1-test',
        'event_id': match.fixture_id,
        'match_label': result.match_label,
        'competition': 'La Liga',
        'kickoff_datetime': match.date,
        'market_family': 'btts',
        'market': 'match_btts',
        'selection': 'BTTS Yes',
        'line': None,
        'odds': odds,
        'eligibility': result.eligibility,
        'score_raw': result.score_raw,
        'confidence_raw': result.confidence_raw,
        'risk_raw': result.risk_raw,
        'edge_raw': result.edge_raw,
        'rationale_summary': result.rationale_summary,
        'main_drivers': result.main_drivers,
        'penalties': result.penalties,
        'data_quality_flag': result.data_quality_flag,
        'module_rank_internal': 1,
        'expiry_context': 'refresh_if_odds_or_inputs_change',
        'module_specific_payload': result.module_specific_payload,
    }
