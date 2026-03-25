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
    req = {"run_profile": "validation_run", "initiated_by": "smoke", "dry_run": True}
    summary, ui = run_validation_pipeline(req, ROOT)
    print(json.dumps({"summary": summary, "ui": ui}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
