# CORNERS_SWAP_CLEAN_NOTE

## objetivo
Fechar a revisão curta do pack do Corners para permitir **swap limpo** da linha atual.

## correção aplicada
Foi **reposta a pasta `runtime_inputs/`** nesta revisão do pack.

## motivo
A linha atual de `modules/corners` ainda expõe `runtime_inputs/`. Para evitar ambiguidade entre pasta esquecida, pasta viva ou remoção incompleta, esta revisão preserva a pasta no pack.

## leitura operacional
- o pack fica mais seguro para swap limpo
- `runtime_inputs/` fica tratada como compatibilidade estrutural nesta revisão
- o smoke desta ronda não depende de `runtime_inputs/`
- não há reabertura do motor Corners nem expansão de escopo

## próximo passo possível
Numa ronda futura, a coordenação pode decidir entre:
1. manter `runtime_inputs/` como parte viva da linha oficial;
2. removê-la formalmente com nota explícita de ausência de dependência runtime residual.
