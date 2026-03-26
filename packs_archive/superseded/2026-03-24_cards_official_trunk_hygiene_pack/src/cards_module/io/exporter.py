from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


def write_output(payload: Dict, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    suffix = payload.get('pack_status', 'unknown')
    path = out_dir / f"{suffix}.json"
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
    return path
