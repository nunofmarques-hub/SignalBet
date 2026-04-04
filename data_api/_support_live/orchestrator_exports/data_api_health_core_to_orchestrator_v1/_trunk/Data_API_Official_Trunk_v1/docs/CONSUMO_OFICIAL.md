# CONSUMO_OFICIAL

## Paths de consumo por módulo
- v12 → fixtures, standings, team_statistics, fixture_statistics
- BTTS → fixtures, events, team_statistics, standings
- Cards → fixtures, events
- Corners → fixtures, fixture_statistics

## Regra
Os módulos em staging devem consumir a Data/API Layer via services e não via chamadas diretas à API externa.
