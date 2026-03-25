from __future__ import annotations
import json
from pathlib import Path
from .models import TeamProfile, MatchRecord


def load_team_profiles(path: str | Path) -> dict[int, TeamProfile]:
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    allowed = set(TeamProfile.__dataclass_fields__.keys())
    result: dict[int, TeamProfile] = {}
    for row in data:
        filtered = {k: row.get(k) for k in allowed}
        profile = TeamProfile(**filtered)
        result[profile.team_id] = profile
    return result


def load_match_master(path: str | Path) -> list[MatchRecord]:
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    allowed = set(MatchRecord.__dataclass_fields__.keys())
    rows = []
    for row in data:
        filtered = {k: row.get(k) for k in allowed}
        rows.append(MatchRecord(**filtered))
    return rows
