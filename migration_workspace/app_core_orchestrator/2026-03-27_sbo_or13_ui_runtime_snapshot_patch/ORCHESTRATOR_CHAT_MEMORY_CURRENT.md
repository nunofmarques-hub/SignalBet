# ORCHESTRATOR_CHAT_MEMORY_CURRENT

## feito
- Criado patch OR13 para gerar `ui_runtime_snapshot.json`.
- Mantido OR12 como linha ativa.
- UI passa a poder ler um snapshot agregado único.

## objetivo
- Fechar o encaixe direto entre OR12 e UI v26 sem bridge paralela.

## decisão
- O ficheiro oficial agregado para a UI passa a ser `ui_runtime_snapshot.json`.

## estado atual
- Patch pronto e smoke OK.

## bloqueio
- Sem bloqueio nesta ronda do patch.

## próximo passo
- Integrar o ficheiro agregado no runtime real do OR12 e validar na UI.
