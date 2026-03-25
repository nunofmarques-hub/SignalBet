from __future__ import annotations


def compute_return_amount(settlement_status: str, stake_executed: float, executed_odds: float | None) -> float:
    if settlement_status == "WIN":
        return round(stake_executed * float(executed_odds or 0.0), 2)
    if settlement_status in {"PUSH", "VOID"}:
        return round(stake_executed, 2)
    return 0.0


def compute_profit_loss(return_amount: float, stake_executed: float) -> float:
    return round(return_amount - stake_executed, 2)
