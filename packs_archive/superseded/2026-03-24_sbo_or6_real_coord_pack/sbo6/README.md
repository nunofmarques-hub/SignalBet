# 2026-03-24_sbo_or6_real_coord_pack

## objetivo do pack
Fazer o App Core / Orchestrator avançar de staging forte para base mais real de coordenação da corrida global da app.

## estado do pack
staging

## módulo / frente
App Core / Orchestrator

## dependências
- Data_API_Official_Trunk_v1
- feeds reais dos módulos quando existirem
- GPS / Banca / Execution em draft de coordenação

## ponto de entrada
- `run_smoke.py`
- `src/app_orch/launcher/run_val.py`

## ponto de saída
- `out/last_health.json`
- `out/last_sum.json`
- `out/last_ui.json`

## ligação à Data/API Layer
Este pack trata o `Data_API_Official_Trunk_v1` como caminho oficial ativo.
Lê por `project_root` configurável, variável `SIGNALBET_PROJECT_ROOT`, `examples/req/project_root.txt` ou fallback demo do pack.

## como correr o smoke test
```bash
python run_smoke.py
```
Opcionalmente, apontar para um projeto real:
```bash
set SIGNALBET_PROJECT_ROOT=C:\SB\signalbet_project
python run_smoke.py
```

## notas finais
- o botão é da UI; a coordenação técnica é do Orchestrator
- a ordem oficial do pipeline é preservada em código
- se não existir tronco real acessível, o pack cai para modo demo sem fingir integração real
