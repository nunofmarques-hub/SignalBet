from __future__ import annotations

def run_market_engines(adapted: dict) -> list[dict]:
    fixture_id = adapted["fixture_id"]
    home = adapted["home_team_name"]
    away = adapted["away_team_name"]

    home_stats = adapted["home_team_statistics"]
    away_stats = adapted["away_team_statistics"]

    home_goals_for = float(home_stats.get("goals_for_per_game", 0.0))
    home_goals_against = float(home_stats.get("goals_against_per_game", 0.0))
    home_shots_on_target = float(home_stats.get("shots_on_target_per_game", 0.0))

    away_goals_for = float(away_stats.get("goals_for_per_game", 0.0))
    away_goals_against = float(away_stats.get("goals_against_per_game", 0.0))
    away_shots_on_target = float(away_stats.get("shots_on_target_per_game", 0.0))

    base = {
        "fixture_id": fixture_id,
        "match_label": f"{home} vs {away}",
        "competition": adapted["competition"],
        "kickoff_datetime": adapted["kickoff_datetime"],
    }

    team_over_score = round(
        (home_goals_for * 18) +
        (away_goals_against * 14) +
        (home_shots_on_target * 4),
        1,
    )

    match_over_score = round(
        ((home_goals_for + away_goals_for) * 18) +
        ((home_shots_on_target + away_shots_on_target) * 2),
        1,
    )

    under_score = round(
        (60 - ((home_goals_for + away_goals_for) * 10)) +
        ((2.8 - (home_goals_against + away_goals_against)) * 8),
        1,
    )

    return [
        {
            **base,
            "motor_id": "TEAM_OVER_ENGINE",
            "market_family": "goals",
            "market": "team_goals_over",
            "selection": f"{home} Over 1.5",
            "line": 1.5,
            "score_raw": max(team_over_score, 0),
            "confidence_raw": 4,
            "risk_raw": 2,
            "edge_raw": "6.3%",
            "eligibility": True,
            "main_drivers": ["FDI support", "team attack", "opponent concession"],
            "penalties": ["provider sample odds"],
            "goal_profile": "offensive_directed",
            "market_variant": "TEAM_OVER_15",
        },
        {
            **base,
            "motor_id": "MATCH_OVER_ENGINE",
            "market_family": "goals",
            "market": "match_goals_over",
            "selection": "Over 1.5",
            "line": 1.5,
            "score_raw": max(match_over_score, 0),
            "confidence_raw": 3,
            "risk_raw": 3,
            "edge_raw": "4.8%",
            "eligibility": True,
            "main_drivers": ["global attack", "shots support"],
            "penalties": ["mid-risk balance"],
            "goal_profile": "offensive_global",
            "market_variant": "MATCH_OVER_15",
        },
        {
            **base,
            "motor_id": "MATCH_UNDER_ENGINE",
            "market_family": "goals",
            "market": "match_goals_under",
            "selection": "Under 3.5",
            "line": 3.5,
            "score_raw": max(under_score, 0),
            "confidence_raw": 3,
            "risk_raw": 2,
            "edge_raw": "5.0%",
            "eligibility": True,
            "main_drivers": ["ULI support", "LTR support"],
            "penalties": ["needs stable game state"],
            "goal_profile": "conservative_under",
            "market_variant": "MATCH_UNDER_35",
        },
    ]


def run_v12_engines(data):
    return run_market_engines(data)