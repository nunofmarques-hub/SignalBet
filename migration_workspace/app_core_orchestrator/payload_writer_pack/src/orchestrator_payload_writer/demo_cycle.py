from __future__ import annotations

from pathlib import Path

from orchestrator_payload_writer.payload_writer import OfficialCyclePayloadWriter


def run_demo(output_path: Path) -> dict:
    writer = OfficialCyclePayloadWriter(output_path=output_path)
    pick_id = "GPS-V12-1208499-O15T-001"
    case_id = "cycle-2026-04-05-001"

    writer.create_cycle(
        case_id=case_id,
        pick_id=pick_id,
        shortlist={
            "fixture_id": 1208499,
            "match_label": "Demo FC vs Sample United",
            "source_module": "v12",
            "selection_label": "Over 1.5 Team Goals",
            "candidate_status": "candidate",
            "eligibility": True,
        },
    )

    writer.update_bankroll_decision(
        pick_id=pick_id,
        decision={
            "decision": "APPROVED",
            "stake": 1.0,
            "handoff_to_execution": "confirmed",
        },
    )

    writer.update_execution_tracking(
        pick_id=pick_id,
        tracking={
            "execution_status": "OPEN",
            "ticket_status": "OPEN",
            "tracking_status": "pronto para registo",
        },
    )

    writer.update_settlement(
        pick_id=pick_id,
        settlement={
            "settlement_status": "WIN",
            "result": "WIN",
            "pnl": 0.85,
        },
    )

    return writer.read_payload()


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]
    output = project_root / "examples" / "official_cycle_payload.json"
    final_payload = run_demo(output)
    print("Demo cycle completed.")
    print(f"Final status: {final_payload['cycle_status']}")
    print(f"Payload file: {output}")
