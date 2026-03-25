from __future__ import annotations

from pathlib import Path
from typing import List, Dict


def run_pipeline_checks(project_root: str) -> List[Dict[str, object]]:
    root = Path(project_root)
    expected = {
        "gps_available": root / "global_pick_selector",
        "bankroll_available": root / "bankroll_manager",
        "execution_available": root / "execution_tracking",
    }
    checks: List[Dict[str, object]] = []
    for check_id, path in expected.items():
        exists = path.exists()
        checks.append({"check_id": check_id, "status": "PASS" if exists else "WARN", "message": f"{path.name} {'disponível' if exists else 'não encontrado'}.", "blocking": False})
    return checks
