from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

ALLOWED_RESULTS = {"WIN", "LOSS", "PUSH", "VOID", "HALF_WIN", "HALF_LOSS"}


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def map_ticket_status(execution_status: str, settlement_status: str) -> str:
    if execution_status in {"SETTLED", "VOID"} or settlement_status in {"WIN", "LOSS", "PUSH", "VOID", "HALF_WIN", "HALF_LOSS"}:
        return "CLOSED"
    return "OPEN"


def normalize_result(settlement_status: str) -> Optional[str]:
    return settlement_status if settlement_status in ALLOWED_RESULTS else None


def normalize_pnl(settlement_status: str, pnl: Any) -> Optional[float]:
    if settlement_status == "UNSETTLED":
        return None
    if pnl is None:
        return None
    return float(pnl)


def build_tracking_item(record: Dict[str, Any]) -> Dict[str, Any]:
    settlement_status = record.get("settlement_status", "UNSETTLED")
    execution_status = record.get("execution_status", "EXECUTED")
    timestamp = record.get("timestamp") or iso_now()
    return {
        "pick_id": str(record["pick_id"]),
        "execution_status": execution_status,
        "ticket_status": record.get("ticket_status") or map_ticket_status(execution_status, settlement_status),
        "settlement_status": settlement_status,
        "result": record.get("result") if record.get("result") in ALLOWED_RESULTS else normalize_result(settlement_status),
        "pnl": normalize_pnl(settlement_status, record.get("pnl")),
        "timestamp": timestamp,
    }


def build_tracking_summary(records: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    return {"tracking_summary": [build_tracking_item(r) for r in records]}
