from __future__ import annotations

from .result_mapper import ResultMapper
from .formulas import compute_return_amount, compute_profit_loss


class SettlementService:
    def __init__(self) -> None:
        self.mapper = ResultMapper()

    def settle(self, order, attempt, fixture_data: dict) -> dict:
        settlement_status = self.mapper.resolve_market_result(order.market, order.selection, order.line, fixture_data)
        return_amount = compute_return_amount(settlement_status, attempt.stake_executed, attempt.executed_odds)
        profit_loss = compute_profit_loss(return_amount, attempt.stake_executed)
        return {
            "execution_id": order.execution_id,
            "settlement_status": settlement_status,
            "return_amount": return_amount,
            "result_profit_loss": profit_loss,
            "settlement_source": "DATA_API_LAYER",
        }
