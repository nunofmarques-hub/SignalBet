"""Static config for Cards v1."""

SCHEMA_VERSION = "market_pick.v1.1"
MODULE_ID = "cards"
MODULE_VERSION = "cards.1.0.0"
MARKET_FAMILY = "cards"

DEFAULT_WEIGHTS = {
    "team_profile": 0.25,
    "game_profile": 0.15,
    "referee": 0.20,
    "competitive_context": 0.15,
    "tactical_asymmetry": 0.10,
    "recent_trend": 0.10,
    "market_adjustment": 0.05,
}

DEFAULT_THRESHOLDS = {
    "eligible_score_min": 70.0,
    "watchlist_score_min": 60.0,
    "high_confidence_min": 80.0,
    "high_risk_max": 4,
    "min_driver_count": 3,
}
