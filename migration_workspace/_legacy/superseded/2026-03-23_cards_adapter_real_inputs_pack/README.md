# Cards Adapter Real Inputs Pack

## Objetivo do pack
Pack de pré-integração (`staging`) do módulo Cards para validar a ligação explícita à Data/API Layer, correr o motor com inputs centrais realistas e produzir output oficial no contrato `market_pick.v1.1`.

## Ficheiros principais
- `src/cards_module/io/data_layer_adapter.py` — adapter Data/API Layer -> input interno do motor
- `src/cards_module/core/orchestrator.py` — fluxo principal do módulo
- `src/cards_module/core/scoring.py` — scoring disciplinar inicial por blocos
- `src/cards_module/core/eligibility.py` — critérios de elegibilidade mais fechados
- `src/cards_module/io/exporter.py` — export oficial para Opportunity Pool
- `src/cards_module/io/validator.py` — validação mínima do payload final
- `examples/real_inputs/*.json` — exemplos de payload central realista
- `examples/expected_outputs/*.json` — outputs esperados do módulo
- `tests/test_smoke.py` — testes mínimos de ponta curta
- `run_cards_real_inputs_demo.py` — demo local
- `START_CARDS_REAL_INPUTS_SANDBOX.cmd` — arranque rápido em Windows

## Dependências
- Python 3.10+
- Apenas standard library

## Destino final pretendido
- Destino agora: `migration_workspace/cards/2026-03-23_cards_adapter_real_inputs_pack/`
- Destino final: `modules/cards/`

## Estado
`staging`
