def build_protected_output(state: dict) -> dict:
    main = state["main_baseline"]
    comp = state["complementary_flow"]
    run = state["central_run"]

    return {
        # campos preservados para UI atual
        "readiness": "ready" if run["readiness_level"] == "real_ready" else ("restricted" if run["readiness_level"] == "degraded" else "blocked"),
        "readiness_level": run["readiness_level"],
        "cta_state": run["cta_state"],
        "source_mode": run["source_mode"],
        "observed_mode": run["observed_mode"],
        "bridge_status": run["bridge_status"],
        "snapshot_name": main["snapshot_name"],
        "final_status": run["final_status"],

        # semântica central reforçada
        "central_health": run["central_health"],
        "baseline_availability": run["baseline_availability"],
        "complementary_availability": run["complementary_availability"],
        "complementary_mode": run["complementary_mode"],
        "corridor_summary": run["corridor_summary"],
        "baseline_status": main["final_status"],
        "complementary_status": comp["final_status"],

        # higiene operacional
        "warnings": run["warnings"],
        "blockers": run["blockers"],
    }
