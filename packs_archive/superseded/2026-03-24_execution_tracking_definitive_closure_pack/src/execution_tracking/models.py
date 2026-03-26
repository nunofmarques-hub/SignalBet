from dataclasses import dataclass
from typing import Optional

@dataclass
class IntakeRecord:
    schema_version: str
    source_system: str
    decision_id: str
    pick_id: str
    event_id: str | int
    module_origin: str
    match_label: str
    market_family: str
    market: str
    selection: str
    line: Optional[float]
    decision_status: str
    stake_approved: float
    stake_pct_bankroll: Optional[float]
    execution_order: int
    approved_odds_window: str
    odds_snapshot: float
    rules_triggered: list[str]
    execution_note: str
    portfolio_group: Optional[str]
    decision_timestamp: str
    selector_run_id: Optional[str]
    source_batch_id: Optional[str]
