from __future__ import annotations

import sys
from pathlib import Path


def _find_project_root(anchor_file: str) -> Path:
    current = Path(anchor_file).resolve()
    start = current if current.is_dir() else current.parent
    for candidate in [start, *start.parents]:
        if (candidate / "manifest.json").exists() and (candidate / "src").exists() and (candidate / "providers").exists():
            return candidate
    return start


def configure_paths(anchor_file: str) -> Path:
    project_root = _find_project_root(anchor_file)
    src_root = project_root / "src"
    ordered = [str(project_root), str(src_root)]
    for item in reversed(ordered):
        if item in sys.path:
            sys.path.remove(item)
        sys.path.insert(0, item)
    return project_root
