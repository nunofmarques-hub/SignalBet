from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / 'data'


def ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def data_path(filename: str) -> str:
    ensure_data_dir()
    return str(DATA_DIR / filename)


def load_json(path: str, default: Any = None) -> Any:
    ensure_data_dir()
    try:
        with open(path, 'r', encoding='utf-8') as handle:
            return json.load(handle)
    except Exception:
        return default


def save_json(path: str, data: Any) -> None:
    ensure_data_dir()
    with open(path, 'w', encoding='utf-8') as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)


def ensure_json_file(path: str, default: Any) -> None:
    ensure_data_dir()
    target = Path(path)
    if not target.exists():
        save_json(path, default)
