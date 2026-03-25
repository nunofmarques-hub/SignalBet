# Prova real

Este pack está preparado para correr em modo de prova real.

## Ordem de resolução do project_root
1. argumento de `run_real_proof.py`
2. variável `SIGNALBET_PROJECT_ROOT`
3. `examples/req/project_root.txt`
4. fallback demo do pack

## Regra
Na prova real, se o root real não estiver disponível ou se não forem detetados feeds reais de módulos, a corrida falha com gates explícitos.
