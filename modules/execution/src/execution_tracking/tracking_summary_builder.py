from __future__ import annotations

from typing import Any, Dict, List, Optional


def build_tracking_item(
    pick_id: str,
    execution_status: str,
    ticket_status: str,
    settlement_status: str,
    result: Optional[str],
    pnl: Optional[float],
    timestamp: str,
) -> Dict[str, Any]:
    return {
        "pick_id": pick_id,
        "execution_status": execution_status,
        "ticket_status": ticket_status,
        "settlement_status": settlement_status,
        "result": result,
        "pnl": pnl,
        "timestamp": timestamp,
    }


def build_tracking_summary(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {"tracking_summary": items}
