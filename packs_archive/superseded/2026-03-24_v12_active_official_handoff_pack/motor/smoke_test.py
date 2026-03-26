from provider_bridge import load_official_bundle
from input_adapter import adapt_official_bundle
from market_engines import run_market_engines
from contract_output import to_contract_pick


def main():
    bundle = load_official_bundle(140, 2024)
    adapted = adapt_official_bundle(bundle)
    rows = run_market_engines(adapted)
    picks = [to_contract_pick(r) for r in rows]
    print("SMOKE_TEST_STATUS=GREEN")
    print(f"PROVIDER={bundle['provider']}")
    print(f"MATCH={adapted['match_label']}")
    print(f"PICKS={len(picks)}")
    for p in picks:
        print(f"- {p['module_specific_payload']['market_variant']} -> {p['selection']}")

if __name__ == '__main__':
    main()
