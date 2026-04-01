from pathlib import Path
import json
import sys
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from batch_runner import run_batch
batch = json.loads((ROOT / "examples" / "multi_module_batch_inputs" / "batch_input_case_main.json").read_text(encoding="utf-8"))
result = run_batch(batch, selector_run_id="gps_run_smoke", normalization_version="norm.v1.1")
assert result["exported"]["batch_schema_version"] == "bankroll_export_batch.frozen.v3"
assert result["exported"]["shortlist_size"] >= 1
print("SMOKE_OK")
