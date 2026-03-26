import json
from pathlib import Path
from corners.data_handoff.data_adapter import adapt_from_trunk
from corners.engine.core import eval_case
from corners.contract_output.contract_mapper import map_corners_output_to_market_pick

def generate_all_cases(fixtures_path, stats_path, contexts_path):
    fixtures = json.loads(Path(fixtures_path).read_text(encoding="utf-8"))
    stats = json.loads(Path(stats_path).read_text(encoding="utf-8"))
    contexts = json.loads(Path(contexts_path).read_text(encoding="utf-8"))
    out = []
    for fixture in fixtures:
        fid = str(fixture["fixture"]["id"])
        adapted = adapt_from_trunk(fixture, stats[fid], contexts[fid])
        engine_output = eval_case(adapted)
        candidate = map_corners_output_to_market_pick(engine_output)
        out.append((adapted, engine_output, candidate))
    return out
