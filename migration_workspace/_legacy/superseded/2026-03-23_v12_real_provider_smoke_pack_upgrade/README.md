# v12 real provider smoke pack upgrade

- **objetivo do pack:** provar leitura mínima real da base central via provider/bridge, validar o adapter da v12, correr smoke test curto e estabilizar output contratual `market_pick.v1.1` para a Opportunity Pool.
- **estado do pack:** `staging`
- **dependências:** Python 3.11+; payload central em shape compatível com `schemas/input_shape_provider_real.json`; contrato `Contrato_Transversal_Integracao_SignalBet_v1_1_Operacional.pdf`; dados centrais mínimos de fixture, standings, stats e odds/fallback.
- **ponto de entrada:** `motor/smoke_test.py`
- **ponto de saída:** `examples/smoke_output_pool.ndjson` e payloads individuais em `examples/smoke_output_*.json`
- **referência ao contrato v1.1:** schema de saída alinhado com `market_pick.v1.1` e regras descritas em `integration/CONTRACT_V1_1_OUTPUT_RULES.md`
- **como lê da Data/API Layer:** via `motor/provider_bridge.py` + `motor/input_adapter.py`; neste pack a leitura é provada com `examples/provider_real_input_sample.json`; para integração real, o provider deve apontar aos providers oficiais em `data_api/` mantendo o mesmo shape.
- **destino final pretendido:** staging em `migration_workspace/v12/` até prova com provider oficial; depois promoção para integração parcial junto da arquitetura comum.

## ficheiros principais
- `motor/provider_bridge.py`
- `motor/input_adapter.py`
- `motor/market_engines.py`
- `motor/contract_output.py`
- `motor/smoke_test.py`
- `schemas/input_shape_provider_real.json`
- `schemas/output_shape_market_pick_v1_1.json`

## validação rápida
1. Abrir `examples/provider_real_input_sample.json` e confirmar shape.
2. Correr `python motor/smoke_test.py` a partir da pasta do pack.
3. Confirmar geração de candidatos para:
   - `TEAM_OVER_15`
   - `MATCH_OVER_15`
   - `MATCH_UNDER_35`
4. Validar que a saída respeita `market_pick.v1.1`.

## o que este pack prova
- leitura em shape central realista
- bridge + adapter funcionais
- fluxo mínimo ponta a ponta
- output v1.1 estável para a Opportunity Pool

## o que ainda falta
- apontar `provider_bridge.py` aos providers oficiais de `data_api/`
- provar leitura sobre dados centrais em runtime do projeto
- ampliar cobertura multi-liga e qualidade real de odds/stats
