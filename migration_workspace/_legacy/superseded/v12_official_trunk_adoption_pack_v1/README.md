# v12_official_trunk_adoption_pack_v1

## objetivo_do_pack
Provar adoção real do `Data_API_Official_Trunk_v1` pelo v12, sem chamadas diretas à API externa.

## estado_do_pack
staging

## dependencias
- `Data_API_Official_Trunk_v1` disponível localmente
- Python 3.11+
- cache mínima no tronco com fixtures, standings, team_statistics e fixture_statistics

## ponto_de_entrada
- `run_smoke.cmd`
- `src/v12_trunk_smoke.py`

## ponto_de_saida
- `examples/v12_smoke_output_generated.json`

## contrato
- referência ao contrato v1.1 do tronco oficial

## como_le_da_data_api_layer
Leitura exclusiva via:
- `get_fixtures_by_league_season()`
- `get_standings_snapshot()`
- `get_team_statistics()`
- `get_fixture_statistics()`

## provider_oficial_usado
Leitura indireta via services oficiais do tronco.
