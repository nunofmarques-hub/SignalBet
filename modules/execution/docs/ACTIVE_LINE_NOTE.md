# Execution / Tracking — Linha oficial ativa

## O que este pack substitui
Substitui a linha viva anterior de `modules/execution/` por uma linha limpa e consolidada, sem ruído de staging intermédio, crosswalks transitórios ou exemplos superseded a competir visualmente com a base oficial.

## O que passa a ser a linha ativa
Passa a ser a linha oficial ativa da Execution nesta fase, já provada com:
- intake oficial de `bank_to_exec_v24`
- settlement com payload físico final de fixture do `Data_API_Official_Trunk_v1`
- outputs núcleo `ledger`, `analytics`, `audit`
- `tracking_summary` curto para a app phase 1

## O que sai da pasta viva
Devem sair da pasta viva:
- exemplos e handoffs antigos de alinhamento intermédio
- variantes de intake pré-`bank_to_exec_v24`
- notas de bloqueios/provisoriedade já ultrapassadas
- staging intermédio e artefactos redundantes

## O que vai para arquivo / histórico / legacy
Qualquer pack de:
- crosswalk
- integration alignment
- operational flow intermédio
- provas parciais anteriores ao fecho do corredor

deve ir para arquivo / histórico / legacy e deixar de competir com esta linha ativa.

## Estado final desta linha
**frente pronta para substituição integral limpa**
