# README.md

## objetivo do pack
Consolidar o handoff oficial do módulo BTTS com a Data/API Layer central, mostrando provider/loader oficial, sample input, fluxo mínimo executável e output formal estável em `market_pick.v1.1`.

## estado do pack
staging

## dependências
- Python 3.11+
- Contrato transversal de integração SignalBet v1.1 operacional
- Payload da Data/API Layer compatível com `sample_input/official_data_api_input.json`

## ponto de entrada
`src/btts/run_minimal_flow.py`

## ponto de saída
`sample_output/market_pick_v1_1_btts.json`

## referência ao contrato v1.1
O output deste pack segue o envelope `market_pick.v1.1` para a Opportunity Pool.

## como lê da Data/API Layer
Lê um payload oficial por evento com:
- contexto do jogo
- snapshots por equipa
- odds
- metadados de qualidade
- sinais temporais mínimos do jogo

Se faltarem campos opcionais, o módulo continua com fallbacks e regista isso no output.

## destino final pretendido
`modules/btts/`
