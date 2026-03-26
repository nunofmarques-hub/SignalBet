from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Any, List

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
    first_goal_min_avg: float
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

@dataclass
class MarketResult:
    market: str
    score_raw: float
    confidence_raw: int
    risk_raw: int
    edge_raw: str
    eligibility: bool
    rationale_summary: str
    main_drivers: List[str] = field(default_factory=list)
    penalties: List[str] = field(default_factory=list)
    data_quality_flag: str = "partial"
    module_specific_payload: Dict[str, Any] = field(default_factory=dict)
