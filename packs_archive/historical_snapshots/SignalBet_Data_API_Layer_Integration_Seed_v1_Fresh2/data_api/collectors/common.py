from __future__ import annotations
import json
import time
from pathlib import Path
from typing import Any

def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def load_state(path: Path, total: int = 0) -> dict[str, Any]:
    if path.exists():
        try:
            data = read_json(path)
            data.setdefault("done", [])
            data.setdefault("failed", [])
            data.setdefault("last_success_item", None)
            data.setdefault("total", total)
            return data
        except Exception:
            pass
    return {"total": total, "done": [], "failed": [], "last_success_item": None, "updated_at": None}

def save_state(path: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    write_json(path, state)
