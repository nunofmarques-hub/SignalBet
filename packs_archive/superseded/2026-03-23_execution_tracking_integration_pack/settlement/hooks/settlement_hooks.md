# Settlement hooks — contrato esperado da Data/API Layer

## Objetivo
Fornecer à Execution os dados mínimos oficiais para fecho operacional e settlement.

## Pré-condições para settlement
- a ordem deve estar em `AWAITING_SETTLEMENT` ou `EXECUTED`
- o fixture deve vir marcado como final (`is_final=true`) ou explicitamente cancelado/abandonado/postponed
- a Execution não fecha settlement sem payload oficial da Data/API Layer

## Estados de fixture e comportamento esperado
- `FT`, `AET`, `PEN` → elegível para resolução normal do mercado
- `CANC` → settlement tende para `VOID`
- `PST` → manter pendente ou route to manual review operacional
- `ABD` → `VOID` ou manual review, conforme regra do mercado
- `AWD`, `WO` → exigir política explícita de mapeamento

## Campos mínimos necessários
- `fixture_status`
- `fixture_status_detail`
- `is_final`
- `result_timestamp`
- dados suficientes para resolver o mercado (ex.: golos finais)

## Hooks internos esperados
- `can_settle(execution_order, fixture_payload)`
- `map_fixture_to_settlement_flow(fixture_payload)`
- `resolve_market_result(execution_order, fixture_payload)`
- `build_settlement_record(execution_order, settlement_status)`
