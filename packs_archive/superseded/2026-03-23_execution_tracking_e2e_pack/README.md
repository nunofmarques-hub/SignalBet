# Execution / Tracking — E2E Pack

## Objetivo
Este pack fecha o próximo passo indicado no relatório do chefe: testar intake real e provar um caso ponta a ponta da Execution / Tracking.

## Estado do pack
- estado: staging avançado / quase integrável
- destino atual: `migration_workspace/execution_tracking/2026-03-23_execution_tracking_e2e_pack/`
- destino final: `modules/execution_tracking/`

## Conteúdo
- `handoff/bankroll_case/` → payload realista vindo da Banca
- `intake/test_case/` → validações e caso inválido de controlo
- `state_machine/e2e_flow/` → transições completas do caso
- `settlement/e2e_case/` → payload oficial vindo da Data/API para fecho
- `ledger/final_outputs/` → ledger final em cenários win, missed e void
- `analytics/final_outputs/` → registo pronto para analytics/audit
- `docs/` → notas de integração e pseudofluxo

## O que este pack demonstra
1. intake realista vindo da Banca
2. sequência de estados ponta a ponta
3. settlement com hook de dados oficiais
4. ledger final consolidado
5. output estável para analytics/audit

## Dependências ainda abertas
- payload final oficial da Banca ainda pode sofrer pequenos ajustes de naming
- ligação real à Data/API Layer para settlement ainda depende da implementação da data layer

## Próximo passo recomendado
Transformar este pack em wiring mais executável dentro de `modules/execution_tracking/`, ligando repositories, state machine e services ao payload final da Banca.
