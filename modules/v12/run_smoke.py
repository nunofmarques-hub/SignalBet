from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
latest_path = base / "latest.json"
examples_path = base / "examples" / "game_card_v12_examples.json"

errors = []

if not latest_path.exists():
    errors.append("missing latest.json")
else:
    latest = json.loads(latest_path.read_text(encoding="utf-8"))
    if latest.get("module_id") != "v12":
        errors.append("latest.json module_id != v12")
    if latest.get("status") != "PASS":
        errors.append("latest.json status != PASS")

if not examples_path.exists():
    errors.append("missing game_card_v12_examples.json")

try:
    subprocess.run([sys.executable, str(base / "motor" / "export_game_cards.py")], check=True)
except subprocess.CalledProcessError:
    errors.append("export_game_cards.py failed")

if errors:
    print("run_smoke = FAIL")
    for e in errors:
        print(f"- {e}")
    raise SystemExit(1)

print("run_smoke = OK")
print("module = v12")
print("line = clean full replacement")
