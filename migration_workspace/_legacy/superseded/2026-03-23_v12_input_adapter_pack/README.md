# v12 input adapter pack

## Objetivo do pack
Fechar a transição da v12 da leitura local/sandbox para consumo da futura Data/API Layer central, mantendo output oficial no contrato `market_pick.v1.1`.

## Ficheiros principais
- `motor/input_adapter.py` — adapta o payload central à shape interna da v12.
- `motor/contract_output.py` — constrói o payload oficial v1.1 para a Opportunity Pool.
- `motor/market_engines.py` — documenta os 3 motores ativos do núcleo.
- `examples/sample_input_from_data_layer.json` — exemplo de input vindo da camada central.
- `examples/sample_output_*.json` — exemplos de output contratual para O15_TEAM, O15_GAME e U35.
- `integration/DATA_REQUIREMENTS_V12.md` — dependências de dados reais que a v12 precisa.
- `integration/SANDBOX_TO_CENTRAL_MIGRATION_NOTE.md` — nota de migração sandbox -> leitura central.

## Dependências
- Python 3.11+ (sem dependências externas obrigatórias neste pack)
- Payload central já normalizado pela Data/API Layer
- Contrato `market_pick.v1.1`

## Destino final pretendido
Leitura central da Data/API Layer + emissão contratual da v12 para a Opportunity Pool.

## Estado
`staging`
