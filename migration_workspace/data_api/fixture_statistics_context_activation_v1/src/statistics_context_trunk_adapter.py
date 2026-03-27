from __future__ import annotations
import importlib.util
import json
from pathlib import Path
from typing import Any


def _load_module(module_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StatisticsContextTrunkAdapter:
    def __init__(self, trunk_root: Path):
        self.trunk_root = trunk_root
        self.data_api_root = trunk_root / "data_api"
        self.services_root = self.data_api_root / "services"
        self.registry_path = self.services_root / "services_registry.json"
        self.discovery_report: dict[str, Any] = {
            "mode": "services_registry",
            "checked_registry_paths": [str(self.registry_path)],
        }
        if not self.registry_path.exists():
            raise RuntimeError(f"services_registry.json not found under trunk_root={trunk_root}")
        registry = json.loads(self.registry_path.read_text(encoding="utf-8"))
        fixtures_rel = registry.get("fixtures") or registry.get("fixtures_service") or "data_api/services/fixtures_service.py"
        stats_rel = registry.get("statistics") or registry.get("statistics_service") or "data_api/services/statistics_service.py"
        self.fixtures_service_path = trunk_root / fixtures_rel if not str(fixtures_rel).startswith("data_api/") else trunk_root / fixtures_rel
        self.statistics_service_path = trunk_root / stats_rel if not str(stats_rel).startswith("data_api/") else trunk_root / stats_rel
        if not self.fixtures_service_path.exists():
            self.fixtures_service_path = self.services_root / "fixtures_service.py"
        if not self.statistics_service_path.exists():
            self.statistics_service_path = self.services_root / "statistics_service.py"
        self.discovery_report["checked_service_paths"] = [str(self.fixtures_service_path), str(self.statistics_service_path)]
        self.discovery_report["chosen_fixtures_service_path"] = str(self.fixtures_service_path)
        self.discovery_report["chosen_statistics_service_path"] = str(self.statistics_service_path)

        import sys
        if str(self.trunk_root) not in sys.path:
            sys.path.insert(0, str(self.trunk_root))
        self.fixtures_service = _load_module(self.fixtures_service_path, "fixtures_service_runtime")
        self.statistics_service = _load_module(self.statistics_service_path, "statistics_service_runtime")
        self.get_fixtures_by_league_season = getattr(self.fixtures_service, "get_fixtures_by_league_season")
        self.get_fixture_statistics = getattr(self.statistics_service, "get_fixture_statistics")

    def load_fixtures(self, league_id: int, season: int, status: str):
        return self.get_fixtures_by_league_season(league_id, season, status=status) or []

    def load_statistics(self, fixture_id: int, league_id: int, season: int):
        return self.get_fixture_statistics(fixture_id, league_id, season) or []
