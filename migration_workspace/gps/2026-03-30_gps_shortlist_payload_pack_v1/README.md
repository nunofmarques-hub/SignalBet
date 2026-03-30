# GPS Shortlist Payload Pack v1

## objetivo do pack
Entregar o bloco `shortlist` curto da app fase 1 para consumo pelo Orchestrator.

## estado do pack
staging

## módulo/frente
global_pick_selector

## ponto de entrada
- pipeline normal do corredor
- módulos integrados

## ponto de saída
- `contracts/gps_shortlist_for_orchestrator_v1.json`
- `examples/shortlist_output_example.json`

## regra desta entrega
A shortlist deve ser:
- ordenada
- curta
- legível
- sem machinery interna de ranking exposta
- sem normalização profunda no payload

## campos mínimos
- pick_id
- module_name
- fixture_id
- match_label
- market_code
- selection_label
- rank_position
- rationale_short

## destino final pretendido
- Orchestrator / App Core
