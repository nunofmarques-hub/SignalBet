# Arquitetura UI v7

## Objetivo
Preparar a frente UI / Frontend para handoff técnico real, mantendo a honestidade técnica: sem consumo direto do trunk ainda, mas com modularização e adapters mais próximos da pipeline real.

## Evoluções face ao v6
- providers mockados separados de adapters
- services desacoplados da renderização
- store mínima para estado da UI e seleção de linhas
- painel do orchestrator com estados `idle / running / partial / success / error`
- componentes de tabela separados por domínio
- seleção contextual em Pool / Banca / Execution / Histórico

## Camadas
- `providers/` → origem mockada próxima da pipeline
- `adapters/` → normalização de shape para a UI
- `services/` → API interna da interface
- `core/` → store mínima e estado transversal
- `components/` → layout, cards, tabelas, states, primitives
- `pages/` → composição final dos ecrãs

## Nota técnica
A substituição futura para providers reais deve ocorrer primeiro em `providers/` e `services/`, preservando páginas e componentes o máximo possível.
