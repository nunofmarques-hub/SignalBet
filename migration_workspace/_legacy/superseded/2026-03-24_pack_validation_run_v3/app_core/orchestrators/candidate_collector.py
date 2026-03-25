from __future__ import annotations

from typing import Any, Dict, List


def collect_candidates(module_outputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    candidates = []
    warnings = []
    for item in module_outputs:
        candidates.extend(item.get("candidates", []))
        warnings.extend(item.get("warnings", []))
    candidates.sort(key=lambda x: (x.get("score", 0), x.get("confidence", 0)), reverse=True)
    return {
        "source_modules": [item["module_id"] for item in module_outputs if item.get("status") != "SKIPPED"],
        "candidate_count": len(candidates),
        "candidates": candidates,
        "warnings": warnings,
    }
