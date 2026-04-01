import json
from pathlib import Path
from contract_constants import EXEC_STATUSES

BASE = Path(__file__).resolve().parents[1]

REQUIRED_PICK_FIELDS = {
    "selector_schema_version", "pick_id", "module_id", "module_version", "event_id", "match_label",
    "market_family", "market", "selection", "odds", "global_score", "confidence_norm", "risk_norm",
    "edge_norm", "priority_tier", "executive_rationale", "pool_status", "normalization_version"
}

ALLOWED_MODULES = {"v12", "corners", "btts", "cards"}
ALLOWED_FAMILIES = {"goals", "btts", "corners", "cards"}
ALLOWED_EDGE = {"weak", "acceptable", "strong", "very_strong"}
ALLOWED_TIER = {"Best", "Top", "Actionable", "Watchlist", "Reject"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_pick(pick: dict):
    missing = sorted(REQUIRED_PICK_FIELDS - set(pick))
    if missing:
        return False, "BLOCK_INVALID_INPUT", f"Missing fields: {', '.join(missing)}"
    if pick["module_id"] not in ALLOWED_MODULES:
        return False, "BLOCK_INVALID_INPUT", "module_id inválido"
    if pick["market_family"] not in ALLOWED_FAMILIES:
        return False, "BLOCK_INVALID_INPUT", "market_family inválido"
    if pick["edge_norm"] not in ALLOWED_EDGE:
        return False, "BLOCK_INVALID_INPUT", "edge_norm inválido"
    if pick["priority_tier"] not in ALLOWED_TIER:
        return False, "BLOCK_INVALID_INPUT", "priority_tier inválido"
    if pick["pool_status"] != "exported_to_bankroll":
        return False, "BLOCK_NOT_ELIGIBLE", "pool_status inválido"
    if not (1.20 <= float(pick["odds"]) <= 2.40):
        return False, "BLOCK_ODD_RANGE", "odd fora da janela"
    if pick["priority_tier"] == "Reject":
        return False, "BLOCK_REJECT_PRIORITY", "priority tier reject"
    return True, None, None


def stake_base(priority: str) -> float:
    return {"Best":1.25, "Top":1.00, "Actionable":0.75, "Watchlist":0.50, "Reject":0.0}[priority]


def decide_pick(pick: dict, locked_fixtures: set, bank_state: str = "Normal", module_counts=None):
    module_counts = module_counts or {}
    ok, code, note = validate_pick(pick)
    base = stake_base(pick.get("priority_tier", "Reject"))
    if not ok:
        return {
            "decision_status": "BLOCKED", "rule": code, "note": note,
            "stake_base": base, "stake_suggested": base, "stake_approved": 0.0,
            "execution_ready": False, "execution_order": None,
        }
    if pick["event_id"] in locked_fixtures:
        return {"decision_status":"BLOCKED","rule":"BLOCK_DUPLICATE_FIXTURE","note":"fixture já ocupada","stake_base":base,"stake_suggested":base,"stake_approved":0.0,"execution_ready":False,"execution_order":None}
    if module_counts.get(pick["module_id"], 0) >= 3:
        return {"decision_status":"BLOCKED","rule":"BLOCK_MODULE_LIMIT","note":"módulo no limite diário","stake_base":base,"stake_suggested":base,"stake_approved":0.0,"execution_ready":False,"execution_order":None}
    if bank_state == "Protecao_Maxima" and pick["priority_tier"] not in {"Best", "Top"}:
        return {"decision_status":"RESERVE","rule":"REDUCE_BANK_ALERT","note":"reserva em proteção máxima para não premium","stake_base":base,"stake_suggested":base,"stake_approved":0.0,"execution_ready":False,"execution_order":None}
    suggested = base
    approved = base
    rules = []
    if pick.get("correlation_flags"):
        approved = max(0.25, round(base * 0.75, 2))
        rules.append("REDUCE_PARTIAL_CORRELATION")
    if pick["risk_norm"] >= 4:
        approved = max(0.25, round(approved * 0.75, 2))
        rules.append("REDUCE_HIGH_RISK")
    if pick["edge_norm"] == "weak":
        approved = round(approved * 0.5, 2)
        rules.append("REDUCE_WEAK_EDGE")
    if bank_state == "Alerta":
        approved = round(approved * 0.9, 2)
        rules.append("REDUCE_BANK_ALERT")
    if approved < 0.25:
        return {"decision_status":"BLOCKED","rule":"BLOCK_MIN_STAKE","note":"stake abaixo do mínimo útil","stake_base":base,"stake_suggested":suggested,"stake_approved":0.0,"execution_ready":False,"execution_order":None}
    if pick["priority_tier"] == "Watchlist" and bank_state != "Normal":
        return {"decision_status":"RESERVE","rule":"REDUCE_BANK_ALERT","note":"watchlist em contexto prudencial","stake_base":base,"stake_suggested":suggested,"stake_approved":0.0,"execution_ready":False,"execution_order":None}
    status = "APPROVED_REDUCED" if approved < suggested else "APPROVED"
    if status in {"APPROVED", "APPROVED_REDUCED"}:
        locked_fixtures.add(pick["event_id"])
        module_counts[pick["module_id"]] = module_counts.get(pick["module_id"], 0) + 1
    return {"decision_status":status, "rule": rules[0] if rules else None, "note":"; ".join(rules) if rules else "entrada plena", "stake_base":base, "stake_suggested":suggested, "stake_approved":approved, "execution_ready": status in EXEC_STATUSES, "execution_order": None}


def corridor_summary():
    batch = load_json(BASE / "examples" / "gps_batch_in_v24.json")
    locked = set()
    module_counts = {}
    decisions = []
    order = 1
    bank_state_map = {"v12_001": "Normal", "corners_002": "Normal", "btts_003": "Normal", "cards_004": "Alerta"}
    for pick in batch["picks"]:
        result = decide_pick(pick, locked, bank_state=bank_state_map.get(pick["pick_id"], "Normal"), module_counts=module_counts)
        if result["execution_ready"]:
            result["execution_order"] = order
            order += 1
        decisions.append({"pick_id": pick["pick_id"], **result})
    return {
        "total": len(decisions),
        "approved": sum(1 for d in decisions if d["decision_status"] == "APPROVED"),
        "approved_reduced": sum(1 for d in decisions if d["decision_status"] == "APPROVED_REDUCED"),
        "blocked": sum(1 for d in decisions if d["decision_status"] == "BLOCKED"),
        "reserve": sum(1 for d in decisions if d["decision_status"] == "RESERVE"),
        "execution_ready": sum(1 for d in decisions if d["execution_ready"]),
        "decisions": decisions,
    }


if __name__ == "__main__":
    print(json.dumps(corridor_summary(), indent=2, ensure_ascii=False))
