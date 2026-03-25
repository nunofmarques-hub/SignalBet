# Output para Analytics / Audit

## Princípio
A Execution / Tracking é a fonte de verdade do histórico real do sistema.

## O que este output resolve
- comparação approved vs executed
- tracking de missed / cancelled / void
- análise de slippage
- análise de performance por módulo e mercado
- reconciliação operacional

## Regra
Consumidores externos não devem ter de reconstruir manualmente o ledger a partir de várias tabelas. A Execution deve expor uma visão consolidada estável.
