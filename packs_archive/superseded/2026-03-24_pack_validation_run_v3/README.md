# App Core / Orchestrator — Pack Validation Run v3

## Missão
Construir a camada transversal da app principal que coordena a corrida ponta a ponta: valida ambiente, confirma readiness do `Data_API_Official_Trunk_v1`, descobre módulos elegíveis, corre subset de módulos, agrega na Opportunity Pool, passa por GPS e Banca, e devolve estado claro à UI.

## Estado do pack
`staging_operacional_inicial`

## O que este pack acrescenta
- mini `validation_run` executável
- checks reais sobre o `Data_API_Official_Trunk_v1`
- ordem oficial do pipeline implementada em draft operacional
- sample end-to-end mais próximo do pipeline real
- output/resumo de execução pronto para UI

## Como correr a demo
No diretório deste pack:

```bash
python run_validation_demo.py
```

O script corre um `validation_run` mínimo sobre um cenário local de demonstração e grava resultados em:

- `runtime_outputs/last_health_report.json`
- `runtime_outputs/last_run_summary.json`
- `runtime_outputs/last_ui_status.json`

## Princípios
- coordena, não recalcula
- UI mostra o botão; Orchestrator governa o fluxo
- `Data_API_Official_Trunk_v1` é a base oficial de readiness
- validação real antes de sofisticação
- simplicidade, auditabilidade e disciplina acima de ruído
