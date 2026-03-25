# Data Handoff BTTS

## Dependências mínimas de dados para v1 robusta
- fixture master por jogo
- events timeline por fixture
- standings por jornada
- team profiles rolling por equipa
- snapshot pré-jogo básico

## Reforço de qualidade
- fixture statistics por jogo
- odds pré-jogo
- xG ou xG proxy enriquecido
- splits casa/fora
- rolling histories pré-computados

## Blocos alimentados
- BOS: scoring support estrutural
- BVS: concession support estrutural
- SBI: simetria e dominância
- AMI: momento recente
- FGT: timing útil
- TSI: estabilidade do padrão
- xG Gap: valor escondido / sobreconversão / subconversão

## Hand-off esperado da Data/API Layer
A camada central deve entregar ao BTTS objetos internos estáveis, e não payloads raw da API:
- `MatchContext`
- `TeamSnapshot`
- `LeagueSnapshot`
- snapshots rolling pré-jogo

## Nota operacional
A cobertura atual permite continuar em teste. O pack não deve ser tratado ainda como pronto para integração final.
