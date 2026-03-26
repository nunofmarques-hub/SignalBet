
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from cards_module.core.orchestrator import run


def test_smoke_examples() -> None:
    examples_dir = BASE / "examples" / "real_inputs"
    for path in examples_dir.glob("*.json"):
        payload = json.loads(path.read_text(encoding="utf-8"))
        output, errors = run(payload)
        assert errors == []
        assert output["schema_version"] == "market_pick.v1.1"
        assert output["market_family"] == "cards"
        assert output["module_id"] == "cards"
