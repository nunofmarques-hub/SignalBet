# Prova real

Este pack continua preparado para correr em modo de prova real.

## Ordem de resolução do project_root
1. argumento de `run_real_proof.py`
2. variável `SIGNALBET_PROJECT_ROOT`
3. `examples/req/project_root.txt`
4. fallback demo do pack

## Regra
Na prova real, se o root real não estiver disponível ou se não forem detetados feeds reais válidos de módulos, a corrida falha com gates explícitos.

## Discovery oficial dos feeds
A discovery oficial fica congelada nesta ordem:

1. `integration_feeds/<module>/latest.json`
2. `integration_feeds/<module>/<module>_output.json`
3. `integration_feeds/<module>/module_output.json`
4. `integration_feeds/<module>/output.json`

Só depois são permitidos fallbacks secundários, incluindo `runtime/mod_out`, `mod_out`, `migration_workspace`, `modules/.../out`, `modules/.../examples` e scans recursivos.
