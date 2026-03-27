
# Bloqueio atual de execução local — nota curta

## O que foi observado
- abrir o pack por `file://` causa bloqueio de imports ES modules / CORS
- foi observado erro `GET /js/data/mock-data.js -> 404`

## O que é bloqueio do ambiente
- `file://` não é ambiente suportado para este pack
- a app precisa de servidor local simples para servir `src/`

## O que era bloqueio do pack
- path/import de `mock-data.js` apontava para caminho incorreto

## Situação atual
- o path foi alinhado com a estrutura real do pack (`src/data/mock-data.js`)
- via servidor local simples, a subida fica limpa sem esse 404
