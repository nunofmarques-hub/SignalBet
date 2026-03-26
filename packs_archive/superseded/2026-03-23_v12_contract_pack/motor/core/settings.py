from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from storage.json_store import data_path, load_json

API_CONFIG_FILE = data_path('api_config.json')
LEAGUE_MAP_FILE = data_path('league_map.json')
TEAM_RATINGS_FILE = data_path('team_ratings.json')
MARKET_ODDS_FILE = data_path('market_odds.json')

DEFAULT_API_CONFIG: dict[str, Any] = {
    "base_url": "https://v3.football.api-sports.io",
    "api_key": "",
    "odds_endpoint_template": "",
    "odds_enabled": False,
    "request_timeout": 20,
}

DEFAULT_LEAGUE_MAP: dict[str, dict[str, Any]] = {
    "England|Premier League": {"league_id": 39, "season": 2025},
    "Spain|La Liga": {"league_id": 140, "season": 2025},
    "Italy|Serie A": {"league_id": 135, "season": 2025},
    "Germany|Bundesliga": {"league_id": 78, "season": 2025},
    "France|Ligue 1": {"league_id": 61, "season": 2025},
    "Portugal|Primeira Liga": {"league_id": 94, "season": 2025},
    "Netherlands|Eredivisie": {"league_id": 88, "season": 2025},
    "Belgium|Jupiler Pro League": {"league_id": 144, "season": 2025},
    "Switzerland|Super League": {"league_id": 207, "season": 2025},
    "Austria|Bundesliga": {"league_id": 218, "season": 2025},
}

ENV_CANDIDATES = [
    Path('api.env.txt'),
    Path('data/api.env.txt'),
    Path('.env'),
    Path('data/.env'),
]

DEFAULT_TEAM_RATINGS: dict[str, float] = {
    "napoli": 7.9,
    "inter": 8.2,
    "milan": 7.8,
    "juventus": 7.7,
    "benfica": 8.1,
    "porto": 7.8,
    "sporting cp": 8.0,
    "sporting": 8.0,
    "manchester city": 9.0,
    "arsenal": 8.5,
    "liverpool": 8.6,
    "chelsea": 7.4,
    "manchester united": 7.3,
    "real madrid": 8.9,
    "barcelona": 8.6,
    "atletico madrid": 8.0,
    "bayern munich": 9.1,
    "borussia dortmund": 8.0,
    "rb leipzig": 8.1,
    "psg": 8.8,
    "marseille": 7.4,
    "monaco": 7.6,
}




def _load_env_file_key() -> str:
    for candidate in ENV_CANDIDATES:
        try:
            if not candidate.exists():
                continue
            for raw in candidate.read_text(encoding='utf-8').splitlines():
                line = raw.strip()
                if not line or line.startswith('#') or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key in {'API_KEY', 'ABC_API_KEY', 'API_FOOTBALL_KEY'} and value:
                    return value
        except Exception:
            continue
    return ''

def _merge_dict(default: dict[str, Any], loaded: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(loaded, dict):
        return dict(default)
    merged = dict(default)
    merged.update(loaded)
    return merged


def load_api_config() -> dict[str, Any]:
    payload = _merge_dict(DEFAULT_API_CONFIG, load_json(API_CONFIG_FILE, default=DEFAULT_API_CONFIG))
    env_key = os.getenv('ABC_API_KEY') or os.getenv('API_FOOTBALL_KEY') or _load_env_file_key()
    if env_key:
        payload['api_key'] = env_key
    return payload


def load_league_map() -> dict[str, dict[str, Any]]:
    payload = load_json(LEAGUE_MAP_FILE, default=DEFAULT_LEAGUE_MAP)
    return payload if isinstance(payload, dict) else dict(DEFAULT_LEAGUE_MAP)


def load_team_ratings() -> dict[str, float]:
    payload = load_json(TEAM_RATINGS_FILE, default=DEFAULT_TEAM_RATINGS)
    return payload if isinstance(payload, dict) else dict(DEFAULT_TEAM_RATINGS)
