# Execution / Tracking — Corridor Minimum Ready Pack

# 2026-03-24_execution_tracking_definitive_closure_pack

## objetivo do pack
Fechar a frente Execution / Tracking em nível de **staging forte com prova operacional de corredor**, mostrando o que já está resolvido internamente e o que ainda depende de upstream oficial para o módulo ser considerado **fechado**.

## estado do pack
staging

## módulo / frente
execution_tracking

## dependências
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- Data_API_Official_Trunk_v1
- Banca / Bankroll & Risk Manager upstream
- GPS v6 como upstream oficial da Banca (por coordenação)
- pack BRM disponível no ambiente: `bankroll_risk_manager_2026-03-23_bankroll_gps_handoff_freeze_pack_v1_8.zip`

## ponto de entrada
- `examples/intake/bank_to_exec_v24_example.json`
- `contracts/upstream/bank_to_exec_v24.schema.json`
- `src/execution_tracking/orchestrator.py`

## ponto de saída
- `tests/smoke_outputs/ledger.json`
- `tests/smoke_outputs/analytics.json`
- `tests/smoke_outputs/audit.json`

## ligação à Data/API Layer
- caminho oficial ativo: `Data_API_Official_Trunk_v1`
- provider_type: `official_trunk`
- provider_name: `Data_API_Official_Trunk_v1`
- provider_object alvo: `fixtures/provider_settlement_payload`
- neste pack o settlement está **ligado por contrato-alvo oficial**; a ligação fica totalmente fechada quando o payload físico final do provider de fixture for entregue

## como correr o smoke test
```bash
python run_smoke.py
```

## notas finais
Este pack é o melhor fecho honesto da Execution com o material atualmente disponível. Prova intake realista, fluxo ponta a ponta, ledger, analytics e audit. O que ainda falta para considerar o módulo **fechado** está documentado em `docs/CLOSURE_GATES.md`.


## Estado atualizado da frente
- estado: pronto_para_integracao_condicional
- intake oficial: `bank_to_exec_v24`
- settlement oficial: `execution_fixture_payload` vindo do Data_API_Official_Trunk_v1
- bloqueios externos estruturais: nenhum para o corredor mínimo

## Nota
Este pack fecha o caso ponta a ponta mínimo do corredor Banca -> Execution com outputs formais para ledger, analytics e audit.
