from __future__ import annotations

from .validator import validate_intake_payload
from .deduplicator import build_duplicate_fingerprint


class IntakeService:
    def receive_order(self, payload: dict) -> dict:
        errors = validate_intake_payload(payload)
        return {
            "accepted": len(errors) == 0,
            "errors": errors,
            "duplicate_fingerprint": build_duplicate_fingerprint(payload),
            "normalized_payload": payload,
        }
