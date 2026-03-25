import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / 'motor' / 'data_handoff'))
sys.path.append(str(ROOT / 'motor' / 'engine'))
sys.path.append(str(ROOT / 'motor' / 'contract_output'))
from data_adapter import adapt_data_layer_input
from corners_engine_stub import run_corners_engine
from candidate_pick_builder import build_candidate_pick
def generate_from_file(input_path):
    raw = json.loads(Path(input_path).read_text(encoding='utf-8'))
    adapted = adapt_data_layer_input(raw)
    engine_output = run_corners_engine(adapted)
    candidate = build_candidate_pick(engine_output, kickoff_datetime=adapted.get('kickoff_datetime'))
    return engine_output, candidate
