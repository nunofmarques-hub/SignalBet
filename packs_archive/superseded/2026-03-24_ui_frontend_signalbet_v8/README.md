# 2026-03-24_ui_frontend_signalbet_v8

## Nome do pack
2026-03-24_ui_frontend_signalbet_v8

## Objetivo do pack
Evoluir a frente UI / Frontend de **staging forte** para **camada de integração-ready staging**, reforçando:
- adapters mais próximos dos outputs reais do Orchestrator
- providers/mock adapters preparados para futura substituição por fontes reais
- painel “Pôr tudo a correr” com estados mais credíveis
- estrutura mais próxima de handoff técnico para a stack frontend definitiva

## Estado do pack
staging

## Módulo / frente
ui_frontend

## Dependências
- Browser moderno com suporte ES modules
- Dados mockados alinhados ao contrato transversal v1.1
- Referência visual da marca SignalBet
- Referência conceptual do `Data_API_Official_Trunk_v1`
- Pipeline central validada em staging forte (Data/API, módulos, GPS, Banca, Execution)

## Ponto de entrada
`src/index.html`

## Ponto de saída
Frontend navegável com 5 ecrãs principais e App Shell real:
- Home / Dashboard
- Opportunity Pool
- Banca / Decision View
- Execution / Tracking
- Histórico / Validação

Inclui painel visual do botão/orchestrator com:
- readiness do sistema
- estado da Data/API
- módulos disponíveis
- progresso da corrida
- resumo final da execução
- estados `idle / running / partial / success / error`
- adaptação visual para checks, fases e output de corrida

## Ligação à Data/API Layer
Este pack **não consome providers reais diretamente**. Usa:
- interfaces de provider estáveis
- providers mockados desacoplados
- adapters mais próximos dos estados do orchestrator
- services intermédios para reduzir acoplamento entre dados e renderização

### Referência oficial ativa
- `provider_name`: `Data_API_Official_Trunk_v1`
- `provider_object`: `ui_v8_provider_interfaces_and_mock_adapters`

### Campos refletidos
- `global_score`
- `confidence_norm`
- `edge_norm`
- `risk_norm`
- `priority_tier`
- `eligibility`
- `decision_status`
- `execution_status`
- `data_quality_flag`

### O que ainda falta para integração completa
- ligação real aos providers oficiais
- consumo de estados reais do App Core / Orchestrator
- sincronização real de banca / execution / histórico
- troca do asset de logo por eventual master asset final de design

## Como correr o smoke test
### Linux / macOS
```bash
./run_smoke.sh
```

### Windows
```bat
run_smoke.bat
```

O smoke test valida a estrutura mínima, a presença dos ficheiros críticos, a nova camada de providers/adapters/services e atualiza o `pack_check_report.txt`.

## Estrutura relevante
- `src/js/providers/` → providers mockados desacoplados e registry
- `src/js/adapters/` → transformação de payloads para shape de UI
- `src/js/services/` → camada de consumo desacoplada da renderização
- `src/js/core/` → store e estado global simples
- `src/js/components/` → componentes reutilizáveis
- `src/js/pages/` → páginas principais
- `contracts/` → notas contratuais e regras de campos

## Notas finais
- Marca principal visível no frontend: **SignalBet**
- ABC PRO permanece como backbone/metodologia interna
- O botão **"Pôr tudo a correr"** continua a ser entrada visual; a coordenação técnica pertence ao App Core / Orchestrator
- O logo SVG incluído é uma aplicação fiel à direção aprovada Radar Focus, adequado para staging e handoff visual
