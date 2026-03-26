# App Shell — Arquitetura Base

## objetivo
Definir a estrutura estável do frontend do produto SignalBet.

## áreas principais
- Home / Dashboard
- Opportunity Pool
- Módulos
- Banca / Decision View
- Execution / Tracking
- Histórico / Validação
- System / Ops (opcional)

## padrão de navegação recomendado
- sidebar principal fixa
- topbar contextual
- content canvas modular
- detail panel lateral opcional

## lógica do produto
A UI deve expressar o pipeline:

**Data -> Análise -> Seleção -> Banca -> Execução -> Validação**

## regra de produto
A app não deve parecer uma lista de picks. Deve parecer um sistema de decisão modular.
