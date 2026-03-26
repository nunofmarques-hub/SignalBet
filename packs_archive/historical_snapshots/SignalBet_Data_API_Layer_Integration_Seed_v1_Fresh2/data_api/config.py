from __future__ import annotations
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / "api.env.txt"

def load_env_file(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        data[k.strip()] = v.strip()
    return data

_ENV = load_env_file(ENV_PATH)

API_KEY = _ENV.get("API_KEY", "")
DEFAULT_LEAGUE = int(_ENV.get("DEFAULT_LEAGUE", "140"))
DEFAULT_SEASON = int(_ENV.get("DEFAULT_SEASON", "2024"))
REQUESTS_PER_MINUTE = int(_ENV.get("REQUESTS_PER_MINUTE", "10"))
REQUESTS_PER_DAY = int(_ENV.get("REQUESTS_PER_DAY", "100"))
API_BASE = "https://v3.football.api-sports.io"
