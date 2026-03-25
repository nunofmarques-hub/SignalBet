#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, os, sys, time, urllib.request, urllib.parse
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

API_BASE = 'https://v3.football.api-sports.io'
DEFAULT_LEAGUE = 140
DEFAULT_SEASON = 2024
DEFAULT_STATUS = 'FT-AET-PEN'


def load_api_key(root: Path) -> str:
    env_path = root / 'api.env.txt'
    if not env_path.exists():
        raise FileNotFoundError(f'api.env.txt not found at {env_path}')
    for line in env_path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line.startswith('API_KEY='):
            key = line.split('=', 1)[1].strip()
            if key:
                return key
    raise ValueError('API_KEY not found in api.env.txt')


def ensure_dirs(base: Path) -> Dict[str, Path]:
    paths = {
        'catalog': base / 'catalog',
        'raw_fixtures': base / 'raw' / 'fixtures',
        'raw_events': base / 'raw' / 'events',
        'raw_team_stats': base / 'raw' / 'team_statistics',
        'raw_standings': base / 'raw' / 'standings',
        'raw_stats': base / 'raw' / 'statistics',
        'raw_odds': base / 'raw' / 'odds',
        'raw_predictions': base / 'raw' / 'predictions',
        'masters': base / 'masters',
        'logs': base / 'logs',
    }
    for p in paths.values():
        p.mkdir(parents=True, exist_ok=True)
    return paths


def api_get(api_key: str, endpoint: str, params: Dict[str, Any], sleep_s: float = 6.2) -> Dict[str, Any]:
    qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    url = f'{API_BASE}{endpoint}?{qs}' if qs else f'{API_BASE}{endpoint}'
    req = urllib.request.Request(url, headers={'x-apisports-key': api_key})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    time.sleep(sleep_s)
    return data


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8'))


def parse_stat_block(stats_resp: List[Dict[str, Any]]) -> Dict[int, Dict[str, Any]]:
    out = {}
    for team_block in stats_resp:
        team = team_block.get('team', {})
        tid = team.get('id')
        vals = {'team_id': tid, 'team_name': team.get('name')}
        for item in team_block.get('statistics', []) or []:
            t = item.get('type')
            v = item.get('value')
            vals[t] = v
        out[tid] = vals
    return out


def percent_to_float(v: Any) -> Optional[float]:
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace('%', '')
    try:
        return float(s)
    except Exception:
        return None


def detect_first_goal_minute(events: List[Dict[str, Any]]) -> Optional[int]:
    mins = []
    for e in events or []:
        if e.get('type') == 'Goal' and e.get('detail') in ('Normal Goal', 'Penalty', 'Own Goal'):
            m = e.get('time', {}).get('elapsed')
            if isinstance(m, int):
                mins.append(m)
    return min(mins) if mins else None


def derive_response_after_conceding(events: List[Dict[str, Any]], home_id: int, away_id: int) -> Optional[bool]:
    score = {home_id: 0, away_id: 0}
    first_scored_by = None
    for e in sorted(events or [], key=lambda x: (x.get('time', {}).get('elapsed') or 999, x.get('time', {}).get('extra') or 0)):
        if e.get('type') != 'Goal' or e.get('detail') not in ('Normal Goal', 'Penalty', 'Own Goal'):
            continue
        tid = e.get('team', {}).get('id')
        if tid not in score:
            continue
        if first_scored_by is None:
            first_scored_by = tid
        score[tid] += 1
        other = away_id if tid == home_id else home_id
        if first_scored_by == other and score[tid] >= 1:
            return True
    if first_scored_by is None:
        return None
    return False


def discover(args):
    root = Path(args.root).resolve()
    api_key = load_api_key(root)
    season_root = root / 'data_api_football' / f'league_{args.league}' / f'season_{args.season}'
    paths = ensure_dirs(season_root)

    leagues = api_get(api_key, '/leagues', {'id': args.league})
    write_json(paths['catalog'] / 'coverage_registry.json', leagues)

    fixtures = api_get(api_key, '/fixtures', {'league': args.league, 'season': args.season, 'status': args.status})
    write_json(paths['raw_fixtures'] / f'fixtures_league_{args.league}_season_{args.season}.json', fixtures)

    rows = fixtures.get('response', []) or []
    fixture_ids = [r.get('fixture', {}).get('id') for r in rows if r.get('fixture', {}).get('id')]
    write_json(paths['catalog'] / 'fixture_ids.json', {'league': args.league, 'season': args.season, 'status': args.status, 'fixture_ids': fixture_ids})
    print(f'Discovered {len(fixture_ids)} fixtures')


