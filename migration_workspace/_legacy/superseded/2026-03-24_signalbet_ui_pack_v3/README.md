# SignalBet UI Pack v3

## objetivo do pack
Base real implementável de frontend para a frente UI / Frontend do projeto SignalBet / ABC PRO.

## estado do pack
staging

## dependências
- Browser moderno (Chrome, Edge, Firefox)
- Sem build obrigatório nesta fase
- Mock data local coerente com os contratos transversais do sistema

## ponto de entrada
- `index.html`

## ponto de saída
- Navegação entre 5 ecrãs principais:
  - Home
  - Opportunity Pool
  - Banca / Decision View
  - Execution / Tracking
  - Histórico / Validação

## referência ao contrato v1.1
A UI usa mock payloads alinhados com os campos nucleares transversais:
- `global_score`
- `confidence_norm`
- `edge_norm`
- `risk_norm`
- `priority_tier`
- `eligibility`
- `decision_status`
- `execution_status`
- `data_quality_flag`

## ligação à Data/API Layer
Este pack ainda não consome diretamente a `Data_API_Official_Trunk_v1`.

No entanto, os mock data e os estados apresentados foram reorganizados para refletirem a estrutura oficial da base de dados/API e o contrato operacional comum. O objetivo é facilitar a futura substituição do `data/mock-data.js` por adapters reais de leitura.

## o que já está implementado
- app shell real com sidebar e topbar
- design system base utilizável
- componentes nucleares reutilizáveis em JS
- 5 ecrãs navegáveis
- ponto de entrada visual do botão “Pôr tudo a correr”
- estados visuais coerentes entre as áreas

## o que continua mockado
- dados dos módulos
- ranking global
- sizing / exposição
- estado de execution
- validação histórica
- estado do orchestrator

## estrutura
- `index.html` — ponto de entrada
- `assets/styles.css` — design system base
- `assets/app.js` — app shell, router simples e renderização
- `data/mock-data.js` — payloads mockados coerentes com o sistema
- `docs/arquitetura_ui_v3.md` — notas de estrutura
