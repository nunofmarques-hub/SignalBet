# SUCCESS_CRITERIA

A v1.1.3 fica validada quando:

- há mais do que 1 fixture no snapshot final
- os runs se mantêm green ou controlados
- a forma do snapshot se mantém consistente
- o Orchestrator se mantém estável
- os logs continuam curtos e legíveis

## Classificação final
- `green`: cobertura > 1 fixture e runs estáveis
- `red_coverage`: bootstrap ok, mas cobertura insuficiente
- `red_bootstrap`: falha de inicialização ou descoberta do entrypoint oficial
