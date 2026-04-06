# ORCHESTRATOR_CHAT_MEMORY_CURRENT

## feito
- Shadow run do corredor completo validado em GREEN.
- OR16 consolidado como linha oficial ativa do output protegido.
- Payload protegido único da app phase 1 fechado como base anterior.
- UI passou a consumir corretamente o payload protegido.
- Payload oficial do ciclo real controlado aberto como feed vivo desta ronda.

## objetivo
- Manter o Orchestrator como montador oficial do payload protegido do corredor.
- Preservar 1 shape única e 1 feed oficial vivo para o caso único do ciclo.
- Garantir estabilidade de `pick_id` e semântica ao longo de shortlist, banca, execution e settlement.

## decisão
- Linha oficial ativa do Orchestrator nesta fase: OR16 + official cycle payload.
- O feed oficial vivo desta ronda fica em `integration_feeds/orchestrator/latest.json`.
- Não manter payload paralelo competitivo na linha ativa.

## estado atual
- `current_status`: official_active
- `runner_oficial_desta_fase`: `run_smoke.py`
- `official_live_feed`: `integration_feeds/orchestrator/latest.json`
- `ui_consumption_status`: deve continuar a ler apenas payload protegido
- `cycle_payload_status`: pronto para teste controlado

## bloqueio
- sem bloqueio estrutural nesta fase

## próximo passo
- testar atualização do mesmo ficheiro ao longo do ciclo
- validar shortlist -> banca -> execution -> settlement sem drift de identidade
