from __future__ import annotations

import importlib.util
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
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
        self.provider_path = self._resolve_provider_path()
        self.provider_module = self._load_provider_module(self.provider_path)
        self.provider_name = self.provider_path.name
        self.provider_fn = self._resolve_provider_function()

    def _known_candidates(self) -> List[Path]:
        return [
            self.trunk_root / "providers" / "fixtures_provider.py",
            self.trunk_root / "src" / "providers" / "fixtures_provider.py",
            self.trunk_root / "data_api" / "providers" / "fixtures_provider.py",
            self.trunk_root / "data_api" / "src" / "providers" / "fixtures_provider.py",
            self.trunk_root / "fixtures_provider.py",
        ]

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
        return "get_fixtures_by_league_season" in text

    def _resolve_provider_path(self) -> Path:
        if not self.trunk_root.exists():
            raise AdapterError(
                f"trunk_root not found: {self.trunk_root}. "
                "Confirma o path do Data_API_Official_Trunk_v1 ou define SIGNALBET_TRUNK_ROOT."
            )

        known_candidates = self._known_candidates()
        existing_known = [str(p) for p in known_candidates if p.exists()]

        recursive_exact = sorted(
            [p for p in self._safe_rglob("fixtures_provider.py") if p.is_file()],
            key=lambda p: (len(p.parts), str(p)),
        )

        exact_with_target = [p for p in recursive_exact if self._contains_target_function(p)]
        if exact_with_target:
            chosen = exact_with_target[0]
            self.discovery_report = {
                "mode": "recursive_exact_match",
                "known_candidates_checked": [str(p) for p in known_candidates],
                "existing_known_candidates": existing_known,
                "recursive_exact_matches": [str(p) for p in recursive_exact[:20]],
                "chosen_provider_path": str(chosen),
            }
            return chosen

        for candidate in known_candidates:
            if candidate.exists():
                self.discovery_report = {
                    "mode": "known_candidate_fallback",
                    "known_candidates_checked": [str(p) for p in known_candidates],
                    "existing_known_candidates": existing_known,
                    "chosen_provider_path": str(candidate),
                }
                return candidate

        recursive_function_hits = sorted(
            [
                p for p in self._safe_rglob("*.py")
                if p.is_file() and self._contains_target_function(p)
            ],
            key=lambda p: (len(p.parts), str(p)),
        )

        if recursive_function_hits:
            chosen = recursive_function_hits[0]
            self.discovery_report = {
                "mode": "recursive_function_search",
                "known_candidates_checked": [str(p) for p in known_candidates],
                "existing_known_candidates": existing_known,
                "recursive_function_hits": [str(p) for p in recursive_function_hits[:20]],
                "chosen_provider_path": str(chosen),
            }
            return chosen

        report = {
            "known_candidates_checked": [str(p) for p in known_candidates],
            "existing_known_candidates": existing_known,
            "recursive_exact_matches": [str(p) for p in recursive_exact[:20]],
            "recursive_function_hits": [str(p) for p in recursive_function_hits[:20]],
        }
        raise AdapterError(
            "fixtures_provider.py not found or provider function unavailable under "
            f"trunk_root={self.trunk_root}. Discovery report: {json.dumps(report, ensure_ascii=False)}"
        )

    def _load_provider_module(self, provider_path: Path):
        sys.path.insert(0, str(provider_path.parent))
        sys.path.insert(0, str(self.trunk_root))
        module_name = f"signalbet_fixtures_provider_{abs(hash(str(provider_path)))}"
        spec = importlib.util.spec_from_file_location(module_name, provider_path)
        if spec is None or spec.loader is None:
            raise AdapterError(f"Unable to load provider module from {provider_path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
        return module

    def _resolve_provider_function(self):
        fn = getattr(self.provider_module, "get_fixtures_by_league_season", None)
        if fn is None or not callable(fn):
            raise AdapterError(
                "Provider function get_fixtures_by_league_season() not available "
                f"in {self.provider_path}"
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

    def _call_provider(self, league_id: int, season: int) -> List[Dict[str, Any]]:
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
                fixtures = self._call_provider(scenario.league_id, scenario.season)
            except Exception as exc:  # noqa: BLE001
                last_error = f"{scenario.label}: {exc}"
                continue

            filtered_by_status = [f for f in fixtures if self._match_status(f, scenario.statuses)]
            for start, end, window_label in DEFAULT_WINDOWS:
                filtered = [f for f in filtered_by_status if self._match_window(f, start, end)]
                payload = {
                    "snapshot_name": "fixtures_calibration_snapshot",
                    "version": "1.1.1",
                    "provider": self.provider_name,
                    "provider_path": str(self.provider_path),
                    "provider_discovery": self.discovery_report,
                    "service": "get_fixtures_by_league_season()",
                    "primary_consumer": "orchestrator",
                    "league_id": scenario.league_id,
                    "season": scenario.season,
                    "coverage_scenario": scenario.label,
                    "coverage_statuses": list(scenario.statuses),
                    "coverage_window": {
                        "start": start,
                        "end": end,
                        "label": window_label,
                    },
                    "fixtures_count": len(filtered),
                    "fixtures": filtered,
                    "snapshot_status": "fresh" if filtered else "empty",
                    "generated_at": datetime.now(timezone.utc).isoformat(),
                }
                if best_payload is None or payload["fixtures_count"] > best_payload["fixtures_count"]:
                    best_payload = payload
                if payload["fixtures_count"] > 1:
                    return payload

        if best_payload is not None:
            return best_payload
        raise AdapterError(last_error or "Unable to fetch fixtures from official provider")


def dump_json(path: str | os.PathLike[str], payload: Dict[str, Any]) -> None:
    Path(path).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
