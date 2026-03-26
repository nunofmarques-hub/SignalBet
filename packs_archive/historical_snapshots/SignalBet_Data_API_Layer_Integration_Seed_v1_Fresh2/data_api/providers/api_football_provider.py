from __future__ import annotations
import json
import time
import urllib.parse
import urllib.request
from typing import Any
from data_api.config import API_BASE, API_KEY, REQUESTS_PER_MINUTE

DEFAULT_SLEEP = max(6.2, 60 / max(REQUESTS_PER_MINUTE, 1))

class ApiFootballProvider:
    def __init__(self, api_key: str | None = None, sleep_seconds: float = DEFAULT_SLEEP) -> None:
        self.api_key = api_key or API_KEY
        self.sleep_seconds = sleep_seconds

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        params = params or {}
        qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        url = f"{API_BASE}{endpoint}?{qs}" if qs else f"{API_BASE}{endpoint}"
        req = urllib.request.Request(url, headers={"x-apisports-key": self.api_key})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        errors = data.get("errors")
        if isinstance(errors, dict) and errors:
            raise RuntimeError(f"API error on {endpoint}: {errors}")
        time.sleep(self.sleep_seconds)
        return data
