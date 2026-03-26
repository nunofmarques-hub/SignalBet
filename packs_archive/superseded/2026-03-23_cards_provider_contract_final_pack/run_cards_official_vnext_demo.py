from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "src"))

from providers.official_cards_provider import load_central_payload, map_to_engine_input
from cards_module.core.orchestrator import run_pipeline


def main() -> None:
    out_dir = BASE / "out"
    out_dir.mkdir(exist_ok=True)
    for path in sorted((BASE / "examples" / "central_inputs").glob("*.json")):
        payload = load_central_payload(path)
        engine_input, provider_errors = map_to_engine_input(payload)
        result, validation_errors = run_pipeline(engine_input)
        name = path.stem + ("__candidate" if result["eligibility"] else "__rejected") + ".json"
        target = out_dir / name
        target.write_text(json.dumps({
            "provider_errors": provider_errors,
            "validation_errors": validation_errors,
            "result": result,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Generated: {target.name} | provider_errors={provider_errors} | validation_errors={validation_errors}")


if __name__ == "__main__":
    main()
