# Real Data Calibration & Reliability Phase — v1.1.1

Esta iteração corrige dois problemas de bootstrap observados na v1.1:

1. descoberta demasiado rígida do `fixtures_provider.py`
2. erro de escaping no `run_calibration.cmd` por causa do caractere `&`

## Objetivo
Manter a mesma base técnica e melhorar apenas a robustez de arranque e a cobertura do cenário:

- mesmo provider oficial
- mesmo trunk oficial
- mesmo consumidor principal: Orchestrator
- mesmo modelo de snapshot e logging
- ajuste apenas de cobertura multi-fixture real

## O que mudou na v1.1.1
- provider discovery agora tenta:
  - caminhos conhecidos
  - procura recursiva por `fixtures_provider.py`
  - procura recursiva por qualquer `.py` que contenha `get_fixtures_by_league_season`
- o snapshot e os logs passam a incluir `provider_path`
- o bootstrap falhado sai como `red_bootstrap`
- cobertura insuficiente sai como `red_coverage`
- o `.cmd` foi corrigido para não partir por causa do `&`

## Execução
No Windows:
```bat
run_calibration.cmd
```

Se o trunk estiver noutro caminho:
```bat
set SIGNALBET_TRUNK_ROOT=C:\caminho\para\Data_API_Official_Trunk_v1
run_calibration.cmd
```

## Outputs gerados
- `examples/calibration_snapshot_generated.json`
- `logs/calibration_run_log_generated.json`
- `logs/calibration_summary_generated.json`


## Correção v1.1.2
- O entrypoint oficial do trunk foi corrigido para usar o service real `data_api/services/fixtures_service.py`, onde existe `get_fixtures_by_league_season()`.
- O ficheiro `data_api/providers/fixtures_provider.py` no trunk físico é apenas placeholder e não expõe a função esperada.
