from __future__ import annotations
from datetime import datetime
from .models import ExecutionAttempt
from .pricing_rules import is_within_window


class ExecutionService:
    def register_attempt(self, order, executed_odds: float | None, stake_executed: float, reason_code: str | None = None, reason_text: str | None = None) -> ExecutionAttempt:
        within_window = None if executed_odds is None else is_within_window(executed_odds, order.metadata["approved_odds_window"])
        slippage = None if executed_odds is None else round(executed_odds - order.metadata["approved_odds_reference"], 4)
        return ExecutionAttempt(
            execution_id=order.execution_id,
            attempted_at=datetime.utcnow(),
            attempt_status="EXECUTED" if executed_odds is not None else "FAILED",
            approved_odds_reference=order.metadata["approved_odds_reference"],
            approved_odds_window=order.metadata["approved_odds_window"],
            executed_odds=executed_odds,
            stake_approved=order.metadata["stake_approved"],
            stake_executed=stake_executed,
            slippage_vs_reference=slippage,
            odds_within_window=within_window,
            reason_code=reason_code,
            reason_text=reason_text,
        )
