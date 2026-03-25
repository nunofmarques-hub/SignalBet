# UI Frontend — SignalBet v5

## Objetivo do pack
Evoluir a frente UI / Frontend de staging visual funcional para uma base de frontend mais preparada para handoff técnico e integração futura com a app real.

## Estado do pack
staging

## Módulo / frente
ui_frontend

## Branding
Marca principal visível no frontend: **SignalBet**

Sistema/metodologia interna: **ABC PRO**

## O que este pack entrega
- app shell navegável mais maduro
- design system base utilizável
- componentes com melhor separação lógica
- 5 ecrãs navegáveis
- estados `loading / empty / error`
- ponto de entrada visual do botão **Pôr tudo a correr**
- asset de logo em SVG alinhado com a direção oficial Radar Focus

## Dependências
- Browser moderno com suporte a ES modules
- Sem backend obrigatório nesta fase
- Dados mockados locais coerentes com os contratos do sistema

## Ponto de entrada
- `src/index.html`

## Ponto de saída
- UI shell navegável para staging visual e handoff técnico

## Referência ao contrato v1.1
Este pack usa mock data alinhado com o contrato transversal do sistema e com campos como:
- `global_score`
- `confidence_norm`
- `edge_norm`
- `risk_norm`
- `priority_tier`
- `eligibility`
- `decision_status`
- `execution_status`
- `data_quality_flag`

## Leitura da Data/API Layer
Este pack **não consome diretamente** a `Data_API_Official_Trunk_v1`.

Nesta fase, usa dados mockados coerentes com a arquitetura oficial e com o contrato transversal, preparados para futura substituição por providers reais.

## Estrutura
- `manifest.json`
- `run_smoke.sh`
- `run_smoke.bat`
- `pack_check_report.txt`
- `src/`
- `docs/`
- `examples/`
- `contracts/`
- `data/`

## Como correr
### Opção 1
Abrir `src/index.html` diretamente no browser.

### Opção 2
Servir a pasta com um servidor local simples.

## Ecrãs incluídos
- Home / Dashboard
- Opportunity Pool
- Banca / Decision View
- Execution / Tracking
- Histórico / Validação

## Observações honestas
- O logo SVG incluído é uma aproximação fiel à direção aprovada Radar Focus, mas não substitui um futuro master asset oficial vindo de design.
- O pack ainda é framework-agnostic e serve como base de staging e handoff.
