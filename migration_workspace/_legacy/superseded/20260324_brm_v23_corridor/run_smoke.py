import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from flow_demo import simulate_corridor


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main():
    gps = load("examples/gps_batch_in_v23.json")
    bank = load("examples/bank_resp_batch_v23.json")
    exe = load("examples/exec_payload_v23.json")
    result = simulate_corridor()
    assert gps["shortlist_size"] == 4
    assert len(bank["decisions"]) == 4
    statuses = {d["decision_status"] for d in bank["decisions"]}
    assert statuses == {"APPROVED", "APPROVED_REDUCED", "BLOCKED", "RESERVE"}
    forwarded = [c["pick_id"] for c in exe["execution_candidates"]]
    assert forwarded == ["v12_20260324_001", "corners_20260324_004"]
    assert result["execution_candidates"] == 2
    print("SMOKE PASS - BRM v2.3 corridor pack")


if __name__ == "__main__":
    main()
