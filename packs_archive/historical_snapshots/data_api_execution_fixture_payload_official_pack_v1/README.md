# data_api_execution_fixture_payload_official_pack_v1

## objetivo_do_pack
Entregar o payload físico final de fixture do `Data_API_Official_Trunk_v1`, em formato estável e oficialmente consumível pela Execution / Tracking.

## estado_do_pack
staging

## dependencias
- `Data_API_Official_Trunk_v1` disponível localmente
- Python 3.11+
- catálogo de fixtures no tronco oficial
- contrato v1.1 como referência estrutural

## ponto_de_entrada
- `run_smoke.cmd`
- `src/build_execution_fixture_payload.py`

## ponto_de_saida
- `examples/execution_fixture_payload_generated.json`

## provider_oficial
- provider_name: `fixtures_provider.py`
- service_name: `get_fixtures_by_league_season()`
- provider_object: `fixtures_catalog`
- official_path: `data_api/storage/raw/league_<league_id>/season_<season>/catalog/fixtures_catalog_status_FT_AET_PEN.json`
