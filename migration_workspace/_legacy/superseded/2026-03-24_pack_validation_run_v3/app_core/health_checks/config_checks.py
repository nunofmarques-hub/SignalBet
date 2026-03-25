from __future__ import annotations

from pathlib import Path
from typing import List, Dict


def run_config_checks(project_root: str) -> List[Dict[str, object]]:
    root = Path(project_root)
    api_env = root / "api.env.txt"
    settings_file = root / "settings.json"

    api_key_present = False
    if api_env.exists():
        try:
            api_key_present = any(
                line.strip().startswith("API_KEY=") and len(line.strip()) > 8
                for line in api_env.read_text(encoding="utf-8", errors="ignore").splitlines()
            )
        except OSError:
            api_key_present = False

    return [
        {"check_id": "api_env_present", "status": "PASS" if api_env.exists() else "FAIL", "message": "api.env.txt encontrado." if api_env.exists() else "api.env.txt em falta.", "blocking": True},
        {"check_id": "api_key_present", "status": "PASS" if api_key_present else "FAIL", "message": "API key presente." if api_key_present else "API key em falta ou inválida.", "blocking": True},
        {"check_id": "settings_file_present", "status": "PASS" if settings_file.exists() else "WARN", "message": "settings.json encontrado." if settings_file.exists() else "settings.json não encontrado.", "blocking": False},
    ]
