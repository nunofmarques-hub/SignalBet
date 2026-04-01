# Nota curta de runtime — emissão do primeiro payload protegido real para o Corners

## emissão
O Orchestrator emite 1 payload protegido real mínimo para o primeiro ensaio curto do Corners.

## ficheiro emitido
- `protected_runtime_payload_corners.json`

## origem
- camada protegida do Orchestrator
- sem ligação direta do Corners ao trunk
- sem provider real direto dentro do Corners

## provider observado
- `fixtures_provider.py`

## readiness observado
- `real_ready`

## source_mode observado
- `project`

## observed_mode observado
- `orchestrator_real_protected`

## estado da emissão
- payload emitido em estado limpo
- sem degradação nesta emissão

## contexto escolhido
- `fixture_id = 1208499`
- `league_id = 140`
- `season = 2024`
- `home_team = Valencia`
- `away_team = Barcelona`

## destino recomendado para ensaio curto do Corners
- `SignalBet\modules\corners\runtime_inputs\protected_runtime_payload_corners.json`

## leitura operacional
Este payload não é integração total do Corners.
É o primeiro input real protegido para ensaio curto, emitido pelo corredor central e pronto para consumo do módulo.
