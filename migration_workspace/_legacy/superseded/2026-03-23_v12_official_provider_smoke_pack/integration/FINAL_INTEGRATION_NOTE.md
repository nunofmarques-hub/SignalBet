# Final integration note

## objetivo
Este pack fecha a transição da v12 de adapter/sandbox para consumo real da base central em modo mínimo.

## fluxo alvo
`data_api/ provider oficial -> provider_bridge.py -> input_adapter.py -> market_engines.py -> contract_output.py`

## condição de prova
Considera-se prova de leitura real quando o smoke test correr com sucesso contra um payload gerado pela `data_api/` no path oficial esperado, sem editar o ficheiro de exemplo do pack.

## caminho oficial esperado nesta entrega
- `data_api/exports/v12/provider_official_fixture_878317.json`

## saída estável esperada
- NDJSON de pool em `examples/smoke_output_pool.ndjson`
- payloads individuais por motor em `examples/smoke_output_*.json`
- schema `market_pick.v1.1`

## estado
- `staging`
- pronto para integração parcial quando houver prova com provider oficial real sem fallback.
