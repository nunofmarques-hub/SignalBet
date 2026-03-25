#!/usr/bin/env python3
"""
SignalBet / ABC PRO - Mini pipeline de fixtures para API-Football

Objetivo:
- Descobrir fixtures concluídos por league + season + status
- Extrair fixture IDs
- Guardar cache local auditável
- Enriquecer fixtures em batch via /fixtures?ids=...
- Validar estatísticas por fixture via /fixtures/statistics?fixture=...

Pensado para correr de forma portátil, incluindo Python embeddable.
Sem dependências externas.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

API_BASE = "https://v3.football.api-sports.io"
DEFAULT_LEAGUE = 140  # LaLiga
DEFAULT_SEASON = 2024
DEFAULT_STATUS = "FT-AET-PEN"
REQUESTS_PER_MINUTE_FREE = 10
DEFAULT_SLEEP_SECONDS = 7.0  # conservador para plano Free
DEFAULT_TIMEOUT = 30


class ApiError(RuntimeError):
    pass


@dataclass
class Config:
    api_key: str
    root_dir: Path
    data_dir: Path
    sleep_seconds: float = DEFAULT_SLEEP_SECONDS
    timeout_seconds: int = DEFAULT_TIMEOUT


def load_api_key(search_root: Path) -> str:
    """
    Lê a API key a partir de api.env.txt no diretório base.
    Formato esperado:
    API_KEY=xxxxxxxx
    """
    env_path = search_root / "api.env.txt"
    if not env_path.exists():
        raise FileNotFoundError(
            f"Não encontrei {env_path}. Cria esse ficheiro ao lado do script com a linha API_KEY=..."
        )

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("API_KEY="):
            value = line.split("=", 1)[1].strip()
            if value:
                return value

    raise ValueError(f"O ficheiro {env_path} existe, mas não encontrei uma linha válida API_KEY=...")


def ensure_dirs(base_data_dir: Path, league: int, season: int) -> Dict[str, Path]:
    root = base_data_dir / f"league_{league}" / f"season_{season}"
    paths = {
        "root": root,
        "catalog": root / "catalog",
        "raw": root / "raw",
        "batches": root / "raw" / "batches",
        "stats": root / "raw" / "stats",
        "masters": root / "masters",
        "logs": root / "logs",
    }
    for p in paths.values():
        p.mkdir(parents=True, exist_ok=True)
    return paths


class ApiFootballClient:
    def __init__(self, config: Config):
        self.config = config
        self._last_call_ts = 0.0

    def _throttle(self) -> None:
        elapsed = time.time() - self._last_call_ts
        if elapsed < self.config.sleep_seconds:
            time.sleep(self.config.sleep_seconds - elapsed)

    def get(self, endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
        self._throttle()

        query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        url = f"{API_BASE}{endpoint}?{query}" if query else f"{API_BASE}{endpoint}"

        req = urllib.request.Request(
            url,
            headers={
                "x-apisports-key": self.config.api_key,
                "Accept": "application/json",
            },
            method="GET",
        )

        try:
            with urllib.request.urlopen(req, timeout=self.config.timeout_seconds) as resp:
                body = resp.read().decode("utf-8")
                self._last_call_ts = time.time()
                payload = json.loads(body)
                if not isinstance(payload, dict):
                    raise ApiError(f"Resposta inesperada em {url}")
                return payload
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            raise ApiError(f"HTTP {e.code} em {url}\n{detail}") from e
        except urllib.error.URLError as e:
            raise ApiError(f"Erro de rede em {url}: {e}") from e

    def get_league_coverage(self, league: int) -> Dict[str, Any]:
        return self.get("/leagues", {"id": league})

    def get_fixtures_catalog(self, league: int, season: int, status: str) -> Dict[str, Any]:
        return self.get("/fixtures", {"league": league, "season": season, "status": status})

    def get_fixtures_by_ids(self, fixture_ids: List[int]) -> Dict[str, Any]:
        if not fixture_ids:
            raise ValueError("fixture_ids vazio")
        if len(fixture_ids) > 20:
            raise ValueError("A rota /fixtures?ids=... aceita no máximo 20 IDs por pedido")
        joined = "-".join(str(x) for x in fixture_ids)
        return self.get("/fixtures", {"ids": joined})

    def get_fixture_statistics(self, fixture_id: int) -> Dict[str, Any]:
        return self.get("/fixtures/statistics", {"fixture": fixture_id})


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def chunked(items: List[int], size: int) -> Iterable[List[int]]:
    for i in range(0, len(items), size):
        yield items[i : i + size]


def extract_fixture_rows(catalog_payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for item in catalog_payload.get("response", []):
        fixture = item.get("fixture", {})
        league = item.get("league", {})
        teams = item.get("teams", {})
        goals = item.get("goals", {})
        score = item.get("score", {})

        rows.append(
            {
                "fixture_id": fixture.get("id"),
                "referee": fixture.get("referee"),
                "timezone": fixture.get("timezone"),
                "date": fixture.get("date"),
                "timestamp": fixture.get("timestamp"),
                "status_long": (fixture.get("status") or {}).get("long"),
                "status_short": (fixture.get("status") or {}).get("short"),
                "elapsed": (fixture.get("status") or {}).get("elapsed"),
                "league_id": league.get("id"),
                "league_name": league.get("name"),
                "country": league.get("country"),
                "season": league.get("season"),
                "round": league.get("round"),
                "home_team_id": (teams.get("home") or {}).get("id"),
                "home_team_name": (teams.get("home") or {}).get("name"),
                "away_team_id": (teams.get("away") or {}).get("id"),
                "away_team_name": (teams.get("away") or {}).get("name"),
                "goals_home": goals.get("home"),
                "goals_away": goals.get("away"),
                "score_halftime_home": (score.get("halftime") or {}).get("home"),
                "score_halftime_away": (score.get("halftime") or {}).get("away"),
                "score_fulltime_home": (score.get("fulltime") or {}).get("home"),
                "score_fulltime_away": (score.get("fulltime") or {}).get("away"),
            }
        )
    return rows


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    headers = list(rows[0].keys())
    import csv

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def discover_pipeline(client: ApiFootballClient, league: int, season: int, status: str, dirs: Dict[str, Path]) -> List[int]:
    coverage = client.get_league_coverage(league)
    write_json(dirs["catalog"] / "league_coverage.json", coverage)

    catalog = client.get_fixtures_catalog(league=league, season=season, status=status)
    write_json(dirs["catalog"] / f"fixtures_catalog_status_{status.replace('-', '_')}.json", catalog)

    rows = extract_fixture_rows(catalog)
    rows_sorted = sorted(rows, key=lambda x: (x["date"] or "", x["fixture_id"] or 0))
    fixture_ids = [r["fixture_id"] for r in rows_sorted if r.get("fixture_id") is not None]

    write_json(dirs["catalog"] / "fixture_ids.json", fixture_ids)
    write_json(dirs["masters"] / "fixtures_master.json", rows_sorted)
    write_csv(dirs["masters"] / "fixtures_master.csv", rows_sorted)

    summary = {
        "league": league,
        "season": season,
        "status": status,
        "fixtures_found": len(fixture_ids),
        "first_fixture_id": fixture_ids[0] if fixture_ids else None,
        "last_fixture_id": fixture_ids[-1] if fixture_ids else None,
    }
    write_json(dirs["logs"] / "discover_summary.json", summary)

    return fixture_ids


def hydrate_batches_pipeline(
    client: ApiFootballClient,
    fixture_ids: List[int],
    dirs: Dict[str, Path],
    chunk_size: int = 20,
    max_batches: Optional[int] = None,
) -> Dict[str, Any]:
    if chunk_size < 1 or chunk_size > 20:
        raise ValueError("chunk_size deve estar entre 1 e 20")

    total_saved = 0
    batches_done = 0

    for idx, batch in enumerate(chunked(fixture_ids, chunk_size), start=1):
        if max_batches is not None and batches_done >= max_batches:
            break
        payload = client.get_fixtures_by_ids(batch)
        write_json(dirs["batches"] / f"batch_{idx:03d}.json", payload)
        batches_done += 1
        total_saved += len(payload.get("response", []))

    summary = {
        "batches_done": batches_done,
        "fixtures_saved_in_batches": total_saved,
        "chunk_size": chunk_size,
    }
    write_json(dirs["logs"] / "hydrate_batches_summary.json", summary)
    return summary


def stats_probe_pipeline(client: ApiFootballClient, fixture_ids: List[int], dirs: Dict[str, Path], max_items: int = 5) -> Dict[str, Any]:
    tested = []
    for fixture_id in fixture_ids[:max_items]:
        payload = client.get_fixture_statistics(fixture_id)
        write_json(dirs["stats"] / f"fixture_{fixture_id}.json", payload)

        stats_names = []
        for team_block in payload.get("response", []):
            for stat in team_block.get("statistics", []):
                if stat.get("type") not in stats_names:
                    stats_names.append(stat.get("type"))

        tested.append(
            {
                "fixture_id": fixture_id,
                "statistics_fields_found": stats_names,
            }
        )

    summary = {
        "fixtures_tested": len(tested),
        "tested": tested,
    }
    write_json(dirs["logs"] / "stats_probe_summary.json", summary)
    return summary


def resolve_fixture_ids(dirs: Dict[str, Path]) -> List[int]:
    ids_path = dirs["catalog"] / "fixture_ids.json"
    if not ids_path.exists():
        raise FileNotFoundError("Ainda não existe fixture_ids.json. Corre primeiro o comando discover.")
    return json.loads(ids_path.read_text(encoding="utf-8"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Mini pipeline de fixtures para SignalBet / ABC PRO")
    parser.add_argument("--root", default=".", help="Diretório raiz onde está o api.env.txt")
    parser.add_argument("--league", type=int, default=DEFAULT_LEAGUE, help="League ID (default: 140 LaLiga)")
    parser.add_argument("--season", type=int, default=DEFAULT_SEASON, help="Season (default: 2024)")
    parser.add_argument("--status", default=DEFAULT_STATUS, help="Status filter (default: FT-AET-PEN)")
    parser.add_argument("--sleep", type=float, default=DEFAULT_SLEEP_SECONDS, help="Espera entre chamadas")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("discover", help="Descobre fixtures e gera cache local de catálogo")

    p_hydrate = sub.add_parser("hydrate-batches", help="Enriquece fixtures em lotes via /fixtures?ids=")
    p_hydrate.add_argument("--chunk-size", type=int, default=20, help="Máximo 20")
    p_hydrate.add_argument("--max-batches", type=int, default=None, help="Opcional: limitar batches")

    p_probe = sub.add_parser("stats-probe", help="Valida /fixtures/statistics em alguns fixtures")
    p_probe.add_argument("--max-items", type=int, default=5, help="Quantos fixtures testar")

    sub.add_parser("full-bootstrap", help="Corre discover + alguns batches + stats probe")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    root_dir = Path(args.root).resolve()
    api_key = load_api_key(root_dir)
    data_dir = root_dir / "data_api_football"

    config = Config(
        api_key=api_key,
        root_dir=root_dir,
        data_dir=data_dir,
        sleep_seconds=args.sleep,
    )
    client = ApiFootballClient(config)
    dirs = ensure_dirs(config.data_dir, args.league, args.season)

    try:
        if args.command == "discover":
            fixture_ids = discover_pipeline(client, args.league, args.season, args.status, dirs)
            print(f"[OK] discover concluído | fixtures encontrados: {len(fixture_ids)}")
            print(f"[OK] catálogo: {dirs['catalog']}")
            print(f"[OK] master:   {dirs['masters'] / 'fixtures_master.csv'}")
            return 0

        if args.command == "hydrate-batches":
            fixture_ids = resolve_fixture_ids(dirs)
            summary = hydrate_batches_pipeline(
                client,
                fixture_ids,
                dirs,
                chunk_size=args.chunk_size,
                max_batches=args.max_batches,
            )
            print(f"[OK] hydrate-batches concluído | batches: {summary['batches_done']} | fixtures guardados: {summary['fixtures_saved_in_batches']}")
            return 0

        if args.command == "stats-probe":
            fixture_ids = resolve_fixture_ids(dirs)
            summary = stats_probe_pipeline(client, fixture_ids, dirs, max_items=args.max_items)
            print(f"[OK] stats-probe concluído | fixtures testados: {summary['fixtures_tested']}")
            return 0

        if args.command == "full-bootstrap":
            fixture_ids = discover_pipeline(client, args.league, args.season, args.status, dirs)
            hydrate_summary = hydrate_batches_pipeline(client, fixture_ids, dirs, chunk_size=20, max_batches=3)
            probe_summary = stats_probe_pipeline(client, fixture_ids, dirs, max_items=min(5, len(fixture_ids)))
            print(f"[OK] full-bootstrap concluído | fixtures: {len(fixture_ids)} | batches: {hydrate_summary['batches_done']} | probes: {probe_summary['fixtures_tested']}")
            return 0

        parser.print_help()
        return 1
    except Exception as e:
        print(f"[ERRO] {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
