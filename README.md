# SignalBet

SignalBet é o repositório operacional do sistema ABC PRO / SignalBet, focado em:

- análise de mercados de futebol
- seleção global de oportunidades
- gestão de banca e risco
- execution / tracking
- coordenação transversal da app

Este repositório funciona como **espelho cloud oficial** da estrutura viva do projeto, enquanto a máquina física continua a ser a base principal de execução, testes e runtime real.

---

## Estado atual do projeto

Nesta fase, o projeto já tem:

- Data/API Layer oficial consolidada
- corredor central estabilizado:
  - Global Pick Selector
  - Banca / Bankroll & Risk Manager
  - Execution / Tracking
- núcleo analítico principal promovido:
  - Cards
  - v12
  - BTTS
  - Corners
- UI / Frontend em fase seguinte
- App Core / Orchestrator em fase seguinte
- frente de Test Strategy / QA / Promotion Gates oficialmente aberta

---

## Estrutura principal

### `data_api/`
Contém a linha oficial da Data/API Layer.

Objetivo:
- providers oficiais
- services oficiais
- storage raw / snapshots
- collectors prioritários
- base comum de dados para os módulos

A referência ativa nesta fase é:
- `Data_API_Official_Trunk_v1`

---

### `migration_workspace/`
Zona oficial de staging, handoff e promoção de packs.

Objetivo:
- packs em avaliação
- linhas de fecho
- packs `pronto_para_integracao`
- frentes em evolução disciplinada

Aqui vivem os packs dos módulos e das frentes antes de integração formal.

---

### `packs_archive/`
Zona de arquivo de packs antigos, superseded ou apenas mantidos como referência histórica.

Objetivo:
- preservar rasto do projeto
- evitar poluir a linha viva
- manter evidência de evolução sem criar ambiguidade operacional

---

## Leitura operacional do repositório

### Base local
A máquina física continua a ser a base principal para:
- execução real
- smoke tests
- runtime
- integração técnica
- validação sobre a árvore física

### Repositório GitHub
Este repositório serve como:
- espelho cloud oficial
- estrutura viva consultável
- documentação transversal
- contratos
- manifests
- freeze notes
- handoffs

### Project no ChatGPT
Serve como:
- camada de continuidade
- memória operacional
- contexto de decisões
- leitura consolidada do projeto

---

## Estado das principais frentes

### Núcleo analítico
- Cards → `pronto_para_integracao`
- v12 → `pronto_para_integracao`
- BTTS → `pronto_para_integracao`
- Corners → `pronto_para_integracao`

### Corredor central
- Global Pick Selector → linha oficial congelada
- Banca / BRM → linha oficial congelada
- Execution / Tracking → linha oficial congelada

### Frentes seguintes
- UI / Frontend
- App Core / Orchestrator

---

## Regra de leitura do projeto nesta fase

O projeto já não está em fase de desenho.
A fase atual é de:

- consolidação
- promoção disciplinada
- integração
- governação de qualidade
- abertura controlada de novas frentes

---

## Frentes novas já desbloqueadas

Com base no estado atual do projeto, ficam desbloqueadas ou em abertura:

- Test Strategy / QA / Promotion Gates
- Integration Governance / Release Promotion
- Analytics / Audit / Reporting

---

## Convenções recomendadas

### Para packs em `migration_workspace/`
Cada pack deve, idealmente, trazer:
- `README.md`
- `manifest.json`
- `run_smoke.*`
- `pack_check_report.txt`
- `src/`
- `docs/`
- `examples/`
- `contracts/` quando aplicável

### Para promoções de estado
Estados usados no projeto:
- `staging`
- `staging_forte`
- `pronto_para_integracao`
- `integrado`

---

## Nota importante

Este repositório não substitui a execução real local.  
Ele existe para tornar o projeto:

- consultável
- governável
- auditável
- mais fácil de continuar entre frentes, packs e decisões

---

## Situação resumida

O núcleo analítico está promovido.  
O corredor central está congelado.  
A Data/API está consolidada.  
UI e Orchestrator lideram a fase seguinte.  
A governação de promoção e qualidade já entrou oficialmente no projeto.
