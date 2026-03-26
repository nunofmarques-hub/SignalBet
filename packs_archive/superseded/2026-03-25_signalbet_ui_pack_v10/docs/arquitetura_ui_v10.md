# Arquitetura UI v10

## Objetivo
Fechar a UI como Integration Surface oficial em staging forte.

## Camadas
- providers
- adapters
- services
- viewmodels
- components
- pages

## Services principais
- systemSnapshotService
- pipelineStatusService
- uiDataService

## View Models
- homeViewModel
- poolViewModel
- bankrollViewModel
- executionViewModel
- historyViewModel

## Nota
Continua a usar mock data alinhada ao contrato. Não existe ligação real ao trunk nem ao orchestrator.
