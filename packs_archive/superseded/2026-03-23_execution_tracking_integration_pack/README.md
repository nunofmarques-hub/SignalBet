# Execution / Tracking — Integration Pack

## Objetivo do pack
Fechar a fronteira real de integração da Execution / Tracking Layer com:
- a Banca / Bankroll & Risk Manager, na entrada de ordens aprovadas
- a Data/API Layer, no settlement e fecho operacional
- a camada de Analytics / Audit, na exportação do histórico real

## Estado do pack
- estado: staging
- maturidade: alta em estrutura / média em integração
- destino atual: `migration_workspace/execution_tracking/2026-03-23_execution_tracking_integration_pack/`
- destino final pretendido: `modules/execution_tracking/`

## Conteúdo principal
- `intake/schema_final/` → schema final de handoff vindo da Banca
- `state_machine/transitions_final/` → transições finais, regras de bloqueio e reason codes por fluxo
- `settlement/hooks/` → contrato de input esperado da Data/API Layer para settlement
- `ledger/examples/` → exemplos reais ponta a ponta do ledger operacional
- `audit_feed/output_contracts/` → payload estável para analytics / audit
- `docs/` → notas operacionais e contrato formal de referência

## Dependências externas do pack
### 1. Banca / Bankroll & Risk Manager
A Execution só aceita ordens com `source_system=BANKROLL_RISK_MANAGER` e `decision_status=APPROVED`.

### 2. Data/API Layer
A Execution precisa de payload oficial de fixture settlement para fechar:
- fixture status final
- score final / contexto necessário ao mercado
- timestamps oficiais de fecho
- flags de cancelamento / abandono / adiamento

### 3. Global Pick Selector
Sem dependência de ordem direta. Apenas contexto congelado para auditabilidade.

## O que este pack fecha
- schema final de intake
- state transitions finais v1
- settlement hooks esperados da Data/API
- exemplo de ledger real
- output estável para analytics/audit
- README de integração com a Banca

## O que ainda fica pendente após este pack
- handoff real da Banca em ambiente de integração
- mapping real da Data/API por tipo de mercado
- wiring persistente e repositories de produção
- reconciliação avançada e partial execution
