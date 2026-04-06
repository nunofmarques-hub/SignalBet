# Handoff curto — UI linha oficial viva limpa

## Esta linha passa a ser
a base oficial viva da frente UI / Frontend

## Substitui
- payloads antigos de teste
- cmd transitórios de aplicação manual
- backups redundantes
- docs duplicadas
- artefactos intermédios já absorvidos

## Deve sair da pasta viva
- `aplicar_teste*.cmd`
- `aplicar_teste*_runtime_outputs.cmd`
- `aplicar_teste_cadeia*.cmd`
- payloads de teste antigos
- `app_phase1_protected_payload.json.json`
- `app_phase1_protected_payload_backup.json`
- docs redundantes

## Deve ir para histórico / legacy
- variantes antigas já ultrapassadas
- packs intermédios
- snapshots de correção sem papel vivo
