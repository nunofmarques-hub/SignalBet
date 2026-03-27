# SUCCESS_CRITERIA

A fase corre bem se:
- há mais do que 1 fixture no snapshot
- o run não quebra a pipeline
- os modos green/degraded_run/hard_fail são distinguíveis
- o snapshot mantém estrutura estável entre runs
- os logs deixam o comportamento legível
- o Orchestrator continua a consumir sem ambiguidade
