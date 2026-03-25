# Arquitetura UI v8 — SignalBet

## Objetivo
A v8 aproxima a UI da fase de integração técnica real sem fingir consumo do trunk oficial.

## Saltos principais face ao v7
- introdução de `providerRegistry`
- separação explícita entre provider de contrato e provider de estados do orchestrator
- adapters específicos para estado de corrida
- painel “Pôr tudo a correr” mais próximo de checks, fases, resumo e issues reais
- services mais preparadas para troca futura de providers mockados por fontes reais

## Organização atual
- `providers/` — fontes mockadas e registry
- `adapters/` — transformação de contrato e de estado do orchestrator
- `services/` — composição de modelos de UI
- `core/` — store mínima e estado de UI
- `components/` — layout, ui atoms, state views, cards e tables
- `pages/` — Home, Pool, Banca, Execution, Histórico

## Estado técnico
A UI continua corretamente em staging com dados mockados alinhados ao contrato v1.1.
Não há ligação direta ao `Data_API_Official_Trunk_v1` nem ao App Core / Orchestrator real.

## Preparação para a stack definitiva
A v8 deixa encaminhada a troca futura de providers mockados por fontes reais com impacto menor na renderização, porque a UI consome modelos vindos de services/adapters e não payloads crus nas páginas.
