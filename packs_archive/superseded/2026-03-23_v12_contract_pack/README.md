# v12 Contract Pack — 2026-03-23

## Objetivo do pack
Entregar a base atual do motor v12 Over/Under em formato de migração, com outputs alinhados ao Contrato Transversal de Integração SignalBet v1.1 Operacional, para teste controlado fora de `modules/`.

## Ficheiros principais
- `motor/v12_sandbox.py` — ponto de entrada da sandbox v12
- `motor/core/` — lógica de dados, indicadores, probabilidade, value, decisão, comparação e explicação
- `motor/models/` — modelos base do módulo
- `outputs/` — exemplos de payload oficial v12 em schema contratual
- `integration/V12_TO_CONTRACT_V1_1_MAPPING.md` — mapeamento do output v12 para o contrato
- `integration/V12_PAYLOAD_TEMPLATE.json` — template oficial reutilizável da pick candidata v12

## Dependências
- Python embeddable compatível com a app portátil
- ficheiro `api.env.txt` na raiz do módulo, com formato `API_KEY=...`
- dados locais em `motor/data/`

## Destino final pretendido
Integração futura na árvore do módulo v12, após validação contratual e adaptação da camada de saída para Opportunity Pool / Global Pick Selector.

## Estado
`teste`
