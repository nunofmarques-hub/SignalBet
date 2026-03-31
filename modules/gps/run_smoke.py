from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from export_shortlist_product import export_shortlist_product

inp = json.loads((ROOT / "examples" / "shortlist_product_input_internal_example.json").read_text(encoding="utf-8"))
out = export_shortlist_product(inp)

assert isinstance(out, list)
assert len(out) == 3
assert out[0]["shortlist_level"] == "primary"
assert out[1]["shortlist_level"] == "secondary"
assert out[2]["shortlist_level"] == "watchlist"
print("SMOKE_OK")
