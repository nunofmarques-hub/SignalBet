# Cards Official Provider Pack

## Objetivo do pack
Formalizar o consumo oficial da base central pelo módulo Cards, com provider explícito, pipeline curto e output oficial estável em `market_pick.v1.1`.

## Ficheiros principais
- `providers/central_cards_provider.py` — provider explícito da base central
- `providers/contracts.py` — contrato esperado do input central
- `providers/mappers.py` — handoff base -> motor
- `src/cards_module/core/orchestrator.py` — pipeline curto do módulo
- `src/cards_module/core/scoring.py` — scoring base do motor
- `src/cards_module/core/eligibility.py` — critérios de elegibilidade
- `src/cards_module/io/validator.py` — validação do output oficial
- `run_cards_official_provider_demo.py` — demo principal
- `tests/test_short_pipeline.py` — testes mínimos de ponta curta

## Dependências
- Python 3.10+
- Apenas biblioteca standard

## Destino final pretendido
- Destino agora: `migration_workspace/cards/2026-03-23_cards_official_provider_pack/`
- Destino final: `modules/cards/`

## Estado
`staging`
