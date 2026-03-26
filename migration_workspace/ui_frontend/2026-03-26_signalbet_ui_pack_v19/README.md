# UI Frontend SignalBet v19

Estado: staging

Objetivo do pack:
- provar reuso efetivo em cenário repetido
- testar refresh protegido e invalidação controlada
- clarificar quando a bridge prefere nova leitura face a snapshot reutilizável
- preservar fallback limpo para `orchestrator_mock`

Ponto de entrada:
- `src/index.html`

Ponto de saída:
- shell navegável com painel do Orchestrator e bridge protegida com política explícita de reuso, refresh e fallback

Dependências:
- browser moderno
- localStorage disponível para persistência do snapshot protegido
- dados mockados locais
- snapshot JSON protegido opcional

Contrato:
- alinhado com o contrato transversal v1.1 e com o runtime do Orchestrator já provado em staging

Leitura Data/API / runtime:
- a UI não consome diretamente a Data/API Layer como motor
- usa runtime bridge, provider protegido e adapters para snapshots do sistema
- mantém fallback limpo para `orchestrator_mock`

Modos disponíveis:
- `contract_mock`
- `orchestrator_mock`
- `real_read_protected`
- `placeholder_live`
