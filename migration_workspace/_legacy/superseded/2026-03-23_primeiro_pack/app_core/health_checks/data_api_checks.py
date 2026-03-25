from __future__ import annotations

from pathlib import Path
from typing import List, Dict


def run_data_api_checks(project_root: str) -> List[Dict[str, object]]:
    root = Path(project_root) / "data_api"
    providers_registry = root / "providers_registry.json"
    snapshots = root / "snapshots"

    return [
        {"check_id": "data_api_root_present", "status": "PASS" if root.exists() else "FAIL", "message": "data_api/ encontrada." if root.exists() else "data_api/ em falta.", "blocking": True},
        {"check_id": "providers_registry_present", "status": "PASS" if providers_registry.exists() else "WARN", "message": "providers_registry.json encontrado." if providers_registry.exists() else "providers_registry.json em falta.", "blocking": False},
        {"check_id": "official_files_present", "status": "PASS" if root.exists() and any(root.iterdir()) else "WARN", "message": "Ficheiros oficiais da Data/API disponíveis." if root.exists() and any(root.iterdir()) else "Sem ficheiros oficiais visíveis na Data/API.", "blocking": False},
        {"check_id": "latest_snapshot_available", "status": "PASS" if snapshots.exists() and any(snapshots.iterdir()) else "WARN", "message": "Snapshot utilizável encontrado." if snapshots.exists() and any(snapshots.iterdir()) else "Sem snapshot utilizável.", "blocking": False},
    ]
