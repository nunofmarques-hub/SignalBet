# Provider usage

## Fonte oficial
`Data_API_Official_Trunk_v1`

## Provider/serviço oficial usado
- `get_fixtures_by_league_season()`
- `get_standings_snapshot()`
- `get_team_statistics()`
- `get_fixture_statistics()`

## Objeto consumido pelo v12
- `fixtures_catalog`
- `standings_snapshot`
- `fixture_statistics`
- `team_statistics`

## Campos obrigatórios mínimos
### fixture
- `fixture.id`
- `fixture.date`
- `league.id`
- `league.name`
- `teams.home.id`
- `teams.home.name`
- `teams.away.id`
- `teams.away.name`

### team_statistics
- `goals_for_per_game`
- `goals_against_per_game`
- `shots_on_target_per_game`

### standings_snapshot
- objeto válido da liga/época para enriquecer contexto competitivo

### fixture_statistics
- objeto válido por fixture para cruzamento contextual

## Regra operacional
O v12 não deve usar fallback preferencial para staging/local quando o provider oficial do tronco estiver disponível.
