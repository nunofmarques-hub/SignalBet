import argparse, json
from datetime import datetime, timezone
from pathlib import Path
from calibration_trunk_adapter import resolve_trunk_root, bootstrap_trunk_imports

def build_snapshot(fixtures, league_id, season, limit=5):
    rows = []
    for row in fixtures[:limit]:
        fixture = row.get('fixture', {})
        teams = row.get('teams', {})
        rows.append({
            'fixture_id': fixture.get('id'),
            'event_date': fixture.get('date'),
            'status_short': fixture.get('status', {}).get('short'),
            'status_long': fixture.get('status', {}).get('long'),
            'home_team_id': teams.get('home', {}).get('id'),
            'home_team_name': teams.get('home', {}).get('name'),
            'away_team_id': teams.get('away', {}).get('id'),
            'away_team_name': teams.get('away', {}).get('name'),
        })
    return {'snapshot_name':'fixtures_calibration_snapshot','version':'1.0.0','provider':'fixtures_provider.py','service':'get_fixtures_by_league_season()','primary_consumer':'orchestrator','league_id':league_id,'season':season,'fixtures_count':len(rows),'fixtures':rows,'snapshot_status':'fresh'}

def same_shape(a, b):
    if not a or not b:
        return False
    if sorted(a.keys()) != sorted(b.keys()):
        return False
    a_rows = a.get('fixtures', [])
    b_rows = b.get('fixtures', [])
    if not a_rows or not b_rows:
        return False
    return sorted(a_rows[0].keys()) == sorted(b_rows[0].keys())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trunk-root', default=None)
    parser.add_argument('--league-id', type=int, default=140)
    parser.add_argument('--season', type=int, default=2024)
    parser.add_argument('--runs', type=int, default=3)
    parser.add_argument('--limit', type=int, default=5)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent.parent
    trunk_root = resolve_trunk_root(args.trunk_root)
    bootstrap_trunk_imports(trunk_root)
    from data_api.services.fixtures_service import get_fixtures_by_league_season
    snapshots = []
    run_logs = []
    green = degraded = hard_fail = 0
    for idx in range(1, args.runs + 1):
        fixtures = get_fixtures_by_league_season(args.league_id, args.season)
        status = 'green'
        fallback_used = False
        if fixtures:
            snapshot = build_snapshot(fixtures, args.league_id, args.season, limit=args.limit)
        else:
            if snapshots:
                snapshot = dict(snapshots[-1])
                snapshot['snapshot_status'] = 'fallback_last_valid'
                status = 'degraded_run'
                fallback_used = True
            else:
                snapshot = {'snapshot_name':'fixtures_calibration_snapshot','version':'1.0.0','provider':'fixtures_provider.py','service':'get_fixtures_by_league_season()','primary_consumer':'orchestrator','league_id':args.league_id,'season':args.season,'fixtures_count':0,'fixtures':[],'snapshot_status':'empty_no_snapshot'}
                status = 'hard_fail'
        if status == 'green': green += 1
        elif status == 'degraded_run': degraded += 1
        else: hard_fail += 1
        snapshots.append(snapshot)
        run_logs.append({'run_index': idx,'timestamp': datetime.now(timezone.utc).isoformat(),'provider':'fixtures_provider.py','fixtures_count': snapshot.get('fixtures_count',0),'snapshot_status': snapshot.get('snapshot_status'),'fallback_used': fallback_used,'final_status': status,'trunk_root': str(trunk_root)})
    latest_snapshot = snapshots[-1]
    shapes_ok = True
    for i in range(1, len(snapshots)):
        if not same_shape(snapshots[i-1], snapshots[i]):
            shapes_ok = False
            break
    counts = [s.get('fixtures_count', 0) for s in snapshots]
    summary = {'phase':'Real Data Calibration & Reliability Phase','runs_attempted': args.runs,'runs_green': green,'runs_degraded': degraded,'runs_hard_fail': hard_fail,'fixtures_count_min': min(counts) if counts else 0,'fixtures_count_max': max(counts) if counts else 0,'snapshot_shape_consistent': shapes_ok,'orchestrator_consumer_status': 'stable' if green > 0 and hard_fail == 0 else 'unstable','result': 'green' if green > 0 and hard_fail == 0 and latest_snapshot.get('fixtures_count',0) > 1 and shapes_ok else 'red'}
    (base / 'examples' / 'calibration_snapshot_generated.json').write_text(json.dumps(latest_snapshot, ensure_ascii=False, indent=2), encoding='utf-8')
    (base / 'logs' / 'calibration_run_log_generated.json').write_text(json.dumps(run_logs, ensure_ascii=False, indent=2), encoding='utf-8')
    (base / 'logs' / 'calibration_summary_generated.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'latest_snapshot': latest_snapshot, 'run_logs': run_logs, 'summary': summary}, ensure_ascii=False, indent=2))
    if summary['result'] != 'green':
        raise SystemExit(1)

if __name__ == '__main__':
    main()
