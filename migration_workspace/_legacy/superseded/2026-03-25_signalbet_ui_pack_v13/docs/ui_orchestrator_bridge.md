# Ponte UI ↔ Orchestrator

## Modos de fonte
- contract_mock
- orchestrator_mock
- placeholder_live

## Situação atual
A UI não liga ao Orchestrator real. Usa snapshots mockados e snapshots protegidos do tipo placeholder_live.

## Objetivo do v13
- reduzir diferença entre mock snapshot e snapshot real esperado
- permitir teste controlado de leitura protegida
- manter fallback sem rebentar a UI
