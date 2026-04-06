from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
for item in (str(ROOT), str(SRC)):
    if item not in sys.path:
        sys.path.insert(0, item)
