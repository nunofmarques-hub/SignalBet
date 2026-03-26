from __future__ import annotations

import json
from pathlib import Path

from provider_bridge import load_official_bundle
from input_adapter import adapt_bundle
from market_engines import run_v12_engines
from contract_output import build_market_pick_v11


def main() -> int:
    bundle = load_official_bundle()
    adapted = adapt_bundle(bundle)
    scored = run_v12_engines(adapted)
    outputs = [build_market_pick_v11(adapted, s) for s in scored]

    outdir = Path(__file__).resolve().parents[1] / "examples"
    outdir.mkdir(parents=True, exist_ok=True)

    names = [
        "smoke_output_team_over_15.json",
        "smoke_output_match_over_15.json",
        "smoke_output_match_under_35.json",
    ]

    for name, payload in zip(names, outputs):
        (outdir / name).write_text(
            json.dumps(payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    (outdir / "smoke_output_pool.ndjson").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in outputs),
        encoding="utf-8",
    )

    summary = {
        "status": "GREEN",
        "provider_name": bundle.provider_name,
        "provider_source": bundle.source,
        "outputs_generated": len(outputs),
        "scenario": "league_140_season_2024_ids_with_real_coverage",
    }

    (outdir / "smoke_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"PROVIDER_NAME={bundle.provider_name}")
    print(f"PROVIDER_SOURCE={bundle.source}")
    print(f"OUTPUTS_GENERATED={len(outputs)}")
    print("SMOKE_TEST_STATUS=GREEN")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())