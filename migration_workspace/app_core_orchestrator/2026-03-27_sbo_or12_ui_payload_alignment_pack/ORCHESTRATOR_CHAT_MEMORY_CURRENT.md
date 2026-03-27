# ORCHESTRATOR_CHAT_MEMORY_CURRENT

## feito
- Corrigido patch de snapshot agregado para compatibilidade com OR12.
- Mantido intake nativo do trunk via `load_baseline_state()`.
- Adicionado `ui_runtime_snapshot.json` sem quebrar a linha ativa.

## objetivo
- Fechar o encaixe OR12 -> UI v26 com snapshot agregado e protegido.

## decisão
- O ficheiro oficial agregado para a UI é `ui_runtime_snapshot.json`.
- Não se altera o intake nativo da baseline real.

## estado atual
- Patch compatível pronto.

## bloqueio
- Sem bloqueio no patch.
- Requer apenas substituir os ficheiros certos no OR12.

## próximo passo
- Copiar este patch compatível para a pasta do OR12 e rerun.
