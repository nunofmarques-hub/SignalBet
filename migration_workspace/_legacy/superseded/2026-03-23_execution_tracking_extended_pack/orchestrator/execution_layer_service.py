from __future__ import annotations
from datetime import datetime

from intake.intake_service import IntakeService
from ledger.models import ExecutionOrder
from ledger.repository import OrderRepository
from snapshots.snapshot_service import SnapshotService
from state_machine.state_machine import StateMachine
from execution.execution_service import ExecutionService
from settlement.settlement_service import SettlementService
from ledger.ledger_builder import build_execution_ledger_view


class ExecutionLayerService:
    def __init__(self) -> None:
        self.intake = IntakeService()
        self.orders = OrderRepository()
        self.snapshots = SnapshotService()
        self.state_machine = StateMachine()
        self.execution = ExecutionService()
        self.settlement = SettlementService()

    def intake_bankroll_order(self, payload: dict) -> dict:
        result = self.intake.receive_order(payload)
        if not result["accepted"]:
            return {
                "schema_version": "execution-ledger.v1",
                "execution_id": None,
                "decision_id": payload.get("decision_id"),
                "pick_id": payload.get("pick_id"),
                "event_id": payload.get("event_id"),
                "execution_status": "REJECTED_AT_EXECUTION",
                "settlement_status": "UNSETTLED",
                "execution_reason_code": result["errors"][0] if result["errors"] else "INVALID_SCHEMA",
                "execution_reason_text": "Intake validation failed",
            }

        execution_id = f"EXEC-{payload['decision_id']}"
        order = ExecutionOrder(
            execution_id=execution_id,
            decision_id=payload["decision_id"],
            pick_id=payload["pick_id"],
            event_id=payload["event_id"],
            module_origin=payload["module_origin"],
            market_family=payload["market_family"],
            market=payload["market"],
            selection=payload["selection"],
            match_label=payload["match_label"],
            line=payload.get("line"),
            execution_status="READY_TO_EXECUTE",
            settlement_status="UNSETTLED",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            metadata={
                "approved_odds_reference": payload["approved_odds_reference"],
                "approved_odds_window": payload["approved_odds_window"],
                "stake_approved": payload["stake_approved"],
            },
        )
        self.orders.save(order)
        self.snapshots.freeze_initial_snapshots(payload)
        return build_execution_ledger_view(order)

    def register_execution(self, execution_id: str, executed_odds: float, stake_executed: float) -> dict:
        order = self.orders.get(execution_id)
        attempt = self.execution.register_attempt(order, executed_odds, stake_executed)
        order.execution_status = "AWAITING_SETTLEMENT"
        return build_execution_ledger_view(order, attempt=attempt)

    def settle_execution(self, execution_id: str, fixture_data: dict, executed_odds: float, stake_executed: float) -> dict:
        order = self.orders.get(execution_id)
        attempt = self.execution.register_attempt(order, executed_odds, stake_executed)
        settlement = self.settlement.settle(order, attempt, fixture_data)
        order.execution_status = "VOID" if settlement["settlement_status"] == "VOID" else "SETTLED"
        order.settlement_status = settlement["settlement_status"]
        class _SettlementObj:
            result_profit_loss = settlement["result_profit_loss"]
            return_amount = settlement["return_amount"]
        return build_execution_ledger_view(order, attempt=attempt, settlement=_SettlementObj())
