import json
from pathlib import Path

def main() -> None:
    root = Path(__file__).resolve().parent
    payload_path = root / "app_phase1_payload" / "app_phase1_protected_payload.json"
    data = json.loads(payload_path.read_text(encoding="utf-8"))
    print("run_ok=1")
    print("system_status=OK" if "system_status" in data else "system_status=MISSING")
    print("shortlist=OK" if "shortlist" in data else "shortlist=MISSING")
    print("game_cards=OK" if "game_cards" in data else "game_cards=MISSING")
    print("banking_decisions=OK" if "banking_decisions" in data else "banking_decisions=MISSING")
    print("tracking_summary=OK" if "tracking_summary" in data else "tracking_summary=MISSING")
    print("final_status=" + str(data["system_status"].get("final_status")))
    print("cta_state=" + str(data["system_status"].get("cta_state")))

if __name__ == "__main__":
    main()
