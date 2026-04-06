# Orchestrator Payload Writer — nota operacional curta

## Leitura oficial desta linha
O Orchestrator passa a ser a **fonte oficial única** do payload do ciclo.

## O que deixa de ser aceite
- latest.json colado manualmente
- payload paralelo por frente
- montagem manual fora da app
- troca de `pick_id` entre fases
- duplicação semântica do mesmo caso

## O que este writer faz
- cria o payload oficial logo na shortlist
- transporta a mesma identidade operacional ao longo do ciclo
- aplica updates semânticos por fase
- grava sempre no mesmo artefacto oficial

## Semântica mínima preservada
- `cycle_status`: `shortlist_ready` -> `bank_decision_ready` -> `execution_tracking_live` -> `settled`
- `pick_id`: imutável
- `case_id`: único por ciclo
- `orchestrator_payload_status`: `live`

## Regra curta
A app deixa de provar handoffs manualmente.
Passa a atualizar o mesmo payload vivo dentro do corredor.
