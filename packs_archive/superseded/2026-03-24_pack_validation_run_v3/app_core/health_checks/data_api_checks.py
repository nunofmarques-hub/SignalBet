from __future__ import annotations

from pathlib import Path
from typing import List, Dict


def run_data_api_checks(project_root: str) -> List[Dict[str, object]]:
    data_api_root = Path(project_root) / "data_api"
    trunk_root = data_api_root / "Data_API_Official_Trunk_v1"
    providers_dir = trunk_root / "providers"
    contracts_dir = trunk_root / "contracts"
    storage_dir = trunk_root / "storage"
    readme_file = trunk_root / "README.md"
    registry_file = providers_dir / "providers_registry.json"

    storage_ready = storage_dir.exists() and any(storage_dir.iterdir())
    providers_ready = providers_dir.exists() and any(providers_dir.iterdir())
    contracts_ready = contracts_dir.exists() and any(contracts_dir.iterdir())

    return [
        {"check_id": "data_api_root_present", "status": "PASS" if data_api_root.exists() else "FAIL", "message": "data_api/ encontrada." if data_api_root.exists() else "data_api/ em falta.", "blocking": True},
        {"check_id": "official_trunk_root_present", "status": "PASS" if trunk_root.exists() else "FAIL", "message": "Data_API_Official_Trunk_v1 encontrado." if trunk_root.exists() else "Data_API_Official_Trunk_v1 em falta.", "blocking": True},
        {"check_id": "official_trunk_readme_present", "status": "PASS" if readme_file.exists() else "WARN", "message": "README do tronco encontrado." if readme_file.exists() else "README do tronco em falta.", "blocking": False},
        {"check_id": "official_trunk_providers_present", "status": "PASS" if providers_ready else "FAIL", "message": "Providers mínimos do tronco encontrados." if providers_ready else "Providers mínimos do tronco em falta.", "blocking": True},
        {"check_id": "official_trunk_provider_registry_present", "status": "PASS" if registry_file.exists() else "WARN", "message": "Registry de providers encontrado." if registry_file.exists() else "Registry de providers em falta.", "blocking": False},
        {"check_id": "official_trunk_contracts_present", "status": "PASS" if contracts_ready else "FAIL", "message": "Contratos mínimos do tronco encontrados." if contracts_ready else "Contratos mínimos do tronco em falta.", "blocking": True},
        {"check_id": "official_trunk_snapshot_or_cache_available", "status": "PASS" if storage_ready else "WARN", "message": "Snapshot/cache utilizável encontrado no tronco." if storage_ready else "Sem snapshot/cache utilizável visível no tronco.", "blocking": False},
    ]
