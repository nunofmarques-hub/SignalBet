import argparse, json
from pathlib import Path
from v12_trunk_adapter import resolve_trunk_root, bootstrap_trunk_imports

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trunk-root", default=None)
    args = parser.parse_args()

    trunk_root = resolve_trunk_root(args.trunk_root)
    bootstrap_trunk_imports(trunk_root)

    from data_api.services.fixtures_service import get_fixtures_by_league_season
    from data_api.services.standings_service import get_standings_snapshot
    from data_api.services.statistics_service import get_fixture_statistics, get_team_statistics

    league_id = 140
    season = 2024
    fixtures = get_fixtures_by_league_season(league_id, season)
    standings = get_standings_snapshot(league_id, season)

    fixture_id = None
    fixture_stats = []
    fixture_row = {}
    for row in fixtures[:10]:
        candidate = row.get("fixture", {}).get("id")
        if not candidate:
            continue
        stats = get_fixture_statistics(candidate, league_id, season)
        if stats:
            fixture_id = candidate
            fixture_stats = stats
            fixture_row = row
            break

    home_team_id = fixture_row.get("teams", {}).get("home", {}).get("id") if fixture_row else None
    away_team_id = fixture_row.get("teams", {}).get("away", {}).get("id") if fixture_row else None
    home_team_stats = get_team_statistics(home_team_id, league_id, season) if home_team_id else {}
    away_team_stats = get_team_statistics(away_team_id, league_id, season) if away_team_id else {}

    report = {
        "module": "v12",
        "source": "Data_API_Official_Trunk_v1",
        "trunk_root": str(trunk_root),
        "fixtures_count": len(fixtures),
        "standings_count": len(standings),
        "fixture_id": fixture_id,
        "fixture_statistics_found": bool(fixture_stats),
        "home_team_id": home_team_id,
        "away_team_id": away_team_id,
        "home_team_statistics_found": bool(home_team_stats),
        "away_team_statistics_found": bool(away_team_stats),
        "result": None
    }

    ok = (
        report["fixtures_count"] > 0 and
        report["standings_count"] > 0 and
        report["fixture_statistics_found"] and
        (report["home_team_statistics_found"] or report["away_team_statistics_found"])
    )
    report["result"] = "green" if ok else "red"

    out_path = Path(__file__).resolve().parent.parent / "examples" / "v12_smoke_output_generated.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if not ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
