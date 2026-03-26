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

OPTIONAL_TOP_LEVEL = {
    "referee_context",
    "source_tag",
    "fixture_context",
}

REQUIRED_MARKET_CONTEXT = {
    "market",
    "selection",
    "line",
    "odds",
}

REQUIRED_DISCIPLINE_CONTEXT = {
    "match_cards_projection",
    "home_cards_projection",
    "away_cards_projection",
    "discipline_profile",
    "match_tension_flag",
    "competitive_pressure",
    "signal_consistency",
    "sample_depth_flag",
}

REQUIRED_QUALITY_CONTEXT = {
    "data_quality_flag",
}

VALID_MARKETS = {
    "match_cards_over",
    "match_cards_under",
    "team_cards_over_home",
    "team_cards_over_away",
}

VALID_DISCIPLINE_PROFILE = {"cold", "warm", "hot", "very_hot"}
VALID_TENSION = {"low", "medium", "high", "very_high"}
VALID_PRESSURE = {"low", "medium", "high"}
VALID_CONSISTENCY = {"low", "medium", "high"}
VALID_SAMPLE_DEPTH = {"low", "medium", "high"}
VALID_DATA_QUALITY = {"clean", "partial", "fragile", "invalid"}
VALID_REF_BIAS = {"under_support", "neutral", "over_support", "unknown"}
