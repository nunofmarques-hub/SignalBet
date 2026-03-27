import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
from app_orch.run_baseline_control import run
if __name__ == "__main__":
    result = run(out_dir=str(ROOT / "runtime_outputs"))
    print("runtime_snapshot_ok=1")
    print(result["runtime_snapshot"])
