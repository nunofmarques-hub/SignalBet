# CORNERS_SWAP_CLEAN_NOTE

## objetivo
Fechar swap limpo da linha atual do Corners.

## decisão
`runtime_inputs/` fica mantido nesta linha por compatibilidade estrutural explícita.

## confirmação
- sem dependência oculta adicional no `run_smoke.py`
- pasta mantida para evitar ambiguidade no swap da linha ativa
