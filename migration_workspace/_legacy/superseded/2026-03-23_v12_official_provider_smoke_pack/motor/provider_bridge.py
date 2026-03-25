from __future__ import annotations

"""Bridge between v12 and the official provider shape from the central Data/API Layer."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol
import json
import os

class CentralProvider(Protocol):
    def fetch_match_payload(self, fixture_id: int | str) -> dict[str, Any]: ...

@dataclass
class FileCentralProvider:
    sample_path: str
    provider_mode: str = 'official_file'

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
            'provider_mode': getattr(self.provider, 'provider_mode', 'unknown')
        })
        return payload


def resolve_official_sample_path(pack_root: str | Path) -> Path:
    pack_root = Path(pack_root).resolve()
    env_path = os.getenv('V12_PROVIDER_SAMPLE')
    if env_path:
        return Path(env_path).resolve()

    candidates = [
        Path.cwd() / 'data_api' / 'exports' / 'v12' / 'provider_official_fixture_878317.json',
        pack_root.parent.parent.parent.parent / 'data_api' / 'exports' / 'v12' / 'provider_official_fixture_878317.json',
        pack_root / 'examples' / 'provider_official_input_sample.json',
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    return candidates[-1].resolve()
