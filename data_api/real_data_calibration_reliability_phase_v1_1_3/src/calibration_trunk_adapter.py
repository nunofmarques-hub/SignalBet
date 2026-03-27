
from __future__ import annotations
import json
import importlib.util
from pathlib import Path

OFFICIAL_SERVICE_NAME = "get_fixtures_by_league_season"
DEFAULT_STATUS = "FT-AET-PEN"

class TrunkAdapterError(RuntimeError):
    pass

def _load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, str(module_path))
    if spec is None or spec.loader is None:
        raise TrunkAdapterError(f"Unable to load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def resolve_fixtures_service(trunk_root: Path):
    checked_registry_paths = [
        trunk_root / "data_api" / "services" / "services_registry.json",
        trunk_root / "services" / "services_registry.json",
    ]
    registry_path = None
    registry_payload = None
    for candidate in checked_registry_paths:
        if candidate.exists():
            registry_path = candidate
            registry_payload = json.loads(candidate.read_text(encoding="utf-8"))
            break

    checked_service_paths = []
    service_path = None

    if registry_payload and isinstance(registry_payload.get("services"), list):
        for entry in registry_payload["services"]:
            if isinstance(entry, dict) and entry.get("name") == OFFICIAL_SERVICE_NAME:
                module_name = entry.get("module", "fixtures_service.py")
                candidate = trunk_root / "data_api" / "services" / module_name
                checked_service_paths.append(str(candidate))
                if candidate.exists():
                    service_path = candidate
                    break

    if service_path is None:
        fallback_candidates = [
            trunk_root / "data_api" / "services" / "fixtures_service.py",
            trunk_root / "services" / "fixtures_service.py",
        ]
        for candidate in fallback_candidates:
            checked_service_paths.append(str(candidate))
            if candidate.exists():
                service_path = candidate
                break

    if service_path is None:
        for candidate in trunk_root.rglob("fixtures_service.py"):
            checked_service_paths.append(str(candidate))
            service_path = candidate
            break

    if service_path is None or not service_path.exists():
        raise TrunkAdapterError(
            f"Official service module not found under trunk_root={trunk_root}"
        )

    # Make trunk importable for intra-package imports like data_api.paths
    import sys
    root_str = str(trunk_root)
    if root_str not in sys.path:
        sys.path.insert(0, root_str)

    module = _load_module(service_path, "signalbet_fixtures_service")
    fn = getattr(module, OFFICIAL_SERVICE_NAME, None)
    if fn is None or not callable(fn):
        raise TrunkAdapterError(
            f"Official service function {OFFICIAL_SERVICE_NAME}() not available in {service_path}"
        )

    discovery_report = {
        "mode": "services_registry" if registry_path else "fallback_search",
        "checked_registry_paths": [str(p) for p in checked_registry_paths],
        "checked_service_paths": checked_service_paths,
        "chosen_provider_path": str(service_path),
    }
    return fn, service_path, discovery_report

def discover_available_scenarios(trunk_root: Path):
    storage_roots = [
        trunk_root / "data_api" / "storage" / "raw",
        trunk_root / "storage" / "raw",
    ]
    scenarios = []
    checked_storage_roots = [str(p) for p in storage_roots]
    for storage_root in storage_roots:
        if not storage_root.exists():
            continue
        for league_dir in storage_root.glob("league_*"):
            if not league_dir.is_dir():
                continue
            league_match = league_dir.name.replace("league_", "")
            if not league_match.isdigit():
                continue
            league_id = int(league_match)
            for season_dir in league_dir.glob("season_*"):
                if not season_dir.is_dir():
                    continue
                season_match = season_dir.name.replace("season_", "")
                if not season_match.isdigit():
                    continue
                season = int(season_match)
                catalog_dir = season_dir / "catalog"
                if not catalog_dir.exists():
                    continue
                for file_path in catalog_dir.glob("fixtures_catalog_status_*.json"):
                    suffix = file_path.stem.replace("fixtures_catalog_status_", "")
                    status = suffix.replace("_", "-")
                    scenarios.append({
                        "league_id": league_id,
                        "season": season,
                        "status": status,
                        "catalog_path": str(file_path),
                    })
    return {
        "checked_storage_roots": checked_storage_roots,
        "available_scenarios": scenarios,
    }

def call_service_for_scenario(service_fn, scenario: dict):
    fixtures = service_fn(
        int(scenario["league_id"]),
        int(scenario["season"]),
        str(scenario["status"]),
    )
    if fixtures is None:
        fixtures = []
    return fixtures
