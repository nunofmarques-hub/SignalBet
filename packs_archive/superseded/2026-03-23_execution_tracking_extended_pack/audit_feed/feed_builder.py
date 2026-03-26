from __future__ import annotations


def build_audit_feed(order, attempt=None, settlement=None) -> dict:
    return {
        "execution_id": order.execution_id,
        "decision_id": order.decision_id,
        "pick_id": order.pick_id,
        "module_origin": order.module_origin,
        "market_family": order.market_family,
        "market": order.market,
        "execution_status": order.execution_status,
        "settlement_status": order.settlement_status,
        "approved_odds_reference": order.metadata.get("approved_odds_reference"),
        "executed_odds": getattr(attempt, "executed_odds", None),
        "stake_approved": order.metadata.get("stake_approved"),
        "stake_executed": getattr(attempt, "stake_executed", None),
        "result_profit_loss": getattr(settlement, "result_profit_loss", None) if settlement else None,
    }
