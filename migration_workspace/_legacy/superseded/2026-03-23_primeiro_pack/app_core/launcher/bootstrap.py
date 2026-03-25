from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict
import uuid


def generate_run_id() -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"RUN-{ts}-{uuid.uuid4().hex[:6].upper()}"


def bootstrap(run_request: Dict[str, Any]) -> Dict[str, Any]:
    """Cria o contexto base da corrida a partir do pedido recebido da UI ou CLI."""
    return {
        "run_id": generate_run_id(),
        "run_profile": run_request.get("run_profile", "validation_run"),
        "initiated_by": run_request.get("initiated_by", "system"),
        "dry_run": run_request.get("dry_run", False),
        "forced_modules": run_request.get("forced_modules", []),
        "data_snapshot_tag": run_request.get("data_snapshot_tag", "latest"),
        "correlation_id": run_request.get("correlation_id") or uuid.uuid4().hex,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
