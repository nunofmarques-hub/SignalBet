# btts_official_trunk_adoption_pack_v1

## objetivo_do_pack
Provar adoção real do `Data_API_Official_Trunk_v1` pelo BTTS, sem chamadas diretas à API externa.

## estado_do_pack
staging

## dependencias
- `Data_API_Official_Trunk_v1` disponível localmente
- Python 3.11+
- cache mínima no tronco com fixtures, standings, events e team_statistics

## ponto_de_entrada
- `run_smoke.cmd`
- `src/btts_trunk_smoke.py`

## ponto_de_saida
- `examples/btts_smoke_output_generated.json`

## contrato
- referência ao contrato v1.1 do tronco oficial

## como_le_da_data_api_layer
Leitura exclusiva via:
- `get_fixtures_by_league_season()`
- `get_standings_snapshot()`
- `get_fixture_events()`
- `get_team_statistics()`
