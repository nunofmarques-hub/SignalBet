from __future__ import annotations

from typing import Any, Dict


def build_ui_status(run_summary: Dict[str, Any], bankroll_output: Dict[str, Any] | None = None) -> Dict[str, Any]:
    failed = run_summary.get("preflight_status") == "FAIL"
    screen_status = "BLOCKED" if failed else "COMPLETED"
    return {
        "screen_status": screen_status,
        "run_id": run_summary.get("run_id"),
        "system_health": run_summary.get("preflight_status"),
        "data_api_health": run_summary.get("data_api_status"),
        "data_api_reference": run_summary.get("data_api_reference", "Data_API_Official_Trunk_v1"),
        "module_overview": ([{"module_id": m, "status": "READY"} for m in run_summary.get("modules_run", [])] +
                            [{"module_id": m, "status": "SKIPPED"} for m in run_summary.get("modules_skipped", [])]),
        "last_run_summary": run_summary.get("final_summary"),
        "approved_count": len((bankroll_output or {}).get("approved", [])),
        "reduced_count": len((bankroll_output or {}).get("reduced", [])),
        "reserve_count": len((bankroll_output or {}).get("reserve", [])),
        "blocking_message": None if not failed else "Corrida bloqueada por falha na readiness do sistema/tronco oficial.",
        "cta_state": "enabled" if not failed else "disabled",
    }
