# fixture_statistics_context_activation_v1

Ativação curta, útil e controlada do segundo fluxo real da Data/API Layer.

## Objetivo
Disponibilizar `fixture statistics context` como camada complementar e **não bloqueante** da baseline real de fixtures já validada.

## Fluxo desta fase
- base principal: fixtures via `fixtures_service.py`
- enriquecimento complementar: statistics por fixture via `statistics_service.py`
- consumidor principal: **Orchestrator / App Core**
- UI: apenas acompanhamento, sem ligação direta à fonte real

## Regras fixas
- fixtures continuam a ser a base principal do corredor
- `statistics context` entra apenas como enriquecimento controlado
- ausência ou erro deste fluxo **não pode quebrar** a baseline principal
- `xG` só entra se vier de forma oficial e estável no provider real; nesta versão fica fora
- sem múltiplos providers, sem novos mercados e sem consumo direto por módulos analíticos

## O que o runner faz
1. resolve os entrypoints oficiais do trunk
2. lê o cenário baseline validado (`league_140 / season_2024 / status FT-AET-PEN`)
3. obtém as fixtures do cenário
4. tenta obter statistics context para cada fixture
5. gera output protegido para consumo do Orchestrator
6. escreve logs curtos e um summary final

## Output protegido
Cada fixture mantém sempre a sua base principal.
O enriquecimento entra num bloco separado:
- `statistics_status = available` quando existem statistics
- `statistics_status = missing` quando não existem statistics
- `fallback_used = true` apenas quando o enriquecimento não está disponível

## Ficheiros principais
- `src/fixture_statistics_context_runner.py`
- `src/statistics_context_trunk_adapter.py`
- `examples/protected_fixture_statistics_output_example.json`
- `docs/POLITICA_MINIMA_OPERACAO.md`
- `data_api/docs/MEMORIA_OPERACIONAL_ATIVA.md`

## Como correr
Windows:
- `run_fixture_statistics_context.cmd`

Linux/macOS:
- `run_fixture_statistics_context.sh`

## Critério de sucesso
A ativação fica bem-sucedida quando:
- o segundo fluxo entra sem quebrar a baseline principal
- o Orchestrator o consome sem ambiguidade
- o output protegido continua legível
- não há regressão no corredor já validado
- o perímetro do sistema continua preservado
