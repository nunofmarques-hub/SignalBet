from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ExecutionOrder:
    execution_id: str
    decision_id: str
    pick_id: str
    event_id: str
    module_origin: str
    market_family: str
    market: str
    selection: str
    match_label: str
    line: float | None
    execution_status: str
    settlement_status: str
    created_at: datetime
    updated_at: datetime
    metadata: dict = field(default_factory=dict)
