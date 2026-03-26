# Nota de migração — sandbox -> leitura central

## O que muda
A sandbox atual da v12 usa sinais locais/proxies e estrutura de dados ad-hoc. O próximo passo é consumir a shape da Data/API Layer central sem alterar a identidade dos 3 motores.

## Princípio
- a Data/API Layer é dona dos dados, cache e normalização base
- a v12 continua dona da leitura analítica, score raw, risco raw e edge raw

## Substituições esperadas
- ratings locais e perfis de liga -> dados centrais reais
- odds estimadas -> odds snapshot da Data/API Layer
- favorite estimation heurística -> favoritismo derivado de standings/contexto/mercado

## O que não muda
- 3 motores ativos do núcleo
- output no contrato `market_pick.v1.1`
- separação entre raw do módulo e linguagem comparável do selector
