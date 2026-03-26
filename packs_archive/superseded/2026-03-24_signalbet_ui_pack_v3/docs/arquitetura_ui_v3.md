# Arquitetura UI v3

## foco
Passar de documentação/mockups para shell navegável da app.

## princípios
- marca visível: SignalBet
- backend interno / sistema: ABC PRO
- app shell desktop-first
- ecrãs baseados na arquitetura oficial do sistema
- componentes comuns e reutilizáveis
- mock data coerente com os contratos

## componentes nucleares já usados
- KPI tile
- score badge
- status chip
- table block
- filter bar
- detail panel
- action button principal

## ponto de entrada visual do botão/orchestrator
Na topbar existe um botão **Pôr tudo a correr** que representa o ponto de entrada visual do App Core / Orchestrator.
A UI apenas representa o entry point. A lógica do fluxo pertence a outra frente.
