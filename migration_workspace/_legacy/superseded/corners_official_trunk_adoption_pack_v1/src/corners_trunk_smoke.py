import argparse, json
from pathlib import Path
from corners_trunk_adapter import resolve_trunk_root, bootstrap_trunk_imports

TARGET_STATS = {
    'Corner Kicks': 'found_corner_kicks',
    'Total Shots': 'found_total_shots',
    'Blocked Shots': 'found_blocked_shots',
    'Ball Possession': 'found_ball_possession',
    'Passes %': 'found_passes_percent',
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trunk-root', default=None)
    args = parser.parse_args()
    trunk_root = resolve_trunk_root(args.trunk_root)
    bootstrap_trunk_imports(trunk_root)

    from data_api.services.fixtures_service import get_fixtures_by_league_season
    from data_api.services.statistics_service import get_fixture_statistics

    league_id = 140
    season = 2024
    fixtures = get_fixtures_by_league_season(league_id, season)

    fixture_id = None
    stats_rows = []
    fixture_row = {}
    for row in fixtures[:10]:
        candidate = row.get('fixture', {}).get('id')
        if not candidate:
            continue
        stats = get_fixture_statistics(candidate, league_id, season)
        if stats:
            fixture_id = candidate
            stats_rows = stats
            fixture_row = row
            break

    found_flags = {v: False for v in TARGET_STATS.values()}
    for team_block in stats_rows:
        for item in team_block.get('statistics', []) or []:
            stat_type = item.get('type')
            if stat_type in TARGET_STATS:
                found_flags[TARGET_STATS[stat_type]] = True

    report = {
        'module': 'Corners',
        'source': 'Data_API_Official_Trunk_v1',
        'trunk_root': str(trunk_root),
        'fixtures_count': len(fixtures),
        'fixture_id': fixture_id,
        'fixture_statistics_found': bool(stats_rows),
        'home_team_id': fixture_row.get('teams', {}).get('home', {}).get('id') if fixture_row else None,
        'away_team_id': fixture_row.get('teams', {}).get('away', {}).get('id') if fixture_row else None,
        'statistics_rows': len(stats_rows),
        **found_flags,
        'result': None,
    }

    ok = report['fixtures_count'] > 0 and report['fixture_statistics_found'] and any(found_flags.values())
    report['result'] = 'green' if ok else 'red'

    out_path = Path(__file__).resolve().parent.parent / 'examples' / 'corners_smoke_output_generated.json'
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if not ok:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
