
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from cards_module.core.orchestrator import run


def main() -> None:
    examples_dir = BASE / "examples" / "real_inputs"
    out_dir = BASE / "out"
    out_dir.mkdir(exist_ok=True)

    for path in sorted(examples_dir.glob('*.json')):
        payload = json.loads(path.read_text(encoding='utf-8'))
        output, errors = run(payload)
        suffix = output["module_specific_payload"]["status_at_source"]
        out_path = out_dir / f"{path.stem}__{suffix}.json"
        out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"Processed: {path.name}")
        print(f"  Output: {out_path}")
        print(f"  Validation errors: {errors}")


if __name__ == "__main__":
    main()
