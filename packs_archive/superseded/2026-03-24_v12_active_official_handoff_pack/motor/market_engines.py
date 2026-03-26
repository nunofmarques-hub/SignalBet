def run_market_engines(adapted: dict) -> list[dict]:
    s = adapted["signals"]
    home = adapted["home_team"]["name"]
    fixture_id = adapted["fixture_id"]
    base = {
        "fixture_id": fixture_id,
        "match_label": adapted["match_label"],
        "competition": adapted["competition"],
        "kickoff_datetime": adapted["kickoff_datetime"],
    }
    team_over_score = round((s["home_goals_for"]*18)+(s["away_goals_against"]*14)+(s["home_shots_on_target"]*4),1)
    match_over_score = round(((s["home_goals_for"]+s["away_goals_for"])*18)+((s["home_shots_on_target"]+s["away_shots_on_target"])*2),1)
    under_score = round((60-((s["home_goals_for"]+s["away_goals_for"])*10))+((2.8-(s["home_goals_against"]+s["away_goals_against"]))*8),1)
    return [
        {**base, "motor_id": "TEAM_OVER_ENGINE", "market_family": "goals", "market": "team_goals_over", "selection": f"{home} Over 1.5", "line": 1.5, "score_raw": max(team_over_score,0), "confidence_raw": 4, "risk_raw": 2, "edge_raw": "6.3%", "eligibility": True, "main_drivers": ["FDI support", "team attack", "opponent concession"], "penalties": ["provider sample odds"], "goal_profile": "offensive_directed", "market_variant": "TEAM_OVER_15"},
        {**base, "motor_id": "MATCH_OVER_ENGINE", "market_family": "goals", "market": "match_goals_over", "selection": "Over 1.5", "line": 1.5, "score_raw": max(match_over_score,0), "confidence_raw": 3, "risk_raw": 3, "edge_raw": "4.8%", "eligibility": True, "main_drivers": ["global attack", "shots support"], "penalties": ["mid-risk balance"], "goal_profile": "offensive_global", "market_variant": "MATCH_OVER_15"},
        {**base, "motor_id": "MATCH_UNDER_ENGINE", "market_family": "goals", "market": "match_goals_under", "selection": "Under 3.5", "line": 3.5, "score_raw": max(under_score,0), "confidence_raw": 3, "risk_raw": 2, "edge_raw": "5.0%", "eligibility": True, "main_drivers": ["ULI support", "LTR support"], "penalties": ["needs stable game state"], "goal_profile": "conservative_under", "market_variant": "MATCH_UNDER_35"},
    ]
