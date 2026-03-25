import json
from pathlib import Path
from .providers.official_data_api_provider import OfficialDataAPIProvider
from .loaders.official_data_api_loader import OfficialDataAPILoader
from .engine import evaluate
from .exporter import export_market_pick

def main():
    root = Path(__file__).resolve().parents[3]
    input_path = root / "sample_input" / "official_data_api_input.json"
    output_path = root / "sample_output" / "market_pick_v1_1_btts.json"
    provider = OfficialDataAPIProvider(input_path)
    loader = OfficialDataAPILoader()
    match = loader.load(provider.get_event_payload())
    result = evaluate(match)
    exported = export_market_pick(match, result)
    output_path.write_text(json.dumps(exported, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated: {output_path}")
    print(f"Score: {exported['score_raw']} | Eligibility: {exported['eligibility']} | Drivers: {exported['main_drivers']}")

if __name__ == "__main__":
    main()
