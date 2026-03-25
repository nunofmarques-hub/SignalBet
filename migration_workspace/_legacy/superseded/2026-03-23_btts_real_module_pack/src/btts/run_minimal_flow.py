from __future__ import annotations
import json
from pathlib import Path
from .loaders import load_match_master, load_team_profiles
from .engine import BTTSEngine
from .exporter import to_market_pick_v1_1


def main() -> None:
    root = Path(__file__).resolve().parent
    match_master = load_match_master(root / 'examples' / 'input' / 'btts_match_master_2024.json')
    profiles = load_team_profiles(root / 'examples' / 'input' / 'btts_team_profiles_overall_2024.json')
    engine = BTTSEngine()

    match = match_master[0]
    home = profiles[match.home_team_id]
    away = profiles[match.away_team_id]
    result = engine.evaluate(match, home, away)
    payload = to_market_pick_v1_1(result, match, odds=1.80)

    out = root / 'examples' / 'output' / 'example_market_pick.json'
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Generated: {out}')
    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
