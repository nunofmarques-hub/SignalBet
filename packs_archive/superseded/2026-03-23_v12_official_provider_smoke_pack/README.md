# v12 official provider smoke pack

- **objetivo do pack:** provar leitura real da Data/API oficial através de provider oficial/bridge, correr smoke test curto e estabilizar output contratual `market_pick.v1.1` para a Opportunity Pool.
- **estado do pack:** `staging`
- **dependências:** Python 3.11+; provider oficial da `data_api/`; contrato `Contrato_Transversal_Integracao_SignalBet_v1_1_Operacional.pdf`; dados centrais mínimos de fixture, standings, stats e odds/fallback.
- **ponto de entrada:** `motor/smoke_test.py`
- **ponto de saída:** `examples/smoke_output_pool.ndjson` e payloads individuais em `examples/smoke_output_*.json`
- **referência ao contrato v1.1:** schema de saída alinhado com `market_pick.v1.1` e regras descritas em `integration/CONTRACT_V1_1_OUTPUT_RULES.md`
- **como lê da Data/API Layer:** via `motor/provider_bridge.py` + `motor/input_adapter.py`. O bridge tenta primeiro ler um payload oficial em `data_api/exports/v12/provider_official_fixture_878317.json` (ou no path indicado pela variável `V12_PROVIDER_SAMPLE`). Se esse ficheiro não existir, o smoke test pode cair para `examples/provider_official_input_sample.json` apenas como fallback de staging.
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
1. Garantir que existe um payload oficial em `data_api/exports/v12/provider_official_fixture_878317.json`, ou definir `V12_PROVIDER_SAMPLE` para o ficheiro oficial equivalente.
2. Correr `python motor/smoke_test.py` a partir da pasta do pack.
3. Confirmar geração de candidatos para:
   - `TEAM_OVER_15`
   - `MATCH_OVER_15`
   - `MATCH_UNDER_35`
4. Validar que a saída respeita `market_pick.v1.1`.

## o que este pack prova
- leitura real da base central quando o ficheiro oficial estiver disponível
- bridge + adapter funcionais
- fluxo mínimo ponta a ponta
- output v1.1 estável para a Opportunity Pool

## o que ainda falta
- apontar o bridge ao provider definitivo em runtime do projeto, se o path oficial mudar
- ampliar cobertura multi-liga e qualidade real de odds/stats
- trocar fallback de staging por consumo 100% oficial em todos os cenários
