
# Discovery rule congelada — OR9u2

## Precedência oficial por módulo
1. `integration_feeds/<module>/latest.json`
2. `integration_feeds/<module>/<module>_output.json`
3. `integration_feeds/<module>/module_output.json`
4. `integration_feeds/<module>/output.json`

## Só depois entram fallbacks secundários
- `runtime/mod_out/<module>/...`
- `mod_out/<module>/...`
- `migration_workspace/<module>/...`
- `modules/<module>/out/...`
- `modules/<module>/examples/...`

## Regra adicional
Os scans recursivos só são tentados depois de todos os paths diretos acima.
`examples/` fica explicitamente como fallback tardio.

## Critérios
- `PASS`: ficheiro encontrado, JSON object, contém `candidates`, e `status` = `PASS` ou ausente.
- `output_invalid`: ficheiro encontrado, mas payload não é object ou não contém `candidates`.
- `output_missing`: nenhum ficheiro encontrado nos paths candidatos.
