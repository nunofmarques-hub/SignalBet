def _safe_get(d, *path, default=0):
    cur = d
    for key in path:
        if isinstance(cur, dict) and key in cur:
            cur = cur[key]
        else:
            return default
    return cur


def adapt_official_bundle(bundle: dict) -> dict:
    fixture = bundle["fixture"]
    home_name = fixture["teams"]["home"]["name"]
    away_name = fixture["teams"]["away"]["name"]
    home_stats = bundle["home_team_statistics"]
    away_stats = bundle["away_team_statistics"]
    return {
        "fixture_id": fixture["fixture"]["id"],
        "match_label": f"{home_name} vs {away_name}",
        "competition": fixture["league"]["name"],
        "kickoff_datetime": fixture["fixture"]["date"],
        "home_team": {"id": fixture["teams"]["home"]["id"], "name": home_name},
        "away_team": {"id": fixture["teams"]["away"]["id"], "name": away_name},
        "standings_snapshot": bundle["standings_snapshot"],
        "signals": {
            "home_goals_for": _safe_get(home_stats, "goals_for_per_game", default=1.4),
            "away_goals_for": _safe_get(away_stats, "goals_for_per_game", default=1.2),
            "home_goals_against": _safe_get(home_stats, "goals_against_per_game", default=1.2),
            "away_goals_against": _safe_get(away_stats, "goals_against_per_game", default=1.4),
            "home_shots_on_target": _safe_get(home_stats, "shots_on_target_per_game", default=4.7),
            "away_shots_on_target": _safe_get(away_stats, "shots_on_target_per_game", default=4.1),
            "fixture_stats": bundle["fixture_statistics"],
        },
        "provider_name": bundle["provider"],
        "required_objects_used": [
            "fixtures_catalog",
            "standings_snapshot",
            "fixture_statistics",
            "team_statistics",
        ],
    }
