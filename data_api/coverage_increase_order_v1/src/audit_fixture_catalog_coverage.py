from __future__ import annotations
import argparse, json
from pathlib import Path

def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def fixture_ids_from_folder(folder: Path):
    ids = set()
    if folder.exists():
        for p in folder.glob('fixture_*.json'):
            try:
                ids.add(int(p.stem.split('_')[1]))
            except Exception:
                pass
    return ids

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--trunk-root', required=True)
    ap.add_argument('--league-id', type=int, default=140)
    ap.add_argument('--season', type=int, default=2024)
    ap.add_argument('--status', default='FT-AET-PEN')
    args = ap.parse_args()

    root = Path(args.trunk_root)
    season_root = root / 'data_api' / 'storage' / 'raw' / f'league_{args.league_id}' / f'season_{args.season}'
    catalog_path = season_root / 'catalog' / f'fixtures_catalog_status_{args.status.replace('-', '_')}.json'
    fixture_ids_path = season_root / 'catalog' / 'fixture_ids.json'
    events_root = season_root / 'events'
    stats_root = season_root / 'statistics'

    report = {
        'league_id': args.league_id,
        'season': args.season,
        'status': args.status,
        'season_root': str(season_root),
        'catalog_exists': catalog_path.exists(),
        'fixture_ids_exists': fixture_ids_path.exists(),
    }

    catalog_ids = []
    if catalog_path.exists():
        payload = read_json(catalog_path)
        for item in payload.get('response', []) or []:
            fx = item.get('fixture', {})
            fid = fx.get('id')
            if fid is not None:
                catalog_ids.append(int(fid))
    expected_ids = []
    if fixture_ids_path.exists():
        payload = read_json(fixture_ids_path)
        expected_ids = [int(x) for x in payload.get('fixture_ids', [])]

    event_ids = sorted(fixture_ids_from_folder(events_root))
    stat_ids = sorted(fixture_ids_from_folder(stats_root))

    expected = set(expected_ids)
    catalog = set(catalog_ids)
    events = set(event_ids)
    stats = set(stat_ids)

    report.update({
        'expected_fixture_ids': sorted(expected),
        'catalog_fixture_ids': sorted(catalog),
        'events_fixture_ids': sorted(events),
        'statistics_fixture_ids': sorted(stats),
        'counts': {
            'expected': len(expected),
            'catalog': len(catalog),
            'events': len(events),
            'statistics': len(stats),
        },
        'missing_from_catalog': sorted(expected - catalog),
        'expected_missing_from_storage': sorted(expected - (events | stats | catalog)),
        'present_in_storage_not_expected': sorted((events | stats | catalog) - expected),
        'coverage_blocker': 'catalog_too_thin' if len(catalog) <= 1 else 'none',
        'next_action': 'backfill_missing_fixture_metadata_and_regenerate_catalog' if len(catalog) <= 1 else 'rerun_calibration',
    })

    out = root / 'coverage_audit_report.json'
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(f'\n[OK] coverage audit report written to: {out}')

if __name__ == '__main__':
    main()
