# UI Frontend SignalBet v18

Estado: staging

Objetivo do pack:
- provar consumo parcial de fonte real protegida com reuso efetivo
- testar freshness e invalidação controlada
- clarificar a fronteira entre leitura nova protegida e snapshot reutilizado
- preservar fallback limpo para `orchestrator_mock`

Ponto de entrada:
- `src/index.html`

Ponto de saída:
- shell navegável com painel do Orchestrator e bridge protegida com persistência controlada

Dependências:
- browser moderno
- localStorage disponível para persistência do snapshot protegido
- dados mockados locais
- snapshot JSON protegido opcional

Contrato:
- alinhado com o contrato transversal v1.1 e com o runtime do Orchestrator já provado em staging

Leitura Data/API / runtime:
- a UI não consome diretamente a Data/API Layer como motor
- usa runtime bridge e adapters para snapshots de sistema
- mantém fallback limpo para `orchestrator_mock`

Modos disponíveis:
- `contract_mock`
- `orchestrator_mock`
- `real_read_protected`
- `placeholder_live`
