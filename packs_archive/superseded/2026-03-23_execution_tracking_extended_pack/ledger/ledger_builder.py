from __future__ import annotations


def build_execution_ledger_view(order, attempt=None, settlement=None) -> dict:
    return {
        "schema_version": "execution-ledger.v1",
        "execution_id": order.execution_id,
        "decision_id": order.decision_id,
        "pick_id": order.pick_id,
        "event_id": order.event_id,
        "execution_status": order.execution_status,
        "settlement_status": order.settlement_status,
        "executed_odds": getattr(attempt, "executed_odds", None),
        "stake_executed": getattr(attempt, "stake_executed", None),
        "result_profit_loss": getattr(settlement, "result_profit_loss", None),
        "return_amount": getattr(settlement, "return_amount", None),
    }
