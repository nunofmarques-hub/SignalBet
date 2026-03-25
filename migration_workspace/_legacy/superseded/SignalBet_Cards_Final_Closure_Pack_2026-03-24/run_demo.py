from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "src"))
sys.path.insert(0, str(BASE))

from providers.official_live_provider import OfficialLiveProvider, OfficialLiveProviderError
from providers.mappers import map_bundle_to_engine_input
from src.cards_module.core.orchestrator import build_output
from src.cards_module.core.output_validator import validate_output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--league", type=int, default=140)
    parser.add_argument("--season", type=int, default=2024)
    parser.add_argument("--fixture-index", type=int, default=0)
    args = parser.parse_args()

    out_dir = BASE / "out"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        provider = OfficialLiveProvider()
        bundle = provider.fetch_fixture_bundle(args.league, args.season, args.fixture_index)
    except OfficialLiveProviderError as exc:
        print(str(exc))
        return 2

    engine_input = map_bundle_to_engine_input(bundle)
    output = build_output(engine_input)
    errors = validate_output(output)
    file_name = f"{output['pick_id']}.json"
    with open(out_dir / file_name, "w", encoding="utf-8") as fh:
        json.dump(output, fh, indent=2, ensure_ascii=False)
    print(f"Output: {out_dir / file_name}")
    print(f"Validation errors: {errors}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
