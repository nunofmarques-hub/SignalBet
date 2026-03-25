from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class TeamSnapshot:
    team_id: int
    team_name: str
    goals_for_90: float
    goals_against_90: float
    shots_on_target_90: float
    shots_on_target_against_90: float
    shots_90: float
    shots_against_90: float
    score_rate_1plus: float
    concede_rate_1plus: float
    clean_sheet_rate: float
    recent_goals_for_3: float
    recent_goals_for_5: float
    recent_score_rate_1plus: float
    recent_sot: float
    recent_form_points: float
    btts_rate: float
    first_goal_u30_rate: float
    first_half_goal_rate: float
    halftime_0_0_rate: float
    response_after_concede_rate: float
    goals_both_halves_rate: float
    home_away_attack_split: float
    home_away_defense_split: float
    league_position: int
    league_points: int

@dataclass
class MatchInput:
    event_id: int
    match_label: str
    competition: str
    kickoff_datetime: str
    market_family: str
    market: str
    selection_hint: str
    odds: Dict[str, float]
    home_snapshot: TeamSnapshot
    away_snapshot: TeamSnapshot
    data_api_context: Dict[str, Any]

class BTTSOfficialTrunkLoader:
    def load(self, payload):
        return MatchInput(
            event_id=payload["event_id"],
            match_label=payload["match_label"],
            competition=payload["competition"],
            kickoff_datetime=payload["kickoff_datetime"],
            market_family=payload["market_family"],
            market=payload["market"],
            selection_hint=payload["selection_hint"],
            odds=payload["odds"],
            home_snapshot=TeamSnapshot(**payload["home_snapshot"]),
            away_snapshot=TeamSnapshot(**payload["away_snapshot"]),
            data_api_context=payload["data_api_context"],
        )
