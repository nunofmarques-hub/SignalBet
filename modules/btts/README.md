# README.md

## objetivo do pack
Manter a linha oficial ativa do módulo BTTS limpa e alinhada com a app phase 1, fechando a entrega curta de `game_cards` para consumo pelo Orchestrator.

## estado do pack
integrado

## dependências
- Python 3.11+
- `Data_API_Official_Trunk_v1`
- corredor central protegido via Orchestrator / App Core
- contrato transversal do módulo preservado

## ponto de entrada
`src/btts/run_minimal_flow.py`

## ponto de saída desta ronda
`latest.json`

## saída curta desta fase
`game_cards` curtos do BTTS para a app phase 1.

## regra desta ronda
- sem odd justa
- sem edge final
- sem blocos internos do motor
- sem payload rico

## linha oficial ativa
Esta linha fica limpa e alinhada com a leitura curta da app phase 1.

## destino final pretendido
`modules/btts/`
