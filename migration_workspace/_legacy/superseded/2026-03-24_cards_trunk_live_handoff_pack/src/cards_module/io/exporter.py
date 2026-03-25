from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


def write_output(payload: Dict, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = 'candidate' if payload.get('eligibility') else 'rejected'
    filename = f"{payload['pick_id']}__{suffix}.json"
    path = output_dir / filename
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
    return path
