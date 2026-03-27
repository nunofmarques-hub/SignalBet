# Política mínima de operação

## Cache
Usar apenas storage/cache oficial já existente no trunk. Não abrir fetch novo nesta fase.

## Refresh
Refresh apenas explícito e controlado. Sem refresh agressivo nem live total.

## Fallback
Se uma fixture não tiver statistics context disponível, devolver output protegido com:
- `statistics_status = missing`
- `fallback_used = true`

A fixture continua utilizável pela baseline principal.

## Comportamento em erro
Erro no enrichment de statistics **não quebra** a leitura principal de fixtures.
O estado final do run só é hard fail se a baseline principal falhar.

## Logs mínimos
Por run:
- `fixture_id`
- `statistics_status`
- `fallback_used`
- `provider_path`
- `final_status`
