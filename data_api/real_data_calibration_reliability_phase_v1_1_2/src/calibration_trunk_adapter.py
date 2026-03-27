from __future__ import annotations

import importlib.util
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


@dataclass
class CoverageScenario:
    league_id: int
    season: int
    statuses: Sequence[str]
    label: str


DEFAULT_SCENARIOS: List[CoverageScenario] = [
    CoverageScenario(league_id=140, season=2024, statuses=("FT", "AET", "PEN", "CANC"), label="primary_status_expanded"),
    CoverageScenario(league_id=39, season=2024, statuses=("FT", "AET", "PEN", "CANC"), label="alt_league_season_1"),
    CoverageScenario(league_id=78, season=2024, statuses=("FT", "AET", "PEN", "CANC"), label="alt_league_season_2"),
]

DEFAULT_WINDOWS: List[Tuple[Optional[str], Optional[str], str]] = [
    (None, None, "no_window"),
    ("2024-08-01", "2025-06-30", "window_broad_2024_2025"),
    ("2024-01-01", "2025-12-31", "window_extra_broad"),
]


class AdapterError(Exception):
    pass


class TrunkAdapter:
    def __init__(self, trunk_root: str | os.PathLike[str]) -> None:
        self.trunk_root = Path(trunk_root)
        self.discovery_report: Dict[str, Any] = {}
        self.provider_path = self._resolve_service_or_provider_path()
        self.provider_module = self._load_module(self.provider_path)
        self.provider_name = self.provider_path.name
        self.provider_fn = self._resolve_provider_function()

    def _safe_rglob(self, pattern: str) -> Iterable[Path]:
        try:
            yield from self.trunk_root.rglob(pattern)
        except Exception:
            return

    def _contains_target_function(self, path: Path) -> bool:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return False
        return "def get_fixtures_by_league_season" in text

    def _read_json_if_exists(self, path: Path) -> Optional[Dict[str, Any]]:
        try:
            if path.exists():
                return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return None
        return None

    def _known_candidates(self) -> List[Path]:
        return [
            self.trunk_root / "data_api" / "services" / "fixtures_service.py",
            self.trunk_root / "services" / "fixtures_service.py",
            self.trunk_root / "data_api" / "providers" / "fixtures_provider.py",
            self.trunk_root / "providers" / "fixtures_provider.py",
        ]

    def _resolve_service_or_provider_path(self) -> Path:
        if not self.trunk_root.exists():
            raise AdapterError(
                f"trunk_root not found: {self.trunk_root}. Confirma o path do Data_API_Official_Trunk_v1 ou define SIGNALBET_TRUNK_ROOT."
            )

        services_registry_paths = [
            self.trunk_root / "data_api" / "services" / "services_registry.json",
            self.trunk_root / "services" / "services_registry.json",
        ]
        checked_registry_paths = [str(p) for p in services_registry_paths]
        for registry_path in services_registry_paths:
            registry = self._read_json_if_exists(registry_path)
            if not registry:
                continue
            for service in registry.get("services", []):
                if service.get("name") == "get_fixtures_by_league_season":
                    module_name = service.get("module", "fixtures_service.py")
                    candidate = registry_path.parent / module_name
                    if candidate.exists() and self._contains_target_function(candidate):
                        self.discovery_report = {
                            "mode": "services_registry",
                            "checked_registry_paths": checked_registry_paths,
                            "chosen_provider_path": str(candidate),
                        }
                        return candidate

        known_candidates = self._known_candidates()
        for candidate in known_candidates:
            if candidate.exists() and self._contains_target_function(candidate):
                self.discovery_report = {
                    "mode": "known_candidate",
                    "checked_registry_paths": checked_registry_paths,
                    "known_candidates_checked": [str(p) for p in known_candidates],
                    "chosen_provider_path": str(candidate),
                }
                return candidate

        recursive_hits = sorted(
            [p for p in self._safe_rglob("*.py") if p.is_file() and self._contains_target_function(p)],
            key=lambda p: (len(p.parts), str(p)),
        )
        if recursive_hits:
            chosen = recursive_hits[0]
            self.discovery_report = {
                "mode": "recursive_function_search",
                "checked_registry_paths": checked_registry_paths,
                "known_candidates_checked": [str(p) for p in known_candidates],
                "recursive_function_hits": [str(p) for p in recursive_hits[:20]],
                "chosen_provider_path": str(chosen),
            }
            return chosen

        report = {
            "checked_registry_paths": checked_registry_paths,
            "known_candidates_checked": [str(p) for p in known_candidates],
        }
        raise AdapterError(
            "No service/provider file exposing get_fixtures_by_league_season() found under "
            f"trunk_root={self.trunk_root}. Discovery report: {json.dumps(report, ensure_ascii=False)}"
        )

    def _load_module(self, module_path: Path):
        sys.path.insert(0, str(self.trunk_root))
        sys.path.insert(0, str(module_path.parent))
        module_name = f"signalbet_fixtures_entrypoint_{abs(hash(str(module_path)))}"
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        if spec is None or spec.loader is None:
            raise AdapterError(f"Unable to load module from {module_path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
        return module

    def _resolve_provider_function(self):
        fn = getattr(self.provider_module, "get_fixtures_by_league_season", None)
        if fn is None or not callable(fn):
            raise AdapterError(
                "Function get_fixtures_by_league_season() not available in "
                f"{self.provider_path}. Discovery report: {json.dumps(self.discovery_report, ensure_ascii=False)}"
            )
        return fn

    @staticmethod
    def _normalize_fixture(raw: Dict[str, Any]) -> Dict[str, Any]:
        fixture = raw.get("fixture", raw)
        teams = raw.get("teams", {})
        home = teams.get("home", {})
        away = teams.get("away", {})
        status = fixture.get("status", {}) if isinstance(fixture.get("status"), dict) else {}
        return {
            "fixture_id": fixture.get("id") or raw.get("fixture_id"),
            "event_date": fixture.get("date") or raw.get("event_date"),
            "status_short": status.get("short") or raw.get("status_short"),
            "status_long": status.get("long") or raw.get("status_long"),
            "home_team_id": home.get("id") or raw.get("home_team_id"),
            "home_team_name": home.get("name") or raw.get("home_team_name"),
            "away_team_id": away.get("id") or raw.get("away_team_id"),
            "away_team_name": away.get("name") or raw.get("away_team_name"),
        }

    @staticmethod
    def _match_status(item: Dict[str, Any], statuses: Sequence[str]) -> bool:
        return (item.get("status_short") or "") in set(statuses)

    @staticmethod
    def _match_window(item: Dict[str, Any], start: Optional[str], end: Optional[str]) -> bool:
        event_date = item.get("event_date")
        if not event_date:
            return True
        date_str = str(event_date)[:10]
        if start and date_str < start:
            return False
        if end and date_str > end:
            return False
        return True

    def _call_provider(self, league_id: int, season: int, statuses: Sequence[str]) -> List[Dict[str, Any]]:
        requested_status = "-".join(statuses)
        try:
            result = self.provider_fn(league_id=league_id, season=season, status=requested_status)
        except TypeError:
            result = self.provider_fn(league_id=league_id, season=season)
        if result is None:
            return []
        if isinstance(result, dict):
            candidates = result.get("response") or result.get("fixtures") or result.get("data") or []
        elif isinstance(result, list):
            candidates = result
        else:
            raise AdapterError(f"Unexpected provider result type: {type(result).__name__}")
        normalized = [self._normalize_fixture(item) for item in candidates if isinstance(item, dict)]
        return [item for item in normalized if item.get("fixture_id")]

    def fetch_best_snapshot(self) -> Dict[str, Any]:
        best_payload: Optional[Dict[str, Any]] = None
        last_error: Optional[str] = None

        for scenario in DEFAULT_SCENARIOS:
            try:
                fixtures = self._call_provider(scenario.league_id, scenario.season, scenario.statuses)
            except Exception as exc:
                last_error = f"{scenario.label}: {exc}"
                continue

            filtered_by_status = [f for f in fixtures if self._match_status(f, scenario.statuses)]
            for start, end, window_label in DEFAULT_WINDOWS:
                filtered = [f for f in filtered_by_status if self._match_window(f, start, end)]
                payload = {
                    "snapshot_name": "fixtures_calibration_snapshot",
                    "version": "1.1.2",
                    "provider": self.provider_name,
                    "provider_path": str(self.provider_path),
                    "service": "get_fixtures_by_league_season()",
                    "primary_consumer": "orchestrator",
                    "league_id": scenario.league_id,
                    "season": scenario.season,
                    "coverage_scenario": scenario.label,
                    "coverage_statuses": list(scenario.statuses),
                    "coverage_window": window_label,
                    "fixtures_count": len(filtered),
                    "fixtures": filtered,
                    "snapshot_status": "fresh" if filtered else "empty",
                    "discovery_report": self.discovery_report,
                }
                if best_payload is None or payload["fixtures_count"] > best_payload["fixtures_count"]:
                    best_payload = payload
                if payload["fixtures_count"] > 1:
                    return payload

        if best_payload is not None:
            return best_payload

        raise AdapterError(f"Unable to fetch fixtures from trunk. Last error: {last_error or 'unknown'}")


def dump_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
