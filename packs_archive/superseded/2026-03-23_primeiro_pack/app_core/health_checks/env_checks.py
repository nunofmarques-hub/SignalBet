from __future__ import annotations

from pathlib import Path
from typing import Dict, List
import os
import sys


def run_environment_checks(project_root: str) -> List[Dict[str, object]]:
    root = Path(project_root)
    checks: List[Dict[str, object]] = []

    checks.append({
        "check_id": "python_available",
        "status": "PASS" if sys.version_info >= (3, 11) else "WARN",
        "message": f"Python {sys.version.split()[0]} disponível.",
        "blocking": True,
    })
    checks.append({
        "check_id": "project_root_valid",
        "status": "PASS" if root.exists() else "FAIL",
        "message": f"Project root {'encontrado' if root.exists() else 'não encontrado'}: {root}",
        "blocking": True,
    })

    required = ["migration_workspace", "data_api"]
    missing = [name for name in required if not (root / name).exists()]
    checks.append({
        "check_id": "required_folders_present",
        "status": "PASS" if not missing else "WARN",
        "message": "Pastas base presentes." if not missing else f"Pastas em falta: {', '.join(missing)}",
        "blocking": False,
    })

    writable = os.access(root, os.W_OK) if root.exists() else False
    checks.append({
        "check_id": "write_permissions_ok",
        "status": "PASS" if writable else "WARN",
        "message": "Permissões de escrita verificadas." if writable else "Sem permissão de escrita no root.",
        "blocking": False,
    })
    return checks
