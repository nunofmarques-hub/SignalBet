# corners_official_trunk_adoption_pack_v1

## objetivo_do_pack
Provar adoção real do `Data_API_Official_Trunk_v1` pelo módulo Corners, sem chamadas diretas à API externa.

## estado_do_pack
staging

## dependencias
- `Data_API_Official_Trunk_v1` disponível localmente
- Python 3.11+
- cache mínima no tronco com fixtures e fixture_statistics

## ponto_de_entrada
- `run_smoke.cmd`
- `src/corners_trunk_smoke.py`

## ponto_de_saida
- `examples/corners_smoke_output_generated.json`

## contrato
- referência ao contrato v1.1 do tronco oficial

## como_le_da_data_api_layer
Leitura exclusiva via:
- `get_fixtures_by_league_season()`
- `get_fixture_statistics()`

## provider_oficial_usado
Leitura indireta via services oficiais do tronco.

## o_que_este_pack_prova
- leitura real da fonte oficial
- resolução do trunk por path configurável
- output mínimo estabilizado de contexto Corners

## o_que_ainda_nao_faz
- scoring final completo de cantos
- candidate generation final
- integração com GPS/Banca
