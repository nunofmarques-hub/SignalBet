# Data_API_Official_Trunk_v1_Consolidation_Pack

## Objetivo
Consolidar o `Data_API_Official_Trunk_v1` como referência oficial ativa da Data/API Layer do projeto SignalBet / ABC PRO.

A partir desta versão:
- providers e services aqui definidos passam a ser os caminhos oficiais de consumo
- módulos em staging devem consumir a base comum a partir deste tronco
- packs anteriores deixam de ser referência ativa e passam a histórico, seed ou material de migração

## Estado
- estado_pack: staging
- integração: parcial forte
- contrato: v1.1
- pode_integrar_ja: sim, parcialmente com boa confiança

## Já pronto
- estrutura oficial do tronco
- providers oficiais iniciais
- collectors prioritários green
- storage raw oficial
- services oficiais de consumo
- smoke tests green:
  - v12
  - BTTS
  - Cards

## Evolução futura
- normalização completa
- odds provider oficial
- settlement/contexto para Execution
- handoff profundo para GPS / Banca / Execution

## Providers oficiais
- `fixtures_provider.py`
- `standings_provider.py`
- `events_provider.py`
- `fixture_statistics_provider.py`
- `team_statistics_provider.py`

## Services oficiais
- `get_fixtures_by_league_season()`
- `get_standings_snapshot()`
- `get_fixture_events()`
- `get_fixture_statistics()`
- `get_team_statistics()`

## Paths oficiais de consumo por módulo
- v12 → fixtures, standings, team_statistics, fixture_statistics
- BTTS → fixtures, events, team_statistics, standings
- Cards → fixtures, events
- Corners → fixtures, fixture_statistics

## Regras
Nenhum módulo em staging deve abrir novos fluxos mínimos com chamadas diretas à API externa se o recurso já existir no `Data_API_Official_Trunk_v1`.

## Packs anteriores
- `Data_API_Official_Trunk_v1` = referência oficial ativa de base
- `SignalBet_Data_API_Layer_Integration_Seed_v1_Fresh2` = intermédio / superado
- `SignalBet_Data_API_Layer_Week1_Fresh` = seed estrutural / histórico
- packs antigos = migração / arquivo / legado

## Como validar
1. preencher `api.env.txt`
2. correr `START_TRUNK_CHECK.cmd`
3. correr os collectors prioritários ou usar cache existente
4. correr smoke tests dos módulos

## Smoke tests validados
- v12: GREEN
- BTTS: GREEN
- Cards: GREEN
