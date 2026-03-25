from __future__ import annotations
from datetime import datetime


class SnapshotService:
    def freeze_initial_snapshots(self, payload: dict) -> list[dict]:
        return [
            {
                "snapshot_type": "decision_snapshot",
                "snapshot_payload": payload,
                "created_at": datetime.utcnow().isoformat(),
            },
            {
                "snapshot_type": "selector_context_snapshot",
                "snapshot_payload": {
                    "global_score": payload.get("global_score"),
                    "priority_tier": payload.get("priority_tier"),
                    "confidence_norm": payload.get("confidence_norm"),
                    "risk_norm": payload.get("risk_norm"),
                    "edge_norm": payload.get("edge_norm"),
                    "selector_flags": payload.get("selector_flags"),
                },
                "created_at": datetime.utcnow().isoformat(),
            },
            {
                "snapshot_type": "operational_snapshot",
                "snapshot_payload": {
                    "approved_odds_reference": payload.get("approved_odds_reference"),
                    "approved_odds_window": payload.get("approved_odds_window"),
                    "stake_approved": payload.get("stake_approved"),
                    "rules_triggered": payload.get("rules_triggered"),
                },
                "created_at": datetime.utcnow().isoformat(),
            },
        ]
