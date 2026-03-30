from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from execution_tracking.tracking_summary_builder import build_tracking_summary


def main() -> int:
    records = [
        {
            "pick_id": "PICK-001",
            "execution_status": "EXECUTED",
            "settlement_status": "UNSETTLED",
            "result": None,
            "pnl": None,
            "timestamp": "2026-03-30T10:15:00Z"
        },
        {
            "pick_id": "PICK-002",
            "execution_status": "SETTLED",
            "settlement_status": "WIN",
            "result": "WIN",
            "pnl": 1.55,
            "timestamp": "2026-03-30T10:20:00Z"
        }
    ]
    payload = build_tracking_summary(records)
    out = ROOT / "tests" / "smoke_outputs" / "tracking_summary.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
