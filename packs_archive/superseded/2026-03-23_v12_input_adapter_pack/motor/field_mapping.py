from __future__ import annotations

FIELD_MAPPING = {
    "fixture.fixture_id": "event_id",
    "fixture.match_label": "match_label",
    "fixture.competition": "competition",
    "fixture.kickoff_datetime": "kickoff_datetime",
    "odds_snapshot.selected_odd": "odds",
    "adapter_meta.data_quality_flag": "data_quality_flag",
    "selected_market.edge_pct": "edge_raw",
    "selected_market.score_raw": "score_raw",
    "selected_market.confidence_raw": "confidence_raw",
    "selected_market.risk_raw": "risk_raw",
}
