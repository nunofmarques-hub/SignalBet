from __future__ import annotations

from typing import Any, Dict


def register_execution(bankroll_output: Dict[str, Any], run_context: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "status": "PASS",
        "registered_orders": len(bankroll_output.get("approved", [])),
        "message": "Registo em draft concluído.",
    }
