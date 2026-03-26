# UI / Frontend — SignalBet — First Staging Pack

## objetivo do pack
Primeiro pack formal da frente **UI / Frontend** para o projeto **SignalBet / ABC PRO**.

Este pack materializa a base visual e funcional da futura app, já alinhada com a arquitetura comum do sistema e com a nova regra de staging em `migration_workspace/`.

O foco deste pack é entregar:
- app shell inicial
- design system base
- 5 ecrãs mockados principais
- documentação de componentes transversais
- mapa de campos por ecrã
- enquadramento claro face ao contrato v1.1 e à Data/API Layer

## estado do pack
`staging`

## dependências
- Contrato Transversal de Integração **v1.1 Operacional**
- Data/API Layer central (`data_api/`) como fonte oficial futura
- Global Pick Selector / Opportunity Pool para a lógica de ranking global
- Bankroll & Risk Manager para decisão operacional
- Execution / Tracking para estados operacionais e audit trail

## ponto de entrada
- Leitura inicial: `README.md`
- Arquitetura base: `docs/app_shell_arquitetura_base.md`
- Design system base: `design_system/ui_design_system_base.md`
- Ecrãs mockados: pasta `mockups/`

## ponto de saída
Este pack serve como base para futura integração em:
- app shell real
- sistema de componentes reutilizáveis
- implementação frontend ligada progressivamente a payloads reais

Destino final esperado, depois de consolidação:
- `modules/` **não aplicável diretamente** nesta fase
- integração posterior na app principal / camada UI oficial do produto

## referência ao contrato v1.1
Este pack foi pensado para representar visualmente campos e estados compatíveis com o contrato operacional transversal v1.1, incluindo nomenclatura e estados como:
- `global_score`
- `confidence_norm`
- `risk_norm`
- `edge_norm`
- `priority_tier`
- `decision_status`
- `execution_status`
- `data_quality_flag`
- `eligibility`

## como lê da Data/API Layer ou o que falta para isso
### estado atual
Este pack **ainda trabalha com dados mockados coerentes** com a arquitetura e com o contrato v1.1.

### leitura futura esperada
A UI deverá consumir dados a partir da **Data/API Layer central**, e não diretamente de APIs externas.

### o que falta para ligação real
- payload oficial estabilizado da Data/API Layer para fixtures, markets e metadata
- output congelado do Global Pick Selector
- payload final GPS -> Banca
- intake formal Banca -> Execution

## conteúdo do pack
- `docs/` — arquitetura, navegação, ecrãs e fluxo funcional
- `design_system/` — base visual, componentes e estados
- `contracts_ui/` — mapa de campos e convenções de integração visual
- `screens/` — documentação resumida por ecrã
- `mockups/` — mockups visuais da linha atual SignalBet

## nota de branding
### frontend / produto visível
**SignalBet**

### camada interna / técnica / documentação estrutural
**ABC PRO**

## nota operacional
Este pack não substitui a implementação final. É um **handeoff de staging** orientado para alinhamento entre UI, arquitetura do sistema e integração futura.
