# GPS Shortlist Product Pack v2

## objetivo do pack
Fechar a leitura de produto do bloco `shortlist` da app phase 1, separando:
- pick principal
- pick secundária
- watchlist

## estado do pack
staging

## módulo/frente
gps / global_pick_selector

## posição desta versão
Esta versão substitui a leitura mais minimal da v1 para materialização do bloco de produto.

## ponto de entrada
- shortlist ordenada já produzida pelo GPS

## ponto de saída
- `contracts/gps_shortlist_product_v2.json`
- `examples/shortlist_product_output_example.json`

## campos mínimos visíveis
- pick_id
- module_name
- match_label
- market_code
- selection_label
- rank_position
- rationale_short
- shortlist_level

## regra de produto
- `primary` = pick principal
- `secondary` = pick secundária
- `watchlist` = watchlist
- `rejected` fica fora do bloco principal

## destino final pretendido
- Orchestrator / App Core
- UI / Frontend