def collect_core(args):
    root = Path(args.root).resolve()
    api_key = load_api_key(root)
    season_root = root / 'data_api_football' / f'league_{args.league}' / f'season_{args.season}'
    paths = ensure_dirs(season_root)
    fixture_ids = read_json(paths['catalog'] / 'fixture_ids.json')['fixture_ids']
    fixtures_payload = read_json(paths['raw_fixtures'] / f'fixtures_league_{args.league}_season_{args.season}.json')
    fixtures_rows = fixtures_payload.get('response', []) or []

    team_ids = set()
    for r in fixtures_rows:
        fx = r.get('fixture', {}).get('id')
        if fx in fixture_ids:
            write_json(paths['raw_fixtures'] / f'fixture_{fx}.json', r)
            for side in ('home', 'away'):
                tid = r.get('teams', {}).get(side, {}).get('id')
                if tid:
                    team_ids.add(tid)

    for fx in fixture_ids:
        out = paths['raw_events'] / f'fixture_{fx}.json'
        if out.exists() and not args.refresh:
            continue
        data = api_get(api_key, '/fixtures/events', {'fixture': fx})
        write_json(out, data)

    standings = api_get(api_key, '/standings', {'league': args.league, 'season': args.season})
    write_json(paths['raw_standings'] / f'standings_league_{args.league}_season_{args.season}.json', standings)

    for tid in sorted(team_ids):
        out = paths['raw_team_stats'] / f'team_{tid}.json'
        if out.exists() and not args.refresh:
            continue
        data = api_get(api_key, '/teams/statistics', {'league': args.league, 'season': args.season, 'team': tid})
        write_json(out, data)
    print(f'Collected core for {len(fixture_ids)} fixtures and {len(team_ids)} teams')


def collect_reinforcement(args):
    root = Path(args.root).resolve()
    api_key = load_api_key(root)
    season_root = root / 'data_api_football' / f'league_{args.league}' / f'season_{args.season}'
    paths = ensure_dirs(season_root)
    fixture_ids = read_json(paths['catalog'] / 'fixture_ids.json')['fixture_ids']
    limit = args.max_items or len(fixture_ids)
    for fx in fixture_ids[:limit]:
        stats_out = paths['raw_stats'] / f'fixture_{fx}.json'
        if (not stats_out.exists()) or args.refresh:
            write_json(stats_out, api_get(api_key, '/fixtures/statistics', {'fixture': fx}))
        if args.with_predictions:
            pred_out = paths['raw_predictions'] / f'fixture_{fx}.json'
            if (not pred_out.exists()) or args.refresh:
                write_json(pred_out, api_get(api_key, '/predictions', {'fixture': fx}))
        if args.with_odds:
            odds_out = paths['raw_odds'] / f'fixture_{fx}.json'
            if (not odds_out.exists()) or args.refresh:
                write_json(odds_out, api_get(api_key, '/odds', {'fixture': fx}))
    print(f'Collected reinforcement for {min(limit, len(fixture_ids))} fixtures')


