def map_operational_state(baseline: dict, source_mode: str) -> dict:
    final_status = baseline.get("final_status", "hard_fail")
    warnings = list(baseline.get("warnings", []))
    blockers = list(baseline.get("blockers", []))

    if final_status == "green":
        readiness_level = "real_ready"
        cta_state = "ready_live"
        ui_safe_status = "baseline_valid"
    elif final_status == "degraded_run":
        readiness_level = "degraded"
        cta_state = "ready_restricted"
        ui_safe_status = "baseline_degraded"
    else:
        readiness_level = "blocked"
        cta_state = "blocked"
        ui_safe_status = "baseline_blocked"
        if not blockers:
            blockers.append("baseline_final_status_not_usable")

    return {
        "provider_observed": baseline.get("provider_observed"),
        "baseline_scenario": baseline.get("baseline_scenario"),
        "snapshot_name": baseline.get("snapshot_name"),
        "snapshot_status": baseline.get("snapshot_status"),
        "final_status": final_status,
        "readiness_level": readiness_level,
        "cta_state": cta_state,
        "warnings": warnings,
        "blockers": blockers,
        "source_mode": source_mode,
        "ui_safe_status": ui_safe_status,
        "native_inputs": baseline.get("native_inputs", {}),
    }
