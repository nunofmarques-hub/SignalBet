# Arquitetura UI v18

O v18 foca na primeira prova parcial de consumo de fonte real protegida com reuso efetivo.

## Eixos principais
- runtimeBridgeService mais rigoroso na decisão entre nova leitura, reuso e fallback
- realOrchestratorProtectedProvider com persistência local reutilizável
- orchestratorAdapters com leitura mais rica de freshness, invalidação e reuso
- painel do Orchestrator com visibilidade explícita sobre a origem e o estado do snapshot

## Resultado
A UI mantém-se em staging, mas já diferencia com mais clareza:
- leitura nova protegida
- snapshot reutilizado
- freshness
- invalidação
- fallback
