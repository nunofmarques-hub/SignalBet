# Corners Official Trunk Calibrated Pack

## objetivo do pack
Ligar o Corners ao Data_API_Official_Trunk_v1 e manter o foco na calibração final do motor.

## estado do pack
staging

## provider oficial e objeto consumido
- provider oficial: Data_API_Official_Trunk_v1
- serviços: get_fixtures_by_league_season(), get_fixture_statistics()
- objeto lógico consumido: fixtures + statistics por fixture

## ponto de entrada
- testes/run_trunk_demo.py

## ponto de saída
- output_contratual/case_1_forte_market_pick.json
- output_contratual/case_2_media_market_pick.json
- output_contratual/case_3_rejeitada_market_pick.json
- output_contratual/summary.json

## objetivo analítico
- 1 caso forte = candidate
- 1 caso médio = watchlist
- 1 caso rejeitado = rejected
