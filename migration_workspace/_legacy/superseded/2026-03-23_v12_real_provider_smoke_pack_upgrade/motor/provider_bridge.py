from __future__ import annotations

"""Bridge between v12 and a future real provider from the central Data/API Layer."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol
import json

class CentralProvider(Protocol):
    def fetch_match_payload(self, fixture_id: int | str) -> dict[str, Any]: ...

@dataclass
class FileCentralProvider:
    sample_path: str
    def fetch_match_payload(self, fixture_id: int | str) -> dict[str, Any]:
        payload = json.loads(Path(self.sample_path).read_text(encoding='utf-8'))
        root_fixture_id = payload.get('fixture', {}).get('fixture_id')
        if str(root_fixture_id) != str(fixture_id):
            raise ValueError(f'fixture_id mismatch: requested={fixture_id} payload={root_fixture_id}')
        return payload

@dataclass
class ProviderBridge:
    provider: CentralProvider
    def get_central_payload(self, fixture_id: int | str) -> dict[str, Any]:
        payload = self.provider.fetch_match_payload(fixture_id)
        payload.setdefault('_provider_meta', {
            'provider_name': self.provider.__class__.__name__,
            'provider_mode': 'real_shape_sample'
        })
        return payload
