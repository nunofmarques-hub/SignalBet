from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExecutionAttempt:
    execution_id: str
    attempted_at: datetime
    attempt_status: str
    approved_odds_reference: float
    approved_odds_window: str
    executed_odds: float | None
    stake_approved: float
    stake_executed: float
    slippage_vs_reference: float | None
    odds_within_window: bool | None
    reason_code: str | None = None
    reason_text: str | None = None
