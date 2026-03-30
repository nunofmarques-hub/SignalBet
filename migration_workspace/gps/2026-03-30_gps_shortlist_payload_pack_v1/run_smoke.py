
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from export_shortlist import export_shortlist

inp = json.loads((ROOT / "examples" / "shortlist_input_internal_example.json").read_text(encoding="utf-8"))
out = export_shortlist(inp)

assert isinstance(out, list)
assert len(out) >= 1
assert list(out[0].keys()) == [
    "pick_id",
    "module_name",
    "fixture_id",
    "match_label",
    "market_code",
    "selection_label",
    "rank_position",
    "rationale_short",
]
print("SMOKE_OK")
