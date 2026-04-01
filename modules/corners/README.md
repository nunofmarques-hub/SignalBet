# Corners — Integral Clean Substitution Pack

## objetivo
Substituição integral limpa da pasta viva do módulo `corners`.

## estado
integrado

## o que este pack substitui
Substitui a linha ativa atual em `modules/corners/`, absorvendo a estrutura viva útil e removendo ruído intermédio, documentação redundante e restos de iterações já ultrapassadas.

## o que passa a ser a linha ativa
Este pack passa a ser a **única linha viva oficial** do módulo `corners`.

## o que sai da pasta viva
Devem sair da pasta viva:
- docs redundantes e intermédias sem papel vivo
- ruído temporário
- caches
- logs antigos
- artefactos transitórios já ultrapassados
- qualquer subpasta histórica que concorra com a linha ativa

## o que vai para arquivo / histórico / legacy
Tudo o que seja:
- pack antigo
- snapshot intermédio
- iteração superseded
- material apenas comparativo ou histórico

deve seguir para `packs_archive/`, `legacy/` ou zona equivalente de histórico do projeto, e não continuar na pasta viva.

## ponto de entrada oficial
- script: `run_smoke.py`
- comando: `python run_smoke.py`

## estrutura viva preservada
- `src/`
- `run_smoke.py`
- `manifest.json`
- `README.md`
- `docs/` mínimas úteis
- `examples/`
- `contracts/`
- `runtime_inputs/`
- `pack_check_report.txt`

## leitura curta da linha
Linha ativa limpa do Corners, já integrada, com runner oficial congelado, logging fechado, consumo protegido validado e `game_card` curto fechado para a app phase 1.

## nota final
**frente pronta para substituição integral limpa**
