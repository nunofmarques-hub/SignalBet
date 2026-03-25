import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / 'motor' / 'data_handoff'))
sys.path.append(str(ROOT / 'motor' / 'engine'))
sys.path.append(str(ROOT / 'motor' / 'contract_output'))
from data_adapter import adapt_from_official_trunk
from core import eval_case
from candidate_pick_builder import build_candidate_pick

def generate_all_cases(fixtures_path, stats_path, contexts_path):
    fixtures=json.loads(Path(fixtures_path).read_text(encoding='utf-8'))
    stats=json.loads(Path(stats_path).read_text(encoding='utf-8'))
    contexts=json.loads(Path(contexts_path).read_text(encoding='utf-8'))
    out=[]
    for fixture in fixtures:
        fid=str(fixture['fixture']['id'])
        adapted=adapt_from_official_trunk(fixture, stats[fid], contexts[fid])
        engine_output=eval_case(adapted)
        candidate=build_candidate_pick(engine_output, kickoff_datetime=adapted.get('kickoff_datetime'))
        out.append((adapted, engine_output, candidate))
    return out
