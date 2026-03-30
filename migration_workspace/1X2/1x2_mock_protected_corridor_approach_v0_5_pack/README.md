# 1X2 — Mock Protected Corridor Approach v0.5

## Estado
staging_forte

## Objetivo desta ronda
Preparar a frente 1X2 para uma aproximação controlada **mockada** ao corredor protegido,
ainda sem integração real com Orchestrator, GPS ou Banca.

## O que este pack prova
- shape futura de input protegido
- adapter mockado de leitura protegida -> input interno 1X2
- output futuro alinhado à cadeia
- separação clara entre:
  - input_status
  - adaptation_status
  - run_status
  - decision_status
  - candidate_status

## O que este pack não faz
- não consome payload real do corredor
- não liga ao Orchestrator
- não faz handoff real para GPS/Banca
- não é pack de integração

## Runner oficial desta linha
run_1x2_mock_protected_corridor.py

## Casos de prova
- case_01_candidate_home.json -> 1 / primary_decision / candidate
- case_02_degraded_1x.json -> 1X / degraded_decision / watchlist
- case_03_rejected.json -> REJECTED / rejected_decision / rejected

## Leitura operacional
Este pack existe para provar forma de consumo futuro e semântica de adaptação, não valor live.
