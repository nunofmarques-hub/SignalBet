# Bankroll / Banca — Pack de Substituição Integral Limpa

## Objetivo do pack
Substituir integralmente a pasta viva `modules/bankroll/` por uma linha limpa, clara e sem ruído estrutural, preservando a linha oficial ativa da Banca nesta fase.

## Estado do pack
pronto_para_integracao

## Dependências
- GPS v6 clean pack como upstream oficial
- Execution / Tracking como downstream oficial
- Contrato Transversal de Integração SignalBet v1.1 Operacional
- Upstream indireto progressivamente alinhado com `Data_API_Official_Trunk_v1`

## Ponto de entrada
- `contracts/gps_to_bank_v24.json`
- `examples/gps_batch_in_v24.json`
- `run_smoke.py`

## Ponto de saída
- `contracts/bank_resp_v24.json`
- `contracts/bank_to_exec_v24.json`
- `examples/bank_resp_batch_v24.json`
- `examples/exec_payload_v24.json`

## Referência ao contrato v1.1
Este pack mantém a linha contratual congelada da Banca para a fronteira GPS -> Banca -> Execution.

## Como lê da Data/API Layer ou o que falta
A Banca não consome a API externa diretamente. O upstream oficial é o GPS v6 clean pack, que consolida picks vindas de módulos progressivamente ligados ao `Data_API_Official_Trunk_v1`.

## Ficheiros principais
- `contracts/gps_to_bank_v24.json`
- `contracts/bank_resp_v24.json`
- `contracts/bank_to_exec_v24.json`
- `contracts/bank_rules_v24.yaml`
- `contracts/bank_policy_v24.yaml`
- `contracts/app_phase1/banking_decisions_phase1_contract.json`
- `contracts/app_phase1/banking_decisions_phase1_example.json`
- `contracts/app_phase1/shortlist_enriched_with_banking_decisions_example.json`
- `contracts/edge_cases/expected_v24.json`
- `docs/closure_note_v25.md`
- `docs/official_line_status_v27.md`
- `docs/replacement_note_v27.md`

## Destino final pretendido
`modules/bankroll/`

## O que este pack substitui
Substitui integralmente a pasta viva atual de `modules/bankroll/`.

## O que passa a ser a linha ativa
Mantém-se a linha oficial ativa da Banca: **v24**, estabilizada e limpa pelo cleanup/freeze **v25**. Este pack v27 é a substituição física limpa dessa linha no repositório vivo.

## O que sai da pasta viva
- ficheiros transitórios de colocação manual
- notas de fecho redundantes já ultrapassadas
- script `flow_demo.py` sem papel oficial nesta fase
- qualquer lixo de ambiente, `__pycache__` ou `.pyc`

## O que vai para arquivo / histórico / legacy
- zips e packs intermédios anteriores desta frente
- notas e artefactos transitórios absorvidos pela linha v24/v25
- histórico não necessário à leitura da pasta viva
