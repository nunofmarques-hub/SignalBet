from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any

@dataclass
class TeamProfile:
    team_id: int
    team_name: str
    matches: int
    goals_for: float
    goals_against: float
    score_rate_1plus: float
    concede_rate_1plus: float
    clean_sheet_inverse_rate: float
    btts_rate_proxy: float
    bos_score_lite: float = 0.0
    bvs_score_lite: float = 0.0
    ami_score_lite: float = 0.0
    tsi_score_lite: float = 0.0

@dataclass
class MatchRecord:
    fixture_id: int
    date: str
    status: str
    home_team_id: int
    home_team_name: str
    away_team_id: int
    away_team_name: str
    home_goals: int
    away_goals: int
    btts_yes: bool
    halftime_home_goals: int | None = None
    halftime_away_goals: int | None = None
    halftime_0_0: bool | None = None
    first_goal_minute: float | None = None
    goal_until_30: bool | None = None
    response_after_conceding: bool | None = None
    home_shots_on_goal: float | None = None
    away_shots_on_goal: float | None = None
    home_total_shots: float | None = None
    away_total_shots: float | None = None
    xg_gap_proxy_lite: float | None = None

@dataclass
class MarketResult:
    fixture_id: int
    match_label: str
    score_raw: float
    confidence_raw: int
    risk_raw: int
    edge_raw: str
    eligibility: bool
    rationale_summary: str
    main_drivers: list[str] = field(default_factory=list)
    penalties: list[str] = field(default_factory=list)
    data_quality_flag: str = 'partial'
    module_specific_payload: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
