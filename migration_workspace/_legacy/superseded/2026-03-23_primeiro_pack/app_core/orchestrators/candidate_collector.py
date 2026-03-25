from __future__ import annotations

from typing import Any, Dict, List


def collect_candidates(module_outputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    candidate_count = sum(item.get("candidates_count", 0) for item in module_outputs)
    return {
        "source_modules": [item["module_id"] for item in module_outputs if item.get("status") != "SKIPPED"],
        "candidate_count": candidate_count,
        "candidates": [],
    }
