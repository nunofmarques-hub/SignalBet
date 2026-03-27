import argparse, json
from datetime import datetime, timezone
from pathlib import Path
from phase1_trunk_adapter import resolve_trunk_root, bootstrap_trunk_imports

def build_snapshot(fixtures, league_id, season):
    rows = []
    for row in fixtures[:20]:
        fixture = row.get('fixture', {})
        teams = row.get('teams', {})
        rows.append({'fixture_id': fixture.get('id'),'event_date': fixture.get('date'),'status_short': fixture.get('status', {}).get('short'),'status_long': fixture.get('status', {}).get('long'),'home_team_id': teams.get('home', {}).get('id'),'home_team_name': teams.get('home', {}).get('name'),'away_team_id': teams.get('away', {}).get('id'),'away_team_name': teams.get('away', {}).get('name')})
    return {'snapshot_name':'fixtures_phase1_snapshot','version':'1.0.0','provider':'fixtures_provider.py','service':'get_fixtures_by_league_season()','primary_consumer':'orchestrator','league_id':league_id,'season':season,'fixtures_count':len(rows),'fixtures':rows,'snapshot_status':'fresh'}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trunk-root', default=None)
    parser.add_argument('--league-id', type=int, default=140)
    parser.add_argument('--season', type=int, default=2024)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent.parent
    trunk_root = resolve_trunk_root(args.trunk_root)
    bootstrap_trunk_imports(trunk_root)
    from data_api.services.fixtures_service import get_fixtures_by_league_season
    fixtures = get_fixtures_by_league_season(args.league_id, args.season)
    snapshot_path = base / 'examples' / 'fixtures_phase1_snapshot_generated.json'
    log_path = base / 'logs' / 'phase1_run_log_generated.json'
    fallback_used = False
    final_status = 'green'
    if fixtures:
        snapshot = build_snapshot(fixtures, args.league_id, args.season)
    else:
        final_status = 'degraded_run'
        fallback_used = True
        if snapshot_path.exists():
            snapshot = json.loads(snapshot_path.read_text(encoding='utf-8'))
            snapshot['snapshot_status'] = 'fallback_last_valid'
        else:
            snapshot = {'snapshot_name':'fixtures_phase1_snapshot','version':'1.0.0','provider':'fixtures_provider.py','service':'get_fixtures_by_league_season()','primary_consumer':'orchestrator','league_id':args.league_id,'season':args.season,'fixtures_count':0,'fixtures':[],'snapshot_status':'empty_no_snapshot'}
            final_status = 'hard_fail'
    snapshot_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding='utf-8')
    log = {'timestamp': datetime.now(timezone.utc).isoformat(),'provider':'fixtures_provider.py','fixtures_count': snapshot.get('fixtures_count',0),'snapshot_status': snapshot.get('snapshot_status'),'fallback_used': fallback_used,'final_status': final_status,'trunk_root': str(trunk_root)}
    log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'snapshot': snapshot, 'log': log}, ensure_ascii=False, indent=2))
    if final_status == 'hard_fail':
        raise SystemExit(1)

if __name__ == '__main__':
    main()
