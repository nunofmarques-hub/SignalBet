# Controlled Runtime Read Bridge

## O que já existe
- `runtimeBridgeService.js` centraliza leitura protegida do runtime
- `providerRegistry` escolhe origem por source mode
- `orchestratorAdapters.js` normaliza shape e faltas

## O que ainda não existe
- live read real
- autenticação
- integração com trunk/orchestrator runtime

## Próximo ponto de ligação
Trocar `placeholder_live` por provider controlado de leitura real quando o adapter certo existir.
