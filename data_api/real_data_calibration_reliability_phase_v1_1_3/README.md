# Real Data Calibration & Reliability Phase — v1.1.3

Pack de ajuste cirúrgico da fase de calibração real.

## Objetivo
Corrigir o alinhamento do pack com o contrato real do trunk e maximizar cobertura sem reabrir arquitetura.

## Mantém igual
- provider/service oficial do trunk
- trunk oficial
- Orchestrator como consumidor principal
- modelo de snapshot e logging
- distinção entre green / degraded_run / hard_fail

## Ajuste principal desta versão
1. Usa primeiro o contrato real do serviço:
   - `get_fixtures_by_league_season(league_id, season, status="FT-AET-PEN")`
2. Não passa listas de statuses ao serviço.
3. Se a cobertura continuar insuficiente, tenta combinações alternativas de liga/época apenas entre cenários disponíveis no próprio trunk.
4. Escolhe o melhor snapshot válido encontrado, mantendo logs legíveis.

## Execução
### Windows
`run_calibration.cmd`

### Linux/macOS
`./run_calibration.sh`

## Outputs esperados
- `examples/calibration_snapshot_generated.json`
- `logs/calibration_run_log_generated.json`
- `logs/calibration_summary_generated.json`
- `logs/bootstrap_debug_generated.json`
