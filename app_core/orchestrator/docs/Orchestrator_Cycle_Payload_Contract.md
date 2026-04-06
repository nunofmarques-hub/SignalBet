# Orchestrator Cycle Payload — contrato curto oficial

## ficheiro oficial vivo
- `integration_feeds/orchestrator/latest.json`

## regra desta fase
- envelope único
- 1 caso único
- 1 `pick_id` estável do início ao fim
- sem payload alternativo na linha ativa
- UI continua a consumir apenas o payload protegido

## blocos principais
- `system_status`
- `active_case`
  - `bankroll_decision`
  - `execution_tracking`
  - `settlement`
  - `corridor_state`

## identidade que não deve mudar a meio do ciclo
- `pick_id`
- `fixture_id`
- `match_label`
- `market_code`
- `selection_label`

## campos de estado que devem evoluir ao longo do ciclo
- `payload_status`
- `bankroll_decision`
- `execution_tracking`
- `settlement`
- `corridor_state`
- `system_status.final_status`
