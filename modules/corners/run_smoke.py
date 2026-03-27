from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
summary = json.loads((ROOT / "examples" / "summary.json").read_text(encoding="utf-8"))
print(json.dumps(summary, ensure_ascii=False, indent=2))
