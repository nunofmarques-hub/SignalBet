# Provider wiring

## path oficial esperado
O smoke test procura por omissão o payload oficial em:

`data_api/exports/v12/provider_official_fixture_878317.json`

Pode ser sobreposto com:

- variável de ambiente `V12_PROVIDER_SAMPLE`

## shape esperado
O ficheiro deve respeitar `schemas/input_shape_provider_real.json`.

## ordem de resolução
1. `V12_PROVIDER_SAMPLE`
2. `data_api/exports/v12/provider_official_fixture_878317.json`
3. `examples/provider_official_input_sample.json` (fallback de staging apenas)