def build_masters(args):
    root = Path(args.root).resolve()
    season_root = root / 'data_api_football' / f'league_{args.league}' / f'season_{args.season}'
    paths = ensure_dirs(season_root)
    fixtures_payload = read_json(paths['raw_fixtures'] / f'fixtures_league_{args.league}_season_{args.season}.json')
    standings_payload = read_json(paths['raw_standings'] / f'standings_league_{args.league}_season_{args.season}.json')
    standings_index = {}
    try:
        table = standings_payload['response'][0]['league']['standings'][0]
        for row in table:
            standings_index[row['team']['id']] = row
    except Exception:
        pass

    team_profiles = {}
    for p in paths['raw_team_stats'].glob('team_*.json'):
        payload = read_json(p).get('response', {})
        team = payload.get('team', {})
        tid = team.get('id')
        played = (payload.get('fixtures', {}).get('played', {}) or {})
        gf = (payload.get('goals', {}).get('for', {}).get('total', {}) or {})
        ga = (payload.get('goals', {}).get('against', {}).get('total', {}) or {})
        cs = payload.get('clean_sheet', {}) or {}
        fts = payload.get('failed_to_score', {}) or {}
        total_played = played.get('total') or 0
        total_gf = gf.get('total') or 0
        total_ga = ga.get('total') or 0
        total_cs = cs.get('total') or 0
        total_fts = fts.get('total') or 0
        team_profiles[tid] = {
            'team_id': tid,
            'team_name': team.get('name'),
            'form': payload.get('form'),
            'played_total': total_played,
            'goals_for_total': total_gf,
            'goals_against_total': total_ga,
            'clean_sheet_total': total_cs,
            'failed_to_score_total': total_fts,
            'score_rate_1plus': round((total_played - total_fts) / total_played, 4) if total_played else None,
            'concede_rate_1plus': round((total_played - total_cs) / total_played, 4) if total_played else None,
            'clean_sheet_inverse_rate': round((total_played - total_cs) / total_played, 4) if total_played else None,
            'bos_score_lite': round((total_gf / total_played), 4) if total_played else None,
            'bvs_score_lite': round((total_ga / total_played), 4) if total_played else None,
            'ami_score_lite': payload.get('form'),
            'tsi_score_lite': round(1 - abs((total_gf - total_ga) / max(total_played, 1)), 4) if total_played else None,
        }

    match_rows = []
    for r in fixtures_payload.get('response', []) or []:
        fx = r.get('fixture', {}).get('id')
        home = r.get('teams', {}).get('home', {})
        away = r.get('teams', {}).get('away', {})
        home_id, away_id = home.get('id'), away.get('id')
        goals_home = r.get('goals', {}).get('home')
        goals_away = r.get('goals', {}).get('away')
        ht_home = r.get('score', {}).get('halftime', {}).get('home')
        ht_away = r.get('score', {}).get('halftime', {}).get('away')

        events_path = paths['raw_events'] / f'fixture_{fx}.json'
        events = read_json(events_path).get('response', []) if events_path.exists() else []
        first_goal_minute = detect_first_goal_minute(events)
        response_after_conceding = derive_response_after_conceding(events, home_id, away_id)

        stats_path = paths['raw_stats'] / f'fixture_{fx}.json'
        stats_index = {}
        if stats_path.exists():
            stats_index = parse_stat_block(read_json(stats_path).get('response', []))

        home_stats = stats_index.get(home_id, {})
        away_stats = stats_index.get(away_id, {})

        hp = team_profiles.get(home_id, {})
        ap = team_profiles.get(away_id, {})
        row = {
            'fixture_id': fx,
            'date': r.get('fixture', {}).get('date'),
            'status': r.get('fixture', {}).get('status', {}).get('short'),
            'home_team_id': home_id,
            'home_team_name': home.get('name'),
            'away_team_id': away_id,
            'away_team_name': away.get('name'),
            'goals_home': goals_home,
            'goals_away': goals_away,
            'halftime_home': ht_home,
            'halftime_away': ht_away,
            'btts_yes': bool((goals_home or 0) > 0 and (goals_away or 0) > 0),
            'halftime_0_0': bool((ht_home or 0) == 0 and (ht_away or 0) == 0),
            'first_goal_minute': first_goal_minute,
            'goal_until_30': bool(first_goal_minute is not None and first_goal_minute <= 30),
            'response_after_conceding': response_after_conceding,
            'home_rank': (standings_index.get(home_id) or {}).get('rank'),
            'away_rank': (standings_index.get(away_id) or {}).get('rank'),
            'rank_gap_abs': abs(((standings_index.get(home_id) or {}).get('rank') or 0) - ((standings_index.get(away_id) or {}).get('rank') or 0)) or None,
            'home_score_rate_1plus': hp.get('score_rate_1plus'),
            'away_score_rate_1plus': ap.get('score_rate_1plus'),
            'home_concede_rate_1plus': hp.get('concede_rate_1plus'),
            'away_concede_rate_1plus': ap.get('concede_rate_1plus'),
            'home_clean_sheet_inverse_rate': hp.get('clean_sheet_inverse_rate'),
            'away_clean_sheet_inverse_rate': ap.get('clean_sheet_inverse_rate'),
            'bos_score_lite': round(((hp.get('bos_score_lite') or 0) + (ap.get('bos_score_lite') or 0)) / 2, 4) if hp or ap else None,
            'bvs_score_lite': round(((hp.get('bvs_score_lite') or 0) + (ap.get('bvs_score_lite') or 0)) / 2, 4) if hp or ap else None,
            'ami_score_lite': f"{hp.get('ami_score_lite') or ''}|{ap.get('ami_score_lite') or ''}",
            'tsi_score_lite': round(((hp.get('tsi_score_lite') or 0) + (ap.get('tsi_score_lite') or 0)) / 2, 4) if hp or ap else None,
            'home_shots_on_goal': home_stats.get('Shots on Goal'),
            'away_shots_on_goal': away_stats.get('Shots on Goal'),
            'home_total_shots': home_stats.get('Total Shots'),
            'away_total_shots': away_stats.get('Total Shots'),
            'home_ball_possession_pct': percent_to_float(home_stats.get('Ball Possession')),
            'away_ball_possession_pct': percent_to_float(away_stats.get('Ball Possession')),
            'home_passes_pct': percent_to_float(home_stats.get('Passes %')),
            'away_passes_pct': percent_to_float(away_stats.get('Passes %')),
            'xg_gap_proxy_lite': None,
        }
        hsog = row['home_shots_on_goal'] or 0
        asog = row['away_shots_on_goal'] or 0
        hts = row['home_total_shots'] or 0
        ats = row['away_total_shots'] or 0
        row['xg_gap_proxy_lite'] = round(((hsog * 0.6 + hts * 0.4) + (asog * 0.6 + ats * 0.4)) / 2, 4) if (hsog or asog or hts or ats) else None
        match_rows.append(row)

    write_json(paths['masters'] / f'btts_match_master_{args.season}.json', match_rows)
    with (paths['masters'] / f'btts_match_master_{args.season}.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(match_rows[0].keys()) if match_rows else ['fixture_id'])
        writer.writeheader()
        writer.writerows(match_rows)

    overall = list(team_profiles.values())
    write_json(paths['masters'] / f'btts_team_profiles_overall_{args.season}.json', overall)
    contract = {
        'season': args.season,
        'league': args.league,
        'status': args.status,
        'core_endpoints': ['/leagues', '/fixtures', '/fixtures/events', '/teams/statistics', '/standings'],
        'reinforcement_endpoints': ['/fixtures/statistics', '/odds', '/predictions'],
        'outputs': [
            f'btts_match_master_{args.season}.json',
            f'btts_match_master_{args.season}.csv',
            f'btts_team_profiles_overall_{args.season}.json',
        ],
    }
    write_json(paths['masters'] / 'btts_data_contract.json', contract)
    print(f'Built {len(match_rows)} BTTS match rows')


def full_bootstrap(args):
    discover(args)
    collect_core(args)
    if args.with_reinforcement:
        collect_reinforcement(args)
    build_masters(args)


def main():
    parser = argparse.ArgumentParser(description='SignalBet BTTS data collector')
    parser.add_argument('command', choices=['discover', 'collect-core', 'collect-reinforcement', 'build-masters', 'full-bootstrap'])
    parser.add_argument('--root', default='.')
    parser.add_argument('--league', type=int, default=DEFAULT_LEAGUE)
    parser.add_argument('--season', type=int, default=DEFAULT_SEASON)
    parser.add_argument('--status', default=DEFAULT_STATUS)
    parser.add_argument('--max-items', type=int, default=20)
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--with-odds', action='store_true')
    parser.add_argument('--with-predictions', action='store_true')
    parser.add_argument('--with-reinforcement', action='store_true')
    args = parser.parse_args()

    cmd_map = {
        'discover': discover,
        'collect-core': collect_core,
        'collect-reinforcement': collect_reinforcement,
        'build-masters': build_masters,
        'full-bootstrap': full_bootstrap,
    }
    cmd_map[args.command](args)


if __name__ == '__main__':
    main()
