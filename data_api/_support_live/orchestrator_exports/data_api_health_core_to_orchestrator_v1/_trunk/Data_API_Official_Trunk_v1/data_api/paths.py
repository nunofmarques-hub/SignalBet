from __future__ import annotations
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_API_DIR = ROOT_DIR / "data_api"
STORAGE_DIR = DATA_API_DIR / "storage"
RAW_DIR = STORAGE_DIR / "raw"
NORMALIZED_DIR = STORAGE_DIR / "normalized"
DERIVED_DIR = STORAGE_DIR / "derived"
STATE_DIR = STORAGE_DIR / "state"
LOGS_DIR = DATA_API_DIR / "logs"
REGISTRY_DIR = DATA_API_DIR / "registry"

def ensure_base_dirs() -> None:
    for p in [RAW_DIR, NORMALIZED_DIR, DERIVED_DIR, STATE_DIR, LOGS_DIR, REGISTRY_DIR]:
        p.mkdir(parents=True, exist_ok=True)

def season_root(league_id: int, season: int) -> Path:
    return RAW_DIR / f"league_{league_id}" / f"season_{season}"

def state_root(league_id: int, season: int) -> Path:
    return STATE_DIR / f"league_{league_id}" / f"season_{season}"
