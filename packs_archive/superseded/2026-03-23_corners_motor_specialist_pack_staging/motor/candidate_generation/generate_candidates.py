import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "motor" / "data_handoff"))
sys.path.append(str(ROOT / "motor" / "engine"))
sys.path.append(str(ROOT / "motor" / "contract_output"))

from data_adapter import adapt_case
from eligibility import evaluate_eligibility
from candidate_selection import build_engine_output
from candidate_pick_builder import build_candidate_pick

def generate_all_cases(input_path):
    payload = json.loads(Path(input_path).read_text(encoding="utf-8"))
    out = []
    for case in payload["cases"]:
        adapted = adapt_case(case)
        eligible, alerts, exclusions = evaluate_eligibility(adapted)
        engine_output = build_engine_output(adapted, eligible, alerts, exclusions)
        candidate = build_candidate_pick(engine_output, kickoff_datetime=adapted.get("kickoff_datetime"))
        out.append((adapted, engine_output, candidate))
    return out
