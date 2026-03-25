from __future__ import annotations

from typing import Dict
from .models import ExecutionOrder


class OrderRepository:
    def __init__(self) -> None:
        self._orders: Dict[str, ExecutionOrder] = {}

    def save(self, order: ExecutionOrder) -> None:
        self._orders[order.execution_id] = order

    def get(self, execution_id: str) -> ExecutionOrder:
        return self._orders[execution_id]

    def exists(self, execution_id: str) -> bool:
        return execution_id in self._orders
