def build_ui_safe_status(summary: dict) -> dict:
    return {
        "ui_safe_status": summary["ui_safe_status"],
        "provider_observed": summary["provider_observed"],
        "baseline_scenario": summary["baseline_scenario"],
        "snapshot_status": summary["snapshot_status"],
        "final_status": summary["final_status"],
        "readiness_level": summary["readiness_level"],
        "cta_state": summary["cta_state"],
        "warnings": summary["warnings"],
        "blockers": summary["blockers"],
        "source_mode": summary["source_mode"],
        "protected_read": True,
    }
