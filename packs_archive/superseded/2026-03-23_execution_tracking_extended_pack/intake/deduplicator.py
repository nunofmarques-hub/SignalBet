from __future__ import annotations

DUPLICATE_KEYS = ("decision_id", "pick_id", "event_id", "market", "selection")


def build_duplicate_fingerprint(payload: dict) -> tuple:
    return tuple(payload.get(k) for k in DUPLICATE_KEYS)
