# SignalBet UI Frontend Pack v2

## objetivo do pack
Entregar a primeira base **implementável** de frontend da futura app SignalBet, já com:
- app shell real
- estrutura navegável entre ecrãs
- componentes nucleares reutilizáveis
- 5 ecrãs mockados navegáveis
- ponto de entrada visual do botão **"pôr tudo a correr"**

## estado do pack
staging

## dependências
- navegador moderno (Chrome, Edge, Firefox)
- sem dependências externas obrigatórias

## ponto de entrada
- `index.html`

## ponto de saída
- protótipo frontend navegável em HTML/CSS/JS
- base implementável para futura migração para framework (React/Next, etc.)

## referência ao contrato v1.1
A UI já usa, de forma mockada e consistente, campos transversais alinhados com o contrato operacional v1.1, incluindo:
- `global_score`
- `confidence_norm`
- `edge_norm`
- `risk_norm`
- `priority_tier`
- `eligibility`
- `decision_status`
- `execution_status`
- `data_quality_flag`

## como lê da Data/API Layer
Nesta fase **ainda não lê da Data/API Layer oficial**.

Leitura atual:
- dados mockados em `data/mock-data.js`
- estrutura preparada para substituir os mocks por providers reais da Data/API Layer

## ecrãs incluídos
- Home / Dashboard
- Opportunity Pool
- Banca / Decision View
- Execution / Tracking
- Histórico / Validação

## nota sobre o botão “pôr tudo a correr”
O pack traz o **ponto de entrada visual** do botão na Home.
A lógica real continua a pertencer ao **App Core / Orchestrator**.

## estrutura do pack
- `index.html` — entrypoint do frontend
- `assets/styles.css` — design system base + layout
- `assets/app.js` — navegação, renderização e componentes
- `data/mock-data.js` — payloads mockados coerentes
- `docs/arquitetura_ui_v2.md` — visão curta da estrutura implementável
