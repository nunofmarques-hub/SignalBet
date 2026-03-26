# UI Snapshot Invalidation Rules

## Objetivo
Clarificar quando um snapshot protegido deve continuar reutilizável e quando deve ser tratado como inválido.

## No v18
- snapshot stale pode continuar reutilizável de forma controlada
- a UI tenta nova leitura protegida antes de cair para fallback
- se a nova leitura falhar, o snapshot stale pode continuar a ser usado sem quebrar a UX

## Ainda não faz
- invalidação dura automática com fonte live real
- revogação por hash/versão de runtime
- invalidation policy baseada em endpoint real
