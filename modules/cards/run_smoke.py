from __future__ import annotations

import argparse
import json

from bootstrap_runtime import configure_paths

BASE = configure_paths(__file__)

from providers.official_live_provider import OfficialLiveProvider
from providers.mappers import map_bundle_to_engine_input
from cards_module.core.orchestrator import build_output
from cards_module.core.output_validator import validate_output


def run_contract_smoke() -> int:
    fixtures = [{
        "fixture": {"id": 999001},
        "teams": {"home": {"name": "Home FC"}, "away": {"name": "Away FC"}},
        "league": {"name": "Primeira Liga"},
    }]
    events = [
        {"type": "Card", "detail": "Yellow Card"},
        {"type": "Card", "detail": "Red Card"},
        {"type": "Goal", "detail": "Normal Goal"},
    ]
    provider = OfficialLiveProvider(
        fixtures_service=lambda league, season: fixtures,
        events_service=lambda fixture_id, league, season: events,
    )
    bundle = provider.fetch_fixture_bundle(140, 2024)
    payload = build_output(map_bundle_to_engine_input(bundle))
    errors = validate_output(payload)
    print(json.dumps({"mode": "contract-smoke", "errors": errors, "eligibility": payload["eligibility"]}, ensure_ascii=False))
    return 0 if not errors else 1


def run_live(league: int, season: int) -> int:
    provider = OfficialLiveProvider()
    bundle = provider.fetch_fixture_bundle(league, season)
    payload = build_output(map_bundle_to_engine_input(bundle))
    errors = validate_output(payload)
    print(json.dumps({
        "mode": "live",
        "errors": errors,
        "eligibility": payload["eligibility"],
        "pick_id": payload["pick_id"],
    }, ensure_ascii=False))
    return 0 if not errors else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Runner oficial desta fase para o Cards.")
    parser.add_argument("--mode", choices=["contract-smoke", "live"], default="contract-smoke")
    parser.add_argument("--league", type=int, default=140)
    parser.add_argument("--season", type=int, default=2024)
    args = parser.parse_args()
    if args.mode == "contract-smoke":
        return run_contract_smoke()
    return run_live(args.league, args.season)


if __name__ == "__main__":
    raise SystemExit(main())
