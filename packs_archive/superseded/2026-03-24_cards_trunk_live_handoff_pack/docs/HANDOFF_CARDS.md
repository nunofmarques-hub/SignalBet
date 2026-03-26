# HANDOFF_CARDS

## Estado
- estado_pack: staging
- leitura_do_tronco: validada_por_interface_oficial
- smoke_test: green

## Fonte oficial
`Data_API_Official_Trunk_v1`

## Ponto de consumo oficial
O Cards deve ler da Data/API Layer via:

- `get_fixtures_by_league_season()`
- `get_fixture_events()`

## Inputs mínimos esperados
- fixtures da liga/época
- events por fixture
- leitura simples de eventos de cartão

## Objetivo do consumo
Permitir ao módulo:
- identificar contexto mínimo de cartões
- validar elegibilidade base
- preparar lógica de sinal ou shortlist

## Regra operacional
O módulo Cards não deve depender de leitura direta da API externa para o fluxo mínimo, se os eventos já existirem no tronco.

## Estado já provado
Smoke test Cards: GREEN

### O que já foi validado
- fixtures lidos do tronco
- events lidos do tronco
- card events simples identificados

## Exemplo de consumo esperado
```python
from data_api.services.fixtures_service import get_fixtures_by_league_season
from data_api.services.events_service import get_fixture_events

fixtures = get_fixtures_by_league_season(140, 2024)
fixture_id = fixtures[0]["fixture"]["id"]

events = get_fixture_events(fixture_id, 140, 2024)
card_events = [
    e for e in events
    if e.get("type") == "Card" or "card" in str(e.get("detail", "")).lower()
]
```
