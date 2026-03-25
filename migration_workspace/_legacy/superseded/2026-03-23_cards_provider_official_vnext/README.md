# Cards — Official Provider vNext Pack

## objetivo do pack
Formalizar o consumo oficial da Data/API Layer para o módulo Cards, com provider explícito, contrato mínimo de input central, pipeline curto, output estável `market_pick.v1.1` e smoke test de ponta curta.

## estado do pack
staging

## dependências
- Python 3.11+
- Sem bibliotecas externas obrigatórias

## ponto de entrada
- `run_cards_official_vnext_demo.py`
- `START_CARDS_OFFICIAL_VNEXT.cmd`

## ponto de saída
- `out/*.json`
- payload oficial do módulo no schema `market_pick.v1.1`

## referência ao contrato v1.1
- Contrato transversal: `market_pick.v1.1`
- O módulo exporta apenas linguagem raw de mercado e `module_specific_payload`

## como lê da Data/API Layer
Leitura prevista a partir de exports oficiais da base central com esta convenção de staging:
- `data_api/exports/cards/*.json`

Neste pack, para demonstrar o handoff sem depender do tronco final da base, os ficheiros de exemplo vivem em:
- `examples/central_inputs/*.json`

O provider explícito está em:
- `providers/official_cards_provider.py`

A função do provider é:
1. carregar o payload central
2. validar campos mínimos de consumo
3. mapear para o handoff interno do motor
4. devolver um input canónico para scoring/elegibilidade/export

## ficheiros principais
- `providers/official_cards_provider.py`
- `providers/contracts.py`
- `src/cards_module/core/orchestrator.py`
- `src/cards_module/core/scoring.py`
- `src/cards_module/core/eligibility.py`
- `src/cards_module/io/exporter.py`
- `src/cards_module/io/validator.py`
- `examples/central_inputs/*.json`
- `tests/test_short_pipeline.py`

## destino final pretendido
`modules/cards/`

## notas
Este pack já prova consumo oficial via provider explícito, mas continua em staging até a Data/API Layer congelar o seu tronco de export oficial.
