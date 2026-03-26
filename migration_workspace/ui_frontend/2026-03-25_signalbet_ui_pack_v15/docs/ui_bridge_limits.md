# UI Bridge Limits

## A bridge atual faz
- leitura protegida parcial
- fallback limpo para `orchestrator_mock`
- metadata de origem observada
- tolerância a falta parcial de campos

## A bridge atual ainda não faz
- live read contínua
- endpoint oficial real do Orchestrator
- substituição integral de todos os mocks
- consumo direto do trunk
