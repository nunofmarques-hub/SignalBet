def adapt_case(raw_case):
    return {
        "case_id": raw_case["case_id"],
        "fixture_id": raw_case["fixture_context"]["fixture_id"],
        "competition": raw_case["fixture_context"]["competition"],
        "season": raw_case["fixture_context"]["season"],
        "kickoff_datetime": raw_case["fixture_context"]["kickoff_datetime"],
        "competitive_state": raw_case["fixture_context"]["competitive_state"],
        "home_team_name": raw_case["fixture_context"]["home_team"]["name"],
        "away_team_name": raw_case["fixture_context"]["away_team"]["name"],
        "home_role": raw_case["fixture_context"]["home_team"]["role"],
        "away_role": raw_case["fixture_context"]["away_team"]["role"],
        "home": raw_case["home_team_window"],
        "away": raw_case["away_team_window"],
        "context": raw_case["match_context"],
    }
