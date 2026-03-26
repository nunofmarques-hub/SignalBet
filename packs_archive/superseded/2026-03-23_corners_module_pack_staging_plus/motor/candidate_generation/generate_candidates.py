import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "motor" / "data_handoff"))
sys.path.append(str(ROOT / "motor" / "engine"))
sys.path.append(str(ROOT / "motor" / "contract_output"))

from data_adapter import adapt_data_layer_input
from eligibility import evaluate_eligibility
from candidate_selection import build_engine_output
from candidate_pick_builder import build_candidate_pick

def generate_from_file(input_path):
    raw = json.loads(Path(input_path).read_text(encoding="utf-8"))
    adapted = adapt_data_layer_input(raw)
    eligible, eligibility_alerts = evaluate_eligibility(adapted)
    engine_output = build_engine_output(adapted, eligible, eligibility_alerts)
    candidate = build_candidate_pick(engine_output, kickoff_datetime=adapted.get("kickoff_datetime"))
    return adapted, engine_output, candidate
