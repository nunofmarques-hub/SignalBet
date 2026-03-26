# Cards — Official Contract Final Pack

## objetivo do pack
Provar consumo oficial da Data/API Layer pelo módulo Cards através de um provider explícito alinhado ao contrato final de input central, com output do módulo estabilizado em `market_pick.v1.1`, critérios de elegibilidade mais fechados e testes curtos de pipeline.

## estado do pack
staging

## dependências
- Python 3.11+
- Sem bibliotecas externas obrigatórias

## ponto de entrada
- `run_cards_contract_final_demo.py`
- `START_CARDS_CONTRACT_FINAL.cmd`

## ponto de saída
- `out/*.json`
- payload oficial do módulo no schema `market_pick.v1.1`

## referência ao contrato v1.1
- Contrato transversal de integração: `market_pick.v1.1`
- O módulo exporta apenas score/confiança/risco/edge raw, racional, drivers, penalties e `module_specific_payload`

## como lê da Data/API Layer
Este pack assume como origem oficial a base central em `data_api/`.

Fluxo esperado:
1. Data/API Layer gera payload central do mercado em `data_api/exports/cards/*.json`
2. `providers/official_cards_provider.py` carrega e valida o contrato mínimo de input
3. `providers/mappers.py` normaliza o payload para o handoff interno do motor
4. `src/cards_module/core/orchestrator.py` corre scoring, elegibilidade, export e validação

Neste pack, para permitir staging autónomo, os exemplos vivem em:
- `examples/official_base_inputs/*.json`

## ficheiros principais
- `providers/contracts.py`
- `providers/official_cards_provider.py`
- `providers/mappers.py`
- `src/cards_module/core/orchestrator.py`
- `src/cards_module/core/scoring.py`
- `src/cards_module/core/eligibility.py`
- `src/cards_module/io/exporter.py`
- `src/cards_module/io/validator.py`
- `examples/official_base_inputs/*.json`
- `examples/expected_outputs/*.json`
- `tests/test_short_pipeline.py`

## destino final pretendido
`modules/cards/`

## estado da leitura oficial da Data/API Layer
- pack já alinhado ao contrato final de consumo da base
- ainda usa exemplos locais de staging porque o tronco oficial de `data_api/` ainda não foi congelado neste ambiente
- assim que a base oficial estiver fechada, basta trocar a origem física dos ficheiros sem mexer no pipeline do módulo
