import argparse, json
from pathlib import Path
from cards_trunk_adapter import resolve_trunk_root, bootstrap_trunk_imports

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trunk-root', default=None)
    args = parser.parse_args()
    trunk_root = resolve_trunk_root(args.trunk_root)
    bootstrap_trunk_imports(trunk_root)

    from data_api.services.fixtures_service import get_fixtures_by_league_season
    from data_api.services.events_service import get_fixture_events

    league_id = 140
    season = 2024
    fixtures = get_fixtures_by_league_season(league_id, season)

    fixture_id = None
    events = []
    fixture_row = {}
    for row in fixtures[:10]:
        candidate = row.get('fixture', {}).get('id')
        if not candidate:
            continue
        ev = get_fixture_events(candidate, league_id, season)
        if ev:
            fixture_id = candidate
            events = ev
            fixture_row = row
            break

    card_events = [e for e in events if e.get('type') == 'Card' or 'card' in str(e.get('detail', '')).lower()]
    report = {
        'module': 'Cards',
        'source': 'Data_API_Official_Trunk_v1',
        'trunk_root': str(trunk_root),
        'fixtures_count': len(fixtures),
        'fixture_id': fixture_id,
        'events_found': bool(events),
        'events_count': len(events),
        'card_events_count': len(card_events),
        'home_team_id': fixture_row.get('teams', {}).get('home', {}).get('id') if fixture_row else None,
        'away_team_id': fixture_row.get('teams', {}).get('away', {}).get('id') if fixture_row else None,
        'result': None
    }

    ok = report['fixtures_count'] > 0 and report['events_found']
    report['result'] = 'green' if ok else 'red'

    out_path = Path(__file__).resolve().parent.parent / 'examples' / 'cards_smoke_output_generated.json'
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if not ok:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
