from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass(slots=True)
class Pick:
    fixture_id: int
    market: str
    probability: float
    fair_odd: float
    market_odd: float | None
    edge: float | None
    value_label: str
    reason: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
