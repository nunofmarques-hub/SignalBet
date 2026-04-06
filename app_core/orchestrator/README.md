# SignalBet — Orchestrator / App Core Active Clean Pack

## objetivo
Pack limpo de substituição integral da linha ativa do Orchestrator / App Core, já alinhado com o payload oficial do ciclo real controlado.

## linha ativa
- official_line_name: OR16 protected output increment + official cycle payload
- current_status: official_active

## o que este pack fixa
- Orchestrator como montador oficial do payload protegido do corredor
- 1 caso único
- 1 pick_id único e estável ao longo do ciclo
- 1 feed oficial vivo em `integration_feeds/orchestrator/latest.json`
- sem payload paralelo competitivo na linha ativa

## estrutura viva desta fase
- `integration_feeds/orchestrator/latest.json` = feed oficial ativo do ciclo
- `run_smoke.py` = runner curto de verificação
- `docs/` = contrato curto e nota de substituição
- `ORCHESTRATOR_CHAT_MEMORY_CURRENT.md` = memória operacional viva

## limpeza aplicada
- removido o payload ativo antigo em pasta separada que competia com o feed oficial atual
- mantido apenas 1 caminho oficial de consumo para o payload vivo
- sem `__pycache__`, `.pyc` ou artefactos transitórios

## destino pretendido
- `app_core/orchestrator/`

## leitura final
Linha pronta para substituição integral limpa, com feed único e coerente com as últimas atualizações do corredor.
