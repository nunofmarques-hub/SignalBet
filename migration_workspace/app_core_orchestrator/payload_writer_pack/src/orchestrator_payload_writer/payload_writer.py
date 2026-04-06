from __future__ import annotations

import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from .contracts import ALLOWED_STATUSES, base_payload


class PayloadWriterError(Exception):
    pass


class OfficialCyclePayloadWriter:
    """Writer único do payload oficial vivo do ciclo.

    Regras fortes:
    - um único payload por ciclo
    - pick_id imutável
    - updates semânticos por fase
    - gravação sempre no mesmo ficheiro oficial
    """

    def __init__(self, output_path: str | Path):
        self.output_path = Path(output_path)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self._payload: Optional[Dict[str, Any]] = None

    @staticmethod
    def _now_iso() -> str:
        return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    def create_cycle(self, *, case_id: str, pick_id: str, shortlist: Dict[str, Any]) -> Dict[str, Any]:
        if self._payload is not None:
            raise PayloadWriterError("Cycle payload already initialized for this writer instance.")

        payload = base_payload(case_id=case_id, pick_id=pick_id)
        payload["shortlist"] = deepcopy(shortlist)
        payload["timeline"] = [
            {
                "status": "shortlist_ready",
                "timestamp": self._now_iso(),
                "source": "orchestrator",
            }
        ]
        self._payload = payload
        self._write()
        return deepcopy(self._payload)

    def update_bankroll_decision(self, *, pick_id: str, decision: Dict[str, Any]) -> Dict[str, Any]:
        self._assert_payload_exists()
        self._assert_pick_id(pick_id)
        self._payload["bankroll_decision"] = deepcopy(decision)
        self._set_status("bank_decision_ready", source="bankroll")
        self._write()
        return deepcopy(self._payload)

    def update_execution_tracking(self, *, pick_id: str, tracking: Dict[str, Any]) -> Dict[str, Any]:
        self._assert_payload_exists()
        self._assert_pick_id(pick_id)
        self._payload["execution_tracking"] = deepcopy(tracking)
        self._set_status("execution_tracking_live", source="execution")
        self._write()
        return deepcopy(self._payload)

    def update_settlement(self, *, pick_id: str, settlement: Dict[str, Any]) -> Dict[str, Any]:
        self._assert_payload_exists()
        self._assert_pick_id(pick_id)
        self._payload["settlement"] = deepcopy(settlement)
        self._set_status("settled", source="execution")
        self._write()
        return deepcopy(self._payload)

    def read_payload(self) -> Dict[str, Any]:
        self._assert_payload_exists()
        return deepcopy(self._payload)

    def _set_status(self, status: str, *, source: str) -> None:
        if status not in ALLOWED_STATUSES:
            raise PayloadWriterError(f"Invalid cycle status: {status}")
        self._payload["cycle_status"] = status
        self._payload.setdefault("timeline", []).append(
            {
                "status": status,
                "timestamp": self._now_iso(),
                "source": source,
            }
        )

    def _assert_payload_exists(self) -> None:
        if self._payload is None:
            raise PayloadWriterError("Payload not initialized. Create cycle first.")

    def _assert_pick_id(self, pick_id: str) -> None:
        if self._payload is None:
            raise PayloadWriterError("Payload not initialized.")
        expected = self._payload["pick_id"]
        if pick_id != expected:
            raise PayloadWriterError(f"pick_id drift detected: expected {expected}, got {pick_id}")

    def _write(self) -> None:
        assert self._payload is not None
        self._payload["updated_at"] = self._now_iso()
        self.output_path.write_text(json.dumps(self._payload, ensure_ascii=False, indent=2), encoding="utf-8")
