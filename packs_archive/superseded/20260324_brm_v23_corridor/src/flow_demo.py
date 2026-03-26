import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_json(rel_path: str):
    return json.loads((ROOT / rel_path).read_text(encoding="utf-8"))


def simulate_corridor():
    gps_batch = load_json("examples/gps_batch_in_v23.json")
    bank_batch = load_json("examples/bank_resp_batch_v23.json")
    exec_batch = load_json("examples/exec_payload_v23.json")
    return {
        "gps_shortlist_size": gps_batch["shortlist_size"],
        "bank_decisions": len(bank_batch["decisions"]),
        "execution_candidates": len(exec_batch["execution_candidates"]),
        "execution_pick_ids": [c["pick_id"] for c in exec_batch["execution_candidates"]],
    }

if __name__ == "__main__":
    print(json.dumps(simulate_corridor(), indent=2, ensure_ascii=False))
