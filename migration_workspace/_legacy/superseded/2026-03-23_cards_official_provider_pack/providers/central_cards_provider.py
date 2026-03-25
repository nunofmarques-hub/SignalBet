from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .contracts import (
    REQUIRED_DISCIPLINE_KEYS,
    REQUIRED_FIXTURE_KEYS,
    REQUIRED_MARKET_KEYS,
    REQUIRED_TEAM_KEYS,
    REQUIRED_TOP_LEVEL_KEYS,
)


class ProviderError(ValueError):
    pass


class CentralCardsProvider:
    """Provider explícito para consumo do payload oficial da base central."""

    def load_json(self, path: str | Path) -> Dict[str, Any]:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        self.validate_payload(payload)
        return payload

    def validate_payload(self, payload: Dict[str, Any]) -> None:
        missing = REQUIRED_TOP_LEVEL_KEYS - payload.keys()
        if missing:
            raise ProviderError(f"Missing top-level keys: {sorted(missing)}")
        for name, required in [
            ("fixture", REQUIRED_FIXTURE_KEYS),
            ("teams", REQUIRED_TEAM_KEYS),
            ("discipline_context", REQUIRED_DISCIPLINE_KEYS),
            ("market_context", REQUIRED_MARKET_KEYS),
        ]:
            missing_child = required - payload[name].keys()
            if missing_child:
                raise ProviderError(f"Missing keys in {name}: {sorted(missing_child)}")

    def get_provider_name(self) -> str:
        return "central_cards_provider.v1"
