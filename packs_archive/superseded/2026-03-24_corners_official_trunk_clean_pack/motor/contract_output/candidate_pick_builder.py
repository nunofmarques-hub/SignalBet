from contract_mapper import map_corners_output_to_market_pick
def build_candidate_pick(corners_output, module_version='corners.official_trunk_clean', kickoff_datetime=None):
    return map_corners_output_to_market_pick(corners_output, module_version=module_version, kickoff_datetime=kickoff_datetime)
