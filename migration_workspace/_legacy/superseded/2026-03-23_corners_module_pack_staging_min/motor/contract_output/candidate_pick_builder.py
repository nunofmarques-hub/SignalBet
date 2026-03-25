from contract_mapper import map_corners_output_to_market_pick
def build_candidate_pick(corners_output, module_version='corners.staging', kickoff_datetime=None, odds=None, edge_raw=None, expiry_context='pre_match_same_day'):
    return map_corners_output_to_market_pick(corners_output, module_version=module_version, kickoff_datetime=kickoff_datetime, odds=odds, edge_raw=edge_raw, module_rank_internal=1, expiry_context=expiry_context)
