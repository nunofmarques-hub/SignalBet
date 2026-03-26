# UI Snapshot Freshness Policy

## Objetivo
Definir como a UI classifica freshness do snapshot protegido.

## Estados
- `fresh`: snapshot recente e reutilizável sem revalidação imediata
- `stale`: snapshot reutilizável temporariamente, mas a aguardar nova leitura protegida
- `invalidated`: snapshot já não deve ser reutilizado

## Política atual
- até 15 minutos: `fresh`
- acima de 15 minutos: `stale`
- invalidação completa ainda depende de regra futura mais forte

## Nota
O v18 continua em staging e usa esta política como base controlada, não como política final de produção.
