from __future__ import annotations

REQUIRED_TOP_LEVEL = {
    "event_id",
    "match_label",
    "competition",
    "kickoff_datetime",
    "market_context",
    "discipline_context",
    "quality_context",
}

REQUIRED_MARKET_CONTEXT = {"market", "selection", "line", "odds"}
REQUIRED_DISCIPLINE_CONTEXT = {
    "match_cards_projection",
    "home_cards_projection",
    "away_cards_projection",
    "discipline_profile",
    "match_tension_flag",
    "competitive_pressure",
    "signal_consistency",
}
