import json
from pathlib import Path

from provider_bridge import load_official_bundle
from input_adapter import adapt_official_bundle
from market_engines import run_market_engines
from contract_output import to_contract_pick


OUTPUT_DIR = Path(__file__).resolve().parent.parent / "examples"


def main() -> None:
    bundle = load_official_bundle(140, 2024)
    adapted = adapt_official_bundle(bundle)
    rows = run_market_engines(adapted)
    picks = [to_contract_pick(r) for r in rows]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pool_path = OUTPUT_DIR / "smoke_output_pool.ndjson"
    with pool_path.open("w", encoding="utf-8") as fh:
        for pick in picks:
            fh.write(json.dumps(pick, ensure_ascii=False) + "\n")
    for pick in picks:
        variant = pick["module_specific_payload"]["market_variant"].lower()
        with (OUTPUT_DIR / f"smoke_output_{variant}.json").open("w", encoding="utf-8") as fh:
            json.dump(pick, fh, ensure_ascii=False, indent=2)
    print("SMOKE_TEST_STATUS=GREEN")
    print(f"PROVIDER={bundle['provider']}")
    print(f"SERVICES={','.join(bundle['official_services_used'])}")
    print(f"MATCH={adapted['match_label']}")
    print(f"REQUIRED_OBJECTS={','.join(bundle['required_objects_used'])}")
    print(f"OUTPUT_POOL={pool_path}")
    print(f"PICKS={len(picks)}")


if __name__ == '__main__':
    main()
