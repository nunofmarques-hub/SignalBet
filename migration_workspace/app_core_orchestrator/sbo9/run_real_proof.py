from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from app_orch.launcher.run_val import run_validation_pipeline

def main():
    req = {
        "run_profile": "validation_run_proof",
        "initiated_by": "cli_real_proof",
        "project_root": "",
        "require_real_project_root": True,
        "require_real_module_feeds": True,
        "dry_run": True,
    }
    if len(sys.argv) > 1:
        req["project_root"] = sys.argv[1]
    elif (ROOT / "examples" / "req" / "project_root.txt").exists():
        req["project_root"] = (ROOT / "examples" / "req" / "project_root.txt").read_text(encoding="utf-8").strip()
    summary, ui = run_validation_pipeline(req, ROOT)
    print(json.dumps({"summary": summary, "ui": ui}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
