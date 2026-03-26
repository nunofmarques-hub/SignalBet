# UI Frontend SignalBet v10 — Integration Surface Pack

## Objetivo do pack
Transformar a frente UI de staging forte numa **camada visual oficial preparada para consumir estados reais do sistema** com o mínimo de fricção.

## Estado do pack
staging_forte

## Módulo / frente
UI / Frontend

## Dependências
- Data_API_Official_Trunk_v1 (referência oficial de dados; ainda não consumida diretamente)
- App Core / Orchestrator (fonte futura dos estados reais de corrida; ainda não ligado diretamente)
- Contrato Transversal de Integração v1.1

## Ponto de entrada
- `src/index.html`

## Ponto de saída
- shell navegável com 5 ecrãs
- Integration Surface com providers, adapters, services e view models
- painel visual do botão “Pôr tudo a correr”

## Como lê da Data/API Layer
Este pack **não consome ainda fontes reais**. Usa providers mockados e placeholder providers alinhados ao contrato e aos estados esperados da pipeline.

## Conteúdo principal
- app shell consolidado
- Home / Dashboard
- Opportunity Pool
- Banca / Decision View
- Execution / Tracking
- Histórico / Validação
- Integration Surface (`services/systemSnapshotService.js`, `services/pipelineStatusService.js`)
- View Models por domínio
- painel do Orchestrator com readiness, progresso e resumo

## Contrato v1.1
Referenciado em `contracts/ui_contract_notes.md`.

## Como correr
### Windows
`run_smoke.bat`

### macOS / Linux
`sh run_smoke.sh`

Ou abrir `src/index.html` diretamente no browser.
