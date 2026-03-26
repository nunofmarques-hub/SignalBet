
REQUIRED_FIELDS = [
    "schema_version", "pick_id", "created_at", "module_id", "module_version",
    "event_id", "match_label", "competition", "market_family", "market",
    "selection", "eligibility", "score_raw", "confidence_raw", "risk_raw",
    "edge_raw", "rationale_summary", "main_drivers", "penalties", "data_quality_flag"
]

ALLOWED_DATA_QUALITY = {"clean", "partial", "fragile", "invalid"}
ALLOWED_MARKETS = {"match_cards_over", "match_cards_under", "team_cards_over_home", "team_cards_over_away"}
