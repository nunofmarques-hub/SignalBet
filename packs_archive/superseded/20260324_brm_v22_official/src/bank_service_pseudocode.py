"""Pseudo-serviço do Bankroll & Risk Manager v2.2.
Não executa decisões reais; documenta a ordem de chamadas para downstream técnico.
"""

RESOLUTION_ORDER = [
    "validate_input",
    "validate_pool_status",
    "check_reject_priority",
    "check_fixture_lock",
    "check_daily_limit",
    "check_module_limit",
    "check_odds_window",
    "compute_stake_base",
    "compute_stake_suggested",
    "apply_soft_reductions",
    "enforce_min_effective_stake",
    "emit_decision",
]

def process_pick_batch(selector_batch: dict) -> dict:
    """Fluxo lógico esperado.
    1. validar contrato batch recebido do GPS
    2. iterar picks e aplicar a cadeia de resolução
    3. emitir response batch da banca
    4. derivar payload final para execution para statuses executáveis
    """
    raise NotImplementedError("Pack de staging: pseudocódigo apenas.")
