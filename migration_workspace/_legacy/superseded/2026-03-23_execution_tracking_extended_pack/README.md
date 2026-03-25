# Execution / Tracking Layer — Extended Core Pack

## Objetivo do pack
Este pack entrega a base estrutural da camada `execution_tracking` do SignalBet / ABC PRO, tratada como **camada única** com subcomponentes internos e não como novos módulos do ecossistema.

## Conteúdo principal
- `intake/` — validação de intake e deduplicação
- `ledger/` — modelos e repositório base da ordem operacional
- `state_machine/` — enums, regras de transição e máquina de estados
- `settlement/` — resolução de settlement e cálculo financeiro
- `audit_feed/` — notas, feed auditável e builders
- `execution/` — registo de tentativas e execução real
- `snapshots/` — congelamento de snapshots
- `reports/` — views consolidadas para ledger, analytics e feedback à banca
- `orchestrator/` — serviço coordenador da camada
- `docs/` — documentação de apoio

## Dependências
- Python 3.11+
- Persistência abstrata (adaptável depois ao storage real do projeto)
- Fonte oficial de fixture/settlement vinda da Data/API Layer

## Destino atual
`migration_workspace/execution_tracking/2026-03-23_execution_tracking_extended_pack/`

## Destino final pretendido
`modules/execution_tracking/`

## Estado
`staging`

## Nota estrutural
Os diretórios deste pack representam **subcomponentes internos da Execution / Tracking Layer**.
Não devem ser promovidos a módulos autónomos do ecossistema.
