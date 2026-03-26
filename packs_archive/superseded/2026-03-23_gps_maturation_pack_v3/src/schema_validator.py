from __future__ import annotations

REQUIRED_FIELDS = [
    "schema_version","pick_id","created_at","module_id","module_version","event_id",
    "match_label","competition","market_family","market","selection","odds","eligibility",
    "score_raw","confidence_raw","risk_raw","rationale_summary","data_quality_flag"
]
VALID_MODULE_IDS = {"v12","corners","btts","cards"}
VALID_MARKET_FAMILIES = {"goals","btts","corners","cards"}
VALID_DATA_QUALITY = {"clean","partial","fragile","invalid"}

def validate_pick(payload: dict) -> dict:
    errors, warnings = [], []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            errors.append(f"Missing required field: {field}")
    if errors:
        return {"valid": False, "errors": errors, "warnings": warnings}
    if payload["module_id"] not in VALID_MODULE_IDS:
        errors.append("Invalid module_id")
    if payload["market_family"] not in VALID_MARKET_FAMILIES:
        errors.append("Invalid market_family")
    if payload["data_quality_flag"] not in VALID_DATA_QUALITY:
        errors.append("Invalid data_quality_flag")
    try:
        if float(payload["odds"]) <= 1.0:
            errors.append("odds must be > 1.0")
    except Exception:
        errors.append("odds must be numeric")
    if not isinstance(payload["eligibility"], bool):
        errors.append("eligibility must be boolean")
    if len(str(payload.get("rationale_summary","")).strip()) < 20:
        warnings.append("Weak rationale_summary")
    if payload.get("data_quality_flag") == "invalid":
        errors.append("Data quality invalid")
    return {"valid": not errors, "errors": errors, "warnings": warnings}
