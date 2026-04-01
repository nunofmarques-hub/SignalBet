# v12 — integration feed clean pack

Pack limpo de substituição para o feed oficial de integração da v12.

## Função
Disponibilizar `integration_feeds/v12/latest.json` como feed vivo, curto, estável e diretamente consumível pelo Orchestrator.

## Escopo ativo
- Over 1.5 equipa
- Over 1.5 jogo
- Under 3.5

## Não inclui
- BTTS
- Over 2.5
- Under 2.5
- família Over/Under alargada
- detalhe profundo do motor
- histórico misturado

## Estrutura viva
- `integration_feeds/v12/latest.json`
- `run_smoke.py`
- `manifest.json`
- `docs/substituicao_integral.md`
- `pack_check_report.txt`

## Nota
Este pack existe para substituir integralmente a linha viva do feed da v12, removendo ruído, redundância e competição entre versões.
