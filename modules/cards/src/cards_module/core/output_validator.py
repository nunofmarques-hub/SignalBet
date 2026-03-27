REQUIRED_FIELDS = [
    "schema_version", "pick_id", "module_id", "module_version", "event_id",
    "match_label", "competition", "market_family", "market", "selection",
    "line", "odds", "eligibility", "score_raw", "confidence_raw", "risk_raw",
    "edge_raw", "rationale_summary", "main_drivers", "penalties", "data_quality_flag"
]


def validate_output(payload: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"missing:{field}")
    if payload.get("schema_version") != "market_pick.v1.1":
        errors.append("invalid:schema_version")
    if payload.get("module_id") != "cards":
        errors.append("invalid:module_id")
    if payload.get("market_family") != "cards":
        errors.append("invalid:market_family")
    return errors
