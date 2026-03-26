from __future__ import annotations


def build_bankroll_feedback(order, status: str, reason_code: str | None = None) -> dict:
    return {
        "decision_id": order.decision_id,
        "execution_id": order.execution_id,
        "execution_status": status,
        "reason_code": reason_code,
    }
