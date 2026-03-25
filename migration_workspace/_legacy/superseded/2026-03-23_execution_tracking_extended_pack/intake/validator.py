from __future__ import annotations

REQUIRED_FIELDS = {
    "schema_version",
    "source_system",
    "decision_id",
    "pick_id",
    "event_id",
    "module_origin",
    "market_family",
    "market",
    "selection",
    "match_label",
    "decision_status",
    "stake_approved",
    "stake_pct_bankroll",
    "approved_odds_reference",
    "approved_odds_window",
    "portfolio_group",
    "execution_order",
    "rules_triggered",
    "decision_timestamp",
}


def validate_intake_payload(payload: dict) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED_FIELDS - set(payload.keys()))
    if missing:
        errors.append(f"MISSING_REQUIRED_FIELD:{','.join(missing)}")

    if payload.get("source_system") != "BANKROLL_RISK_MANAGER":
        errors.append("INVALID_SOURCE")

    if payload.get("decision_status") != "APPROVED":
        errors.append("INVALID_DECISION_STATUS")

    if payload.get("stake_approved", 0) <= 0:
        errors.append("INVALID_STAKE")

    if payload.get("approved_odds_reference", 0) <= 1.0:
        errors.append("INVALID_ODDS_REFERENCE")

    return errors
