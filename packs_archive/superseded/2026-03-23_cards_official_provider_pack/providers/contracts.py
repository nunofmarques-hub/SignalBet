from __future__ import annotations

REQUIRED_TOP_LEVEL_KEYS = {
    "fixture",
    "teams",
    "competition_context",
    "discipline_context",
    "market_context",
    "data_quality",
}

REQUIRED_FIXTURE_KEYS = {"event_id", "match_label", "competition", "kickoff_datetime"}
REQUIRED_TEAM_KEYS = {"home", "away"}
REQUIRED_DISCIPLINE_KEYS = {"home_profile", "away_profile"}
REQUIRED_MARKET_KEYS = {"market", "selection", "line", "odds"}
