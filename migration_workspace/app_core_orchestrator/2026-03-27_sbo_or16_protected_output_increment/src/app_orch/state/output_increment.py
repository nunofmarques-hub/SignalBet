def build_semantic_center(corridor: dict, source_mode: str) -> dict:
    fixtures = corridor["fixtures"]
    stats = corridor["statistics_context"]

    if fixtures["final_status"] == "green":
        readiness_level = "real_ready"
        cta_state = "ready_live"
        final_status = "green"
    elif fixtures["final_status"] == "degraded_run":
        readiness_level = "degraded"
        cta_state = "ready_restricted"
        final_status = "degraded_run"
    else:
        readiness_level = "blocked"
        cta_state = "blocked"
        final_status = "hard_fail"

    warnings = list(fixtures.get("warnings", []))
    blockers = list(fixtures.get("blockers", []))
    if stats["final_status"] != "green":
        warnings.extend(stats.get("warnings", []))

    observed_mode = "orchestrator_real_protected" if source_mode == "project" else "orchestrator_demo_protected"
    bridge_status = "protected_real_ready" if readiness_level == "real_ready" else ("protected_degraded" if readiness_level == "degraded" else "blocked")

    if final_status == "green" and stats["final_status"] == "green":
        central_health = "healthy_enriched"
    elif final_status == "green":
        central_health = "healthy_minimum"
    elif final_status == "degraded_run":
        central_health = "degraded"
    else:
        central_health = "blocked"

    baseline_availability = "available" if fixtures["final_status"] in ("green", "degraded_run") else "unavailable"
    complementary_availability = "available" if stats["available"] else "missing"
    complementary_mode = "non_blocking_enrichment"

    consolidated_state = {
        "main_baseline": {
            "flow_id": fixtures["flow_id"],
            "flow_role": fixtures["flow_role"],
            "provider_observed": fixtures["provider_observed"],
            "scenario": fixtures["scenario"],
            "snapshot_name": fixtures["snapshot_name"],
            "snapshot_status": fixtures["snapshot_status"],
            "final_status": fixtures["final_status"],
        },
        "complementary_flow": {
            "flow_id": stats["flow_id"],
            "flow_role": stats["flow_role"],
            "available": stats["available"],
            "non_blocking": stats["non_blocking"],
            "final_status": stats["final_status"],
            "observed_path": stats["observed_path"],
        },
        "central_run": {
            "source_mode": source_mode,
            "observed_mode": observed_mode,
            "bridge_status": bridge_status,
            "readiness_level": readiness_level,
            "cta_state": cta_state,
            "final_status": final_status,
            "warnings": warnings,
            "blockers": blockers,
            "central_health": central_health,
            "baseline_availability": baseline_availability,
            "complementary_availability": complementary_availability,
            "complementary_mode": complementary_mode,
            "corridor_summary": f"baseline={fixtures['final_status']}; complement={stats['final_status']}; central={final_status}",
        }
    }
    return consolidated_state
