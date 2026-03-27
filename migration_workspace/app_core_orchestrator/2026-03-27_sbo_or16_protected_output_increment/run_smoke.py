import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
from app_orch.run_output_increment import run
if __name__ == "__main__":
    result = run(out_dir=str(ROOT / "runtime_outputs"))
    p = result["protected"]
    print("output_increment_smoke=OK")
    print(f"readiness_level={p['readiness_level']}")
    print(f"cta_state={p['cta_state']}")
    print(f"source_mode={p['source_mode']}")
    print(f"bridge_status={p['bridge_status']}")
    print(f"baseline_status={p['baseline_status']}")
    print(f"complementary_status={p['complementary_status']}")
    print(f"central_health={p['central_health']}")
