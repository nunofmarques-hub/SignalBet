from __future__ import annotations

import json
from pathlib import Path

from data_api.services.fixtures_service import get_fixtures_by_league_season
from data_api.services.standings_service import get_standings_snapshot
from data_api.services.statistics_service import (
    get_fixture_statistics,
    get_team_statistics,
)

LEAGUE_ID = 140
SEASON = 2024


def find_fixture_with_statistics(fixtures: list[dict], limit: int = 10) -> tuple[int | None, list[dict]]:
    for row in fixtures[:limit]:
        fixture_id = row.get("fixture", {}).get("id")
        if not fixture_id:
            continue
        stats = get_fixture_statistics(fixture_id, LEAGUE_ID, SEASON)
        if stats:
            return fixture_id, stats
    return None, []


def main() -> None:
    fixtures = get_fixtures_by_league_season(LEAGUE_ID, SEASON)
    standings = get_standings_snapshot(LEAGUE_ID, SEASON)

    fixture_id, fixture_stats = find_fixture_with_statistics(fixtures, limit=10)

    home_team_id = None
    away_team_id = None
    if fixtures:
        first = fixtures[0]
        home_team_id = first.get("teams", {}).get("home", {}).get("id")
        away_team_id = first.get("teams", {}).get("away", {}).get("id")

    home_team_stats = get_team_statistics(home_team_id, LEAGUE_ID, SEASON) if home_team_id else {}
    away_team_stats = get_team_statistics(away_team_id, LEAGUE_ID, SEASON) if away_team_id else {}

    report = {
        "module": "v12",
        "source": "Data_API_Official_Trunk_v1",
        "fixtures_count": len(fixtures),
        "standings_count": len(standings),
        "fixture_statistics_fixture_id": fixture_id,
        "fixture_statistics_found": bool(fixture_stats),
        "home_team_id": home_team_id,
        "away_team_id": away_team_id,
        "home_team_statistics_found": bool(home_team_stats),
        "away_team_statistics_found": bool(away_team_stats),
        "result": None,
    }

    ok = (
        report["fixtures_count"] > 0
        and report["standings_count"] > 0
        and report["fixture_statistics_found"]
        and (report["home_team_statistics_found"] or report["away_team_statistics_found"])
    )
    report["result"] = "green" if ok else "red"

    out_path = Path("smoke_test_v12_result.json")
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))

    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
