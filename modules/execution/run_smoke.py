from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from execution_tracking.orchestrator import ExecutionOrchestrator
from execution_tracking.tracking_summary_builder import build_tracking_summary


def main() -> int:
    intake = json.loads((ROOT / "examples" / "intake" / "bank_to_exec_v24_example.json").read_text(encoding="utf-8"))
    fixture = json.loads((ROOT / "examples" / "fixture" / "execution_fixture_payload.json").read_text(encoding="utf-8"))

    orchestrator = ExecutionOrchestrator()
    ledger, analytics, audit = orchestrator.run(intake, fixture)

    tracking = build_tracking_summary([
        {
            "pick_id": ledger["pick_id"],
            "execution_status": ledger["execution_status"],
            "settlement_status": ledger["settlement_status"],
            "result": ledger["settlement_status"],
            "pnl": ledger["result_profit_loss"],
            "timestamp": ledger["settled_at"],
        }
    ])

    out = ROOT / "tests" / "smoke_outputs"
    out.mkdir(parents=True, exist_ok=True)
    (out / "ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "analytics.json").write_text(json.dumps(analytics, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "tracking_summary.json").write_text(json.dumps(tracking, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: wrote {out / 'ledger.json'}")
    print(f"OK: wrote {out / 'analytics.json'}")
    print(f"OK: wrote {out / 'audit.json'}")
    print(f"OK: wrote {out / 'tracking_summary.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
