# Arquitetura UI v5

## Objetivo desta ronda
Evoluir de shell navegável forte para base de frontend mais preparada para integração futura.

## Melhorias desta versão
- estados `loading / empty / error`
- separação de componentes em módulos JS
- asset SVG de logo mais fiel à direção oficial
- páginas renderizadas por função do sistema
- dados mockados isolados do código de UI

## Páginas
- Home
- Opportunity Pool
- Banca
- Execution
- Histórico

## Componentes base
- Sidebar
- Topbar
- KPI Tiles
- Status Chips
- Score Pills
- Tables
- Panels
- State Blocks

## Integração conceptual com o orchestrator
A UI expõe um botão visual **Pôr tudo a correr** no App Shell.
A lógica real pertence ao App Core / Orchestrator.
