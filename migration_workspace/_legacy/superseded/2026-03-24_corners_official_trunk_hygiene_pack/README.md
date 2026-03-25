# 2026-03-24_corners_official_trunk_hygiene_pack

## objetivo do pack
Fechar o módulo Corners como pack disciplinado segundo a regra oficial de Pack Hygiene, mantendo o fluxo funcional já validado:
- provider oficial declarado
- leitura do trunk oficial
- adaptação para o motor
- candidate generation
- output contratual

## estado do pack
staging

## módulo / frente
corners

## dependências
- Python 3.x
- Data/API Layer oficial presente no projeto para integração real
- sem dependências externas obrigatórias no pack

## ponto de entrada
- `run_smoke.py`

## ponto de saída
- `examples/sample_output_case_1_candidate.json`
- `examples/sample_output_case_2_watchlist.json`
- `examples/sample_output_case_3_rejected.json`
- `examples/summary.json`

## referência ao contrato
- `market_pick.v1.1`

## ligação à Data/API Layer
- provider_type: `official_trunk`
- provider_name: `Data_API_Official_Trunk_v1`
- provider_object: `fixtures + fixture_statistics`
- serviços oficiais:
  - `get_fixtures_by_league_season()`
  - `get_fixture_statistics()`

## como correr o smoke test
```bash
python run_smoke.py
```

## resultado esperado do smoke test
- 1 forte = `candidate`
- 1 médio = `watchlist`
- 1 rejeitado = `rejected`
