from __future__ import annotations

import json
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from core.settings import load_api_config, load_league_map
from models.match import Match
from storage.json_store import data_path, load_json, save_json

FIXTURES_CACHE_FILE = data_path('fixtures_cache.json')

ALLOWED_LEAGUES = {
    ("Germany", "Bundesliga"),
    ("Austria", "Bundesliga"),
    ("Spain", "La Liga"),
    ("France", "Ligue 1"),
    ("England", "Premier League"),
    ("Italy", "Serie A"),
    ("Netherlands", "Eredivisie"),
    ("Portugal", "Primeira Liga"),
    ("Belgium", "Jupiler Pro League"),
    ("Switzerland", "Super League"),
}


def load_fixture_cache() -> dict[str, list[dict[str, Any]]]:
    payload = load_json(FIXTURES_CACHE_FILE, default={})
    return payload if isinstance(payload, dict) else {}


def save_fixture_cache(cache: dict[str, list[dict[str, Any]]]) -> None:
    save_json(FIXTURES_CACHE_FILE, cache)


def _league_key(country: str, league: str) -> str:
    return f'{country}|{league}'


def filter_allowed_leagues(fixtures: list[dict[str, Any]]) -> list[dict[str, Any]]:
    league_map = load_league_map()
    rows: list[dict[str, Any]] = []
    for item in fixtures:
        country = (item.get('league', {}).get('country') or '').strip()
        league = (item.get('league', {}).get('name') or '').strip()
        if (country, league) not in ALLOWED_LEAGUES:
            continue
        home = item.get('teams', {}).get('home', {})
        away = item.get('teams', {}).get('away', {})
        fixture = item.get('fixture', {})
        league_info = league_map.get(_league_key(country, league), {})
        rows.append({
            'fixture_id': fixture.get('id') or 0,
            'date': (fixture.get('date') or '')[:10],
            'league': league,
            'country': country,
            'league_id': league_info.get('league_id'),
            'season': league_info.get('season'),
            'status_short': item.get('fixture', {}).get('status', {}).get('short') or '',
            'home_team': home.get('name') or 'Home',
            'away_team': away.get('name') or 'Away',
            'home_team_id': home.get('id'),
            'away_team_id': away.get('id'),
        })
    return rows


def fetch_api_fixtures(date_str: str) -> tuple[list[dict[str, Any]], str]:
    config = load_api_config()
    api_key = config.get('api_key') or ''
    if not api_key:
        raise RuntimeError('API key em falta. Definir ABC_API_KEY ou data/api_config.json')
    base_url = config.get('base_url') or 'https://v3.football.api-sports.io'
    timeout = int(config.get('request_timeout') or 20)
    url = base_url + '/fixtures?' + urlencode({'date': date_str})
    req = Request(url, headers={
        'x-apisports-key': api_key,
        'User-Agent': 'Mozilla/5.0',
    })
    with urlopen(req, timeout=timeout) as response:
        payload = json.loads(response.read().decode('utf-8'))
    filtered = filter_allowed_leagues(payload.get('response', []))
    return filtered, 'API'


def get_fixtures(date_str: str) -> tuple[list[dict[str, Any]], str]:
    cache = load_fixture_cache()
    try:
        rows, source = fetch_api_fixtures(date_str)
        cache[date_str] = rows
        save_fixture_cache(cache)
        return rows, source
    except Exception:
        return cache.get(date_str, []), 'CACHE'


def build_match_objects(fixtures: list[dict[str, Any]], source: str = 'API') -> list[Match]:
    matches: list[Match] = []
    for item in fixtures:
        matches.append(Match(
            fixture_id=int(item.get('fixture_id') or 0),
            date=item.get('date') or '',
            country=item.get('country') or '',
            league=item.get('league') or '',
            league_id=item.get('league_id'),
            season=item.get('season'),
            status_short=item.get('status_short') or '',
            home_team=item.get('home_team') or '',
            away_team=item.get('away_team') or '',
            home_team_id=item.get('home_team_id'),
            away_team_id=item.get('away_team_id'),
            source=source,
        ))
    return matches
