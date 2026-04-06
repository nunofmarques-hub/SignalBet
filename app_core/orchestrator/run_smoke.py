import json
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    payload_path = root / "integration_feeds" / "orchestrator" / "latest.json"
    data = json.loads(payload_path.read_text(encoding="utf-8"))

    active_case = data.get("active_case", {})
    system_status = data.get("system_status", {})
    corridor_state = active_case.get("corridor_state", {})

    print("run_ok=1")
    print("payload_path=" + str(payload_path.relative_to(root)))
    print("payload_name=" + str(data.get("payload_name")))
    print("payload_status=" + str(data.get("payload_status")))
    print("pick_id=" + str(active_case.get("pick_id")))
    print("fixture_id=" + str(active_case.get("fixture_id")))
    print("readiness_level=" + str(system_status.get("readiness_level")))
    print("final_status=" + str(system_status.get("final_status")))
    print("shortlist_status=" + str(corridor_state.get("shortlist_status")))
    print("bankroll_status=" + str(corridor_state.get("bankroll_status")))
    print("execution_status=" + str(corridor_state.get("execution_status")))
    print("settlement_status=" + str(corridor_state.get("settlement_status")))


if __name__ == "__main__":
    main()
