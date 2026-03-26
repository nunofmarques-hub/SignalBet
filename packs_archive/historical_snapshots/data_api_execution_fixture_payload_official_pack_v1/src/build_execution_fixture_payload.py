import argparse, json
from pathlib import Path
from trunk_fixture_payload_adapter import resolve_trunk_root, bootstrap_trunk_imports

def map_fixture_to_execution_payload(row, league_id, season):
    fixture = row.get('fixture', {})
    teams = row.get('teams', {})
    goals = row.get('goals', {})
    score = row.get('score', {})
    fixture_id = fixture.get('id')
    home_team_id = teams.get('home', {}).get('id')
    away_team_id = teams.get('away', {}).get('id')
    home_goals = goals.get('home')
    away_goals = goals.get('away')
    winner_team_id = None
    if isinstance(home_goals, int) and isinstance(away_goals, int):
        if home_goals > away_goals: winner_team_id = home_team_id
        elif away_goals > home_goals: winner_team_id = away_team_id
    status_short = fixture.get('status', {}).get('short')
    return {
        'payload_name': 'execution_fixture_payload',
        'version': '1.0.0',
        'fixture_id': fixture_id,
        'fixture_ref': f'league_{league_id}_season_{season}_fixture_{fixture_id}',
        'league_id': league_id,
        'season': season,
        'event_date': fixture.get('date'),
        'status_short': status_short,
        'status_long': fixture.get('status', {}).get('long'),
        'is_finished': status_short in ('FT','AET','PEN'),
        'home_team_id': home_team_id,
        'home_team_name': teams.get('home', {}).get('name'),
        'away_team_id': away_team_id,
        'away_team_name': teams.get('away', {}).get('name'),
        'home_goals': home_goals,
        'away_goals': away_goals,
        'score_fulltime_home': score.get('fulltime', {}).get('home'),
        'score_fulltime_away': score.get('fulltime', {}).get('away'),
        'score_halftime_home': score.get('halftime', {}).get('home'),
        'score_halftime_away': score.get('halftime', {}).get('away'),
        'settlement_context': {
            'winner_team_id': winner_team_id,
            'is_draw': home_goals == away_goals if isinstance(home_goals,int) and isinstance(away_goals,int) else None,
            'total_goals': (home_goals + away_goals) if isinstance(home_goals,int) and isinstance(away_goals,int) else None,
            'both_teams_scored': (home_goals > 0 and away_goals > 0) if isinstance(home_goals,int) and isinstance(away_goals,int) else None,
            'went_extra_time': status_short == 'AET',
            'went_penalties': status_short == 'PEN'
        },
        'source': {
            'provider_name': 'fixtures_provider.py',
            'service_name': 'get_fixtures_by_league_season()',
            'provider_object': 'fixtures_catalog',
            'official_path': f'data_api/storage/raw/league_{league_id}/season_{season}/catalog/fixtures_catalog_status_FT_AET_PEN.json'
        }
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trunk-root', default=None)
    parser.add_argument('--league-id', type=int, default=140)
    parser.add_argument('--season', type=int, default=2024)
    args = parser.parse_args()
    trunk_root = resolve_trunk_root(args.trunk_root)
    bootstrap_trunk_imports(trunk_root)
    from data_api.services.fixtures_service import get_fixtures_by_league_season
    fixtures = get_fixtures_by_league_season(args.league_id, args.season)
    if not fixtures:
        raise SystemExit('Nao encontrei fixtures no tronco oficial.')
    chosen = None
    for row in fixtures:
        short = row.get('fixture', {}).get('status', {}).get('short')
        if short in ('FT','AET','PEN'):
            chosen = row
            break
    if chosen is None:
        chosen = fixtures[0]
    payload = map_fixture_to_execution_payload(chosen, args.league_id, args.season)
    payload['trunk_root'] = str(trunk_root)
    out_path = Path(__file__).resolve().parent.parent / 'examples' / 'execution_fixture_payload_generated.json'
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(payload, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
