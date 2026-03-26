# v12 real provider smoke pack

- **objetivo do pack:** provar fluxo mínimo real da v12 com leitura vinda de provider da Data/API Layer, adapter ativo, smoke test e output contratual v1.1 estável.
- **ficheiros principais:** `motor/provider_bridge.py`, `motor/input_adapter.py`, `motor/smoke_test.py`, `motor/contract_output.py`, `examples/provider_real_input_sample.json`.
- **dependências:** Python 3.11+, payload central com shape compatível, sem dependências externas obrigatórias.
- **destino final pretendido:** `migration_workspace/v12/` antes de integração parcial no ecossistema SignalBet.
- **estado:** `staging`

## Como validar rapidamente
1. Confirmar o sample de entrada em `examples/provider_real_input_sample.json`.
2. Correr `python motor/smoke_test.py` a partir da pasta do pack.
3. Validar que saem 3 candidatos v12 em schema `market_pick.v1.1`.
4. Confirmar estabilidade de campos obrigatórios e enums.

## O que este pack prova
- bridge para provider real em shape central
- adapter funcional
- fluxo mínimo ponta a ponta
- output v1.1 estável

## O que ainda não prova
- cobertura multi-liga larga
- provider central definitivo em produção
- odds reais multi-bookmaker em volume
