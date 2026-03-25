from contract_mapper import map_corners_output_to_market_pick

def infer_internal_rank(score):
    if score >= 86: return 1
    if score >= 72: return 2
    if score >= 60: return 3
    if score >= 50: return 4
    return 5

def build_candidate_pick(corners_output, module_version="corners.staging_plus", kickoff_datetime=None, odds=None, edge_raw=None, expiry_context="pre_match_same_day"):
    return map_corners_output_to_market_pick(corners_output, module_version=module_version, kickoff_datetime=kickoff_datetime, odds=odds, edge_raw=edge_raw, module_rank_internal=infer_internal_rank(float(corners_output.get("score",0.0))), expiry_context=expiry_context)
