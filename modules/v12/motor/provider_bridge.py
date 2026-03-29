from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from input_adapter import InputContractError, normalize_protected_bundle


class ProviderBridge:
    def __init__(self, payload_path: str | Path) -> None:
        self.payload_path = Path(payload_path)

    def load_bundle(self) -> Dict[str, Any]:
        with self.payload_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def build_runtime_context(self) -> Dict[str, Any]:
        bundle = self.load_bundle()
        normalized = normalize_protected_bundle(bundle)
        return {
            "normalized_fixture": normalized.to_dict(),
            "runtime_status": "full_read" if normalized.readiness_level == "real_ready" else "degraded_run",
            "provider_mode": "protected_central_only",
            "motors_enabled": ["over15_team", "over15_match", "under35"],
        }


def build_context_or_fail(payload_path: str | Path) -> Dict[str, Any]:
    bridge = ProviderBridge(payload_path)
    try:
        return bridge.build_runtime_context()
    except InputContractError:
        raise
