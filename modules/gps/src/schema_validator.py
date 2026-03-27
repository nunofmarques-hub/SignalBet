from __future__ import annotations
REQUIRED_FIELDS=["schema_version","pick_id","created_at","module_id","module_version","event_id","match_label","competition","market_family","market","selection","odds","eligibility","score_raw","confidence_raw","risk_raw","rationale_summary","data_quality_flag"]
VALID_MODULE_IDS={"v12","corners","btts","cards"}
def validate_pick(payload: dict) -> dict:
    errors=[]
    for f in REQUIRED_FIELDS:
        if f not in payload: errors.append(f"Missing required field: {f}")
    if payload.get("module_id") not in VALID_MODULE_IDS: errors.append("Invalid module_id")
    return {"valid": not errors, "errors": errors, "warnings": []}
