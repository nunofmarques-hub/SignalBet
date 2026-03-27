def build_ui_payloads(summary: dict) -> dict:
    requested_mode = "real_read_protected"
    observed_mode = "orchestrator_real_protected" if summary["source_mode"] == "project" else "orchestrator_demo_protected"
    fallback_used = summary["source_mode"] != "project"

    if summary["final_status"] == "green" and summary["source_mode"] == "project":
        bridge_status = "protected_real_ready"
        bridge_scope = "baseline_control_flow"
        source_transition = "requested_protected_to_project"
        bridge_decision_reason = "native trunk baseline available and valid"
    elif summary["final_status"] == "green":
        bridge_status = "controlled_fallback"
        bridge_scope = "baseline_control_flow"
        source_transition = "requested_protected_to_demo"
        bridge_decision_reason = "real trunk baseline unavailable in current environment"
    elif summary["final_status"] == "degraded_run":
        bridge_status = "protected_degraded"
        bridge_scope = "baseline_control_flow"
        source_transition = "requested_protected_to_project_degraded"
        bridge_decision_reason = "native trunk available with degraded state"
    else:
        bridge_status = "blocked"
        bridge_scope = "baseline_control_flow"
        source_transition = "requested_protected_to_blocked"
        bridge_decision_reason = "baseline not usable"

    button_payload = {
        "requested_mode": requested_mode,
        "observed_mode": observed_mode,
        "fallback_used": fallback_used,
        "bridge_status": bridge_status,
        "bridge_scope": bridge_scope,
        "stability_status": summary["stability_status"],
        "source_transition": source_transition,
        "bridge_decision_reason": bridge_decision_reason,
        "readiness_level": summary["readiness_level"],
        "cta_state": summary["cta_state"],
    }

    panel_payload = {
        **button_payload,
        "provider_observed": summary["provider_observed"],
        "baseline_scenario": summary["baseline_scenario"],
        "snapshot_name": summary["snapshot_name"],
        "snapshot_status": summary["snapshot_status"],
        "final_status": summary["final_status"],
        "warnings": summary["warnings"],
        "blockers": summary["blockers"],
        "protected_read": True,
    }
    return {"button_payload": button_payload, "panel_payload": panel_payload}
