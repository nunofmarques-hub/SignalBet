#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

STAT_KEYS = {
    "Corner Kicks": "corner_kicks",
    "Total Shots": "total_shots",
    "Blocked Shots": "blocked_shots",
    "Ball Possession": "ball_possession_pct",
    "Passes %": "passes_pct",
}


def parse_number(value: Any) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text:
        return None
    if text.endswith('%'):
        text = text[:-1].strip()
    text = text.replace(',', '.')
    try:
        return float(text)
    except ValueError:
        return None


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8'))


def extract_fixture_id(path: Path, payload: Dict[str, Any]) -> Optional[int]:
    match = re.search(r'fixture_(\d+)\.json$', path.name)
    if match:
        return int(match.group(1))
    params = payload.get('parameters', {}) if isinstance(payload, dict) else {}
    fixture = params.get('fixture')
    if fixture is None:
        return None
    try:
        return int(str(fixture))
    except ValueError:
        return None


def extract_team_stats(team_block: Dict[str, Any]) -> Dict[str, Optional[float]]:
    out = {v: None for v in STAT_KEYS.values()}
    for stat in team_block.get('statistics', []):
        stat_type = stat.get('type')
        if stat_type in STAT_KEYS:
            out[STAT_KEYS[stat_type]] = parse_number(stat.get('value'))
    return out


def build_master_rows(stats_dir: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for path in sorted(stats_dir.glob('fixture_*.json')):
        payload = read_json(path)
        fixture_id = extract_fixture_id(path, payload)
        if fixture_id is None:
            continue

        blocks = payload.get('response', [])
        if len(blocks) < 2:
            continue

        home_block, away_block = blocks[0], blocks[1]
        home = extract_team_stats(home_block)
        away = extract_team_stats(away_block)

        row = {
            'fixture_id': fixture_id,
            'home_team_id': (home_block.get('team') or {}).get('id'),
            'home_team_name': (home_block.get('team') or {}).get('name'),
            'away_team_id': (away_block.get('team') or {}).get('id'),
            'away_team_name': (away_block.get('team') or {}).get('name'),
            'home_corner_kicks': home['corner_kicks'],
            'away_corner_kicks': away['corner_kicks'],
            'home_total_shots': home['total_shots'],
            'away_total_shots': away['total_shots'],
            'home_blocked_shots': home['blocked_shots'],
            'away_blocked_shots': away['blocked_shots'],
            'home_ball_possession_pct': home['ball_possession_pct'],
            'away_ball_possession_pct': away['ball_possession_pct'],
            'home_passes_pct': home['passes_pct'],
            'away_passes_pct': away['passes_pct'],
        }
        rows.append(row)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description='Build true corners_master_2024.json from raw/stats/fixture_*.json')
    parser.add_argument('--root', default='.', help='Project root')
    parser.add_argument('--league', type=int, default=140)
    parser.add_argument('--season', type=int, default=2024)
    parser.add_argument('--out-name', default='corners_master_2024.json')
    args = parser.parse_args()

    root = Path(args.root).resolve()
    base = root / 'data_api_football' / f'league_{args.league}' / f'season_{args.season}'
    stats_dir = base / 'raw' / 'stats'
    masters_dir = base / 'masters'
    logs_dir = base / 'logs'
    masters_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)

    if not stats_dir.exists():
        raise SystemExit(f'Não existe diretório de stats: {stats_dir}')

    rows = build_master_rows(stats_dir)
    out_path = masters_dir / args.out_name
    out_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding='utf-8')

    summary = {
        'stats_dir': str(stats_dir),
        'rows': len(rows),
        'output': str(out_path),
    }
    (logs_dir / 'build_true_corners_master_2024_summary.json').write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8'
    )

    print(f'[OK] rows={len(rows)}')
    print(out_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
