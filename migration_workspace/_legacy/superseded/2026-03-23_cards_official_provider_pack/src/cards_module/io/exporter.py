from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def write_output(output_dir: str | Path, filename: str, payload: Dict[str, Any]) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    target = output_path / filename
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return target
