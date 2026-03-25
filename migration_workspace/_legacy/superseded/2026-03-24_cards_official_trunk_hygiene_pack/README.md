# 2026-03-24_cards_official_trunk_hygiene_pack

## objetivo do pack
Fechar o módulo Cards como staging forte, com provider oficial único, pipeline curto, output estável e disciplina completa de Pack Hygiene.

## estado do pack
staging

## módulo / frente
cards

## dependências
- Python 3.11+
- Data/API Layer oficial disponível em `data_api/` para modo live
- Contrato transversal SignalBet v1.1

## ponto de entrada
- `run_smoke.py`
- `run_demo.py`
- `START_CARDS_OFFICIAL_HYGIENE.cmd`

## ponto de saída
- `out/live_candidate.json` ou `out/blocked_live_run.json`
- `out/contract_smoke_candidate.json`
- `pack_check_report.txt`

## referência ao contrato
- `market_pick.v1.1`
- contrato transversal SignalBet v1.1

## ligação à Data/API Layer
Este pack lê **exclusivamente** do provider oficial do `Data_API_Official_Trunk_v1`:
- provider: `providers/official_live_provider.py`
- serviços consumidos:
  - `data_api.services.fixtures_service.get_fixtures_by_league_season`
  - `data_api.services.events_service.get_fixture_events`
- objeto lógico consumido: `fixtures + fixture_events`

### campos mínimos esperados da base
- fixtures da liga/época
- `fixture.id`
- `teams.home.name`
- `teams.away.name`
- `league.name`
- events por fixture
- identificação simples de eventos de cartão

## como correr o smoke test
### modo oficial live
```bash
python run_smoke.py --mode live --league 140 --season 2024
```

### modo contract-smoke
Usa doubles em memória com os **mesmos paths oficiais** para provar o pipeline via `official_live_provider` quando o trunk físico não está montado no ambiente.
```bash
python run_smoke.py --mode contract-smoke --league 140 --season 2024
```

## notas finais
- O provider oficial é a fonte única do módulo.
- Não existe mirror local nem sample input intermédio de staging para o pipeline principal.
- Quando o trunk físico estiver montado em `data_api/`, o modo `live` deve correr sem doubles.
