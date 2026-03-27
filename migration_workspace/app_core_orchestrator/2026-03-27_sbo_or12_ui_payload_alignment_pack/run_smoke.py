import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from app_orch.run_baseline_control import run

if __name__ == "__main__":
    result = run(out_dir=str(ROOT / "runtime_outputs"))
    print("baseline_control_smoke=OK")
    print(f"readiness_level={result['summary']['readiness_level']}")
    print(f"cta_state={result['summary']['cta_state']}")
    print(f"source_mode={result['summary']['source_mode']}")
    print(f"observed_mode={result['button_payload']['observed_mode']}")
    print(f"bridge_status={result['button_payload']['bridge_status']}")
