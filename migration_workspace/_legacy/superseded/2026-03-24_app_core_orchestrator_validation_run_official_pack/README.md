# 2026-03-24_app_core_orchestrator_validation_run_official_pack

## Objetivo do pack
Transformar o App Core / Orchestrator numa camada operacional inicial da app, com `validation_run` realmente corrível, checks reais sobre o `Data_API_Official_Trunk_v1`, ordem oficial do pipeline em draft implementado e output utilizável pela UI.

## Estado do pack
`staging`

## Módulo / frente
App Core / Orchestrator

## Dependências
- Python 3.11+
- estrutura local do `Data_API_Official_Trunk_v1`
- outputs de módulos em formato JSON para `validation_run`

## Ponto de entrada
`run_smoke.py`

## Ponto de saída
- `examples/outputs/sample_health_report.json`
- `examples/outputs/sample_output.json`
- `examples/outputs/sample_ui_status.json`

## Ligação à Data/API Layer
Este pack trata o `Data_API_Official_Trunk_v1` como caminho oficial ativo. Lê uma estrutura de trunk em `project_root/data_api/Data_API_Official_Trunk_v1/` e valida `README.md`, `providers/`, `contracts/` e `storage/`. No smoke incluído, o `project_root` aponta para `examples/demo_data_api/`, que simula a estrutura mínima do trunk oficial.

## Como correr o smoke test
Na raiz do pack:

```bash
python run_smoke.py
```

## Notas finais
- O fluxo continua a coordenar, não recalcular.
- A UI mostra o botão; o Orchestrator governa o fluxo.
- `validation_run` usa subset controlado de módulos (`v12` e `cards`).
- `btts` e `corners` ficam fora por maturidade/registry.
- Os inputs são mais reais do que puro sample porque a readiness é verificada sobre uma árvore concreta de `Data_API_Official_Trunk_v1`, ainda que local de demonstração.
