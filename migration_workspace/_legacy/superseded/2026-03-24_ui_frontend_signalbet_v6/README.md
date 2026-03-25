# 2026-03-24_ui_frontend_signalbet_v6

## Nome do pack
2026-03-24_ui_frontend_signalbet_v6

## Objetivo do pack
Evoluir a frente UI / Frontend de shell navegável forte para base visual séria da app principal SignalBet, com app shell mais real, estados visuais completos, componentes reutilizáveis, 5 ecrãs navegáveis e ponto de entrada visual do botão **"Pôr tudo a correr"**.

## Estado do pack
staging

## Módulo / frente
ui_frontend

## Dependências
- Browser moderno com suporte ES modules
- Dados mockados alinhados ao contrato transversal v1.1
- Referência visual da marca SignalBet
- Referência conceptual do `Data_API_Official_Trunk_v1`

## Ponto de entrada
`src/index.html`

## Ponto de saída
Shell navegável de frontend com 5 ecrãs principais:
- Home / Dashboard
- Opportunity Pool
- Banca / Decision View
- Execution / Tracking
- Histórico / Validação

Inclui ainda painel visual do botão/orchestrator com:
- readiness do sistema
- estado da Data/API
- módulos disponíveis
- progresso da corrida
- resumo final da execução

## Ligação à Data/API Layer
Este pack **não consome providers reais diretamente**. Usa payloads mockados coerentes com os contratos do sistema e alinhados conceptualmente com a referência oficial ativa:
- provider oficial de referência: `Data_API_Official_Trunk_v1`
- consumo atual da UI: `contract-aligned mock payloads`
- campos obrigatórios refletidos: `global_score`, `confidence_norm`, `edge_norm`, `risk_norm`, `priority_tier`, `eligibility`, `decision_status`, `execution_status`, `data_quality_flag`

### O que ainda falta para integração completa
- ligação real aos providers oficiais e/ou camada app backend/frontend final
- atualização dinâmica dos estados de corrida do orchestrator
- ligação direta a dados de banca, execution e histórico reais

## Como correr o smoke test
### Linux / macOS
```bash
./run_smoke.sh
```

### Windows
```bat
run_smoke.bat
```

O smoke test valida a estrutura mínima, a presença dos ficheiros críticos e atualiza o `pack_check_report.txt`.

## Notas finais
- Marca principal visível no frontend: **SignalBet**
- ABC PRO fica tratado como backbone/metodologia interna, não como branding principal do produto
- O botão **"Pôr tudo a correr"** é apenas ponto de entrada visual; a coordenação técnica continua a pertencer ao App Core / Orchestrator
