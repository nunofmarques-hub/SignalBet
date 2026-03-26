from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "motor" / "candidate_generation"))

from generate_candidates import generate_from_file

inp = ROOT / "motor" / "data_handoff" / "sample_input_from_data_layer_real.json"
adapted, engine_output, candidate = generate_from_file(inp)

(ROOT / "output_contratual" / "example_engine_output.json").write_text(json.dumps(engine_output, ensure_ascii=False, indent=2), encoding="utf-8")
(ROOT / "output_contratual" / "example_market_pick.json").write_text(json.dumps(candidate, ensure_ascii=False, indent=2), encoding="utf-8")

print("Engine output gravado em:", ROOT / "output_contratual" / "example_engine_output.json")
print("Candidate pick gravada em:", ROOT / "output_contratual" / "example_market_pick.json")
print(json.dumps(candidate, ensure_ascii=False, indent=2))
