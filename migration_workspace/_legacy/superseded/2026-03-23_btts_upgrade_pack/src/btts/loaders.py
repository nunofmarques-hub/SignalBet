from __future__ import annotations
import json
from pathlib import Path
from .models import MatchInput, TeamSnapshot

def load_match_input(path: str | Path) -> MatchInput:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return MatchInput(
        event_id=data["event_id"],
        match_label=data["match_label"],
        competition=data["competition"],
        kickoff_datetime=data["kickoff_datetime"],
        market_family=data["market_family"],
        market=data["market"],
        selection_hint=data["selection_hint"],
        odds=data["odds"],
        home_snapshot=TeamSnapshot(**data["home_snapshot"]),
        away_snapshot=TeamSnapshot(**data["away_snapshot"]),
        data_api_context=data["data_api_context"],
    )
