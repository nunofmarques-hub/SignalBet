# Execution / Tracking — Operational Flow Pack

## Objetivo do pack
Provar o fluxo operacional real da Execution / Tracking a partir de um handoff vindo da Banca, com intake testado, state flow ponta a ponta, settlement com payload de fixture em formato-alvo e output formal para analytics/audit.

## Estado do pack
staging

## Dependências
- Banca / Bankroll & Risk Manager: payload de handoff aprovado
- Data/API Layer: payload oficial de fixture para settlement ainda por congelar
- Contrato Transversal de Integração SignalBet v1.1

## Ponto de entrada
`handoff/bankroll_real_case/bankroll_handoff_real_case_v1.json`

## Ponto de saída
- `ledger/final_real_outputs/execution_ledger_settled_win_v1.json`
- `analytics/final_real_outputs/execution_analytics_output_settled_win_v1.json`

## Referência ao contrato v1.1
Este pack segue o Contrato Transversal de Integração SignalBet v1.1 como referência operacional e mantém a Execution como fonte de verdade do histórico real.

## Leitura da Data/API Layer
Este pack ainda **não lê diretamente** da `data_api/` porque a frente Data/API ainda não congelou o payload oficial de fixture para settlement da Execution. Por isso, o ficheiro em `settlement/fixture_real_payload/` deve ser tratado como **payload-alvo de integração**, já desenhado para encaixar no futuro hook oficial.

## Conteúdo do pack
- `handoff/` caso real vindo da Banca
- `intake/` casos de teste de intake
- `state_machine/` fluxo ponta a ponta
- `settlement/` payload-alvo de fixture para settlement
- `ledger/` outputs finais do ledger
- `analytics/` output formal para analytics/audit
- `docs/` notas de integração e teste

## Destino atual
`migration_workspace/execution_tracking/2026-03-23_execution_tracking_operational_flow_pack/`

## Destino final pretendido
`modules/execution_tracking/`
