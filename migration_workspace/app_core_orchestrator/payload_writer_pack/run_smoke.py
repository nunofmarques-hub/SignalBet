from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from orchestrator_payload_writer.demo_cycle import run_demo


def main() -> int:
    output = PROJECT_ROOT / "examples" / "official_cycle_payload.json"
    payload = run_demo(output)

    assert payload["cycle_status"] == "settled", "Final status must be settled"
    assert payload["pick_id"] == "GPS-V12-1208499-O15T-001", "pick_id drift detected"
    assert payload["audit_meta"]["parallel_payloads_allowed"] is False
    assert payload["audit_meta"]["manual_glue_allowed"] is False
    assert len(payload["timeline"]) == 4, "Expected 4 lifecycle steps"

    disk_payload = json.loads(output.read_text(encoding="utf-8"))
    assert disk_payload["pick_id"] == payload["pick_id"]
    assert disk_payload["cycle_status"] == "settled"

    print("SMOKE PASS")
    print(f"pick_id={payload['pick_id']}")
    print(f"cycle_status={payload['cycle_status']}")
    print(f"output={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
