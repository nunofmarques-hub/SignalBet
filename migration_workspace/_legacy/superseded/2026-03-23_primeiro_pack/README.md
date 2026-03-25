# App Core / Orchestrator — Primeiro Pack de Staging

## Missão
Construir a camada transversal da app principal que coordena a corrida ponta a ponta: valida ambiente, confirma readiness da Data/API Layer, corre módulos elegíveis, agrega no Global Pick Selector, envia shortlist à Banca, regista na Execution / Tracking e devolve estado claro à UI.

## Estado do pack
`staging`

## Objetivo deste pack
Fechar a primeira base operacional do botão **"pôr tudo a correr"** com:
- fluxo operacional v1
- health checks base
- draft do launcher/orchestrator
- integração conceptual com UI
- ordem oficial do pipeline

## Princípios
- coordena, não recalcula
- UI mostra o botão; Orchestrator governa o fluxo
- resposta orientada a estado, logs e auditoria
- simplicidade, auditabilidade e disciplina acima de complexidade gratuita

## Dependências
- `data_api/` funcional
- módulos elegíveis com contrato mínimo
- GPS disponível
- Banca disponível
- Execution / Tracking disponível

## Entrada
`run_request`

## Saída
`run_summary`, `health_report`, `ui_status`

## Estrutura
Este pack vive em staging e prepara a futura integração da frente transversal `app_core / launcher / orchestrator`.

## Próximo passo esperado
Transformar os drafts, contracts e manifests deste pack num fluxo mínimo executável com `validation_run` real.
