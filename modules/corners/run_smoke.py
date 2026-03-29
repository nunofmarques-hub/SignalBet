import json
from pathlib import Path

p = Path(__file__).parent / "examples" / "corners_shadow_run_readiness_summary.json"
print(p.read_text(encoding="utf-8"))
