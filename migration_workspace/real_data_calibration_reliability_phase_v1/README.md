# real_data_calibration_reliability_phase_v1

## objetivo_do_pack
Abrir a Real Data Calibration & Reliability Phase com foco em repetição controlada da leitura real, cobertura multi-fixture, comportamento green/degraded_run/hard_fail, estabilidade do snapshot e impacto no Orchestrator.

## estado_do_pack
staging

## dependencias
- `Data_API_Official_Trunk_v1` disponível localmente
- Python 3.11+
- provider oficial de fixtures já funcional

## ponto_de_entrada
- `run_calibration.cmd`
- `src/real_data_calibration_runner.py`

## ponto_de_saida
- `examples/calibration_snapshot_generated.json`
- `logs/calibration_run_log_generated.json`
- `logs/calibration_summary_generated.json`

## foco_desta_fase
- repetição controlada
- mais do que 1 fixture
- estabilidade do snapshot
- consistência dos dados
- impacto no Orchestrator como consumidor principal
