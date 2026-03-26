# Limitações remanescentes — Iteração 2 curta

- O contexto do Orchestrator já entra por artefactos runtime do `sbo9/out`, o que melhora a ancoragem do `run_summary.json`.
- Mesmo assim, esta frente ainda não consome um feed dedicado próprio do Orchestrator; consolida artefactos já emitidos pelo pack vivo.
- O segundo audit trace prova uma linha pré-execution bloqueada, mas a cobertura de casos ainda é curta por desenho desta iteração.
- O reporting continua deliberadamente leve e textual; não há camada visual nesta fase.
