import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "motor" / "candidate_generation"))
from generate_candidates import generate_all_cases

inp = ROOT / "motor" / "data_handoff" / "sample_cases_from_data_api.json"
cases = generate_all_cases(inp)

for adapted, engine_output, candidate in cases:
    case_id = adapted["case_id"]
    (ROOT / "output_contratual" / f"{case_id}_engine_output.json").write_text(json.dumps(engine_output, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "output_contratual" / f"{case_id}_market_pick.json").write_text(json.dumps(candidate, ensure_ascii=False, indent=2), encoding="utf-8")

summary = {"generated_cases": [adapted["case_id"] for adapted, _, _ in cases], "count": len(cases)}
(ROOT / "output_contratual" / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
