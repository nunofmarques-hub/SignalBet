# Corners Confidence Risk Refinement Pack

## objetivo do pack
Dar mais convicção ao caso forte do módulo Corners, refinando:
- score_over final
- confidence_raw
- risk_raw
- distância entre candidate / watchlist / rejected

## estado do pack
staging

## dependências
- Python 3.x
- sem dependências externas

## ponto de entrada
- `testes/run_demo.py`

## ponto de saída
- `output_contratual/case_1_forte_market_pick.json`
- `output_contratual/case_2_media_market_pick.json`
- `output_contratual/case_3_rejeitada_market_pick.json`
- `output_contratual/summary.json`

## referência ao contrato v1.1
Este pack emite candidate picks em `market_pick.v1.1`.

## provider oficial da Data/API
- provider oficial: `data_api`
- objeto oficial consumido: `corners_input.v1`

## lógica final de classificação
- score final = score direcional + força da linha - penalties
- confidence_raw depende da banda + coerência linha/projeção
- risk_raw depende da robustez estrutural e da presença de alertas/penalties
- objetivo:
  - caso forte -> candidate
  - caso médio -> watchlist
  - caso rejeitado -> rejected

## destino final pretendido
`modules/corners/`
