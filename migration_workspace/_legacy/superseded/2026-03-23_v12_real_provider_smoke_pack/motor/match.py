from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass(slots=True)
class Match:
    fixture_id: int
    date: str
    country: str
    league: str
    home_team: str
    away_team: str
    league_id: int | None = None
    season: int | None = None
    status_short: str = ''
    home_team_id: int | None = None
    away_team_id: int | None = None
    favorite_team: str | None = None
    source: str = 'API'

    @property
    def game_label(self) -> str:
        return f'{self.home_team} vs {self.away_team}'

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload['game'] = self.game_label
        return payload
