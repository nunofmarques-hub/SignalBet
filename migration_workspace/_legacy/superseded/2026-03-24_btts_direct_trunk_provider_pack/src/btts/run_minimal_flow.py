import json
from pathlib import Path
from .providers.direct_official_trunk_provider import BTTSDirectOfficialTrunkProvider
from .loaders.official_trunk_loader import BTTSOfficialTrunkLoader
from .engine import evaluate
from .exporter import export_market_pick

def main():
    root = Path(__file__).resolve().parents[3]
    fallback_path = root / "sample_fallback" / "fallback_official_trunk_input_btts.json"
    output_path = root / "sample_output" / "market_pick_v1_1_btts.json"

    provider = BTTSDirectOfficialTrunkProvider(fallback_path)
    payload = provider.build_official_input(140, 2024, fixture_index=0)

    loader = BTTSOfficialTrunkLoader()
    match = loader.load(payload)

    result = evaluate(match)
    exported = export_market_pick(match, result)

    output_path.write_text(json.dumps(exported, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated: {output_path}")
    print(f"Source profile: {exported['module_specific_payload']['input_context'].get('source_profile')}")
    print(f"Score: {exported['score_raw']} | Eligibility: {exported['eligibility']} | Drivers: {exported['main_drivers']}")

if __name__ == "__main__":
    main()
