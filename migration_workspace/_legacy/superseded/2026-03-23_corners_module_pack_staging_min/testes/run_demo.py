import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / 'motor' / 'candidate_generation'))
from generate_candidates import generate_from_file
engine_output, candidate = generate_from_file(ROOT / 'motor' / 'data_handoff' / 'input_contract_corners.json')
Path(ROOT / 'output_contratual' / 'example_engine_output.json').write_text(json.dumps(engine_output, ensure_ascii=False, indent=2), encoding='utf-8')
Path(ROOT / 'output_contratual' / 'example_market_pick.json').write_text(json.dumps(candidate, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(candidate, ensure_ascii=False, indent=2))
