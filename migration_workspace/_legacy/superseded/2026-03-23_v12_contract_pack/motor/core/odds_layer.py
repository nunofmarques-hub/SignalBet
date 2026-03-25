from __future__ import annotations

from typing import Any

from core.settings import MARKET_ODDS_FILE
from storage.json_store import load_json


def _fixture_key(fixture_id: int) -> str:
    return str(int(fixture_id or 0))


def load_market_odds_store() -> dict[str, Any]:
    payload = load_json(MARKET_ODDS_FILE, default={})
    return payload if isinstance(payload, dict) else {}


def get_fixture_market_odds(fixture_id: int) -> dict[str, Any]:
    store = load_market_odds_store()
    fixture_block = store.get(_fixture_key(fixture_id), {})
    return fixture_block if isinstance(fixture_block, dict) else {}


def resolve_market_odd(fixture_id: int, market_name: str) -> tuple[float | None, str]:
    fixture_market_odds = get_fixture_market_odds(fixture_id)
    row = fixture_market_odds.get(market_name)
    if isinstance(row, (int, float)):
        return float(row), 'ODDS OVERRIDE'
    if isinstance(row, dict):
        odd = row.get('odd')
        source = row.get('source') or 'ODDS OVERRIDE'
        if isinstance(odd, (int, float)):
            return float(odd), str(source)
    return None, 'ESTIMATED'
