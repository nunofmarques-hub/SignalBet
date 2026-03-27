# Coverage findings

## Bloqueio atual
O bloqueio já não está no pack de calibração. Está na **cobertura física do trunk**.

## Sinais concretos
- `fixtures_service.py` devolve dados apenas do catálogo oficial.
- `fixture_ids.json` aponta para uma amostra maior do que a atualmente exposta pelo catálogo.
- Existem ficheiros de `events/` e `statistics/` para múltiplos fixtures, mas isso não entra no serviço oficial de fixtures.

## Leitura operacional
Aumentar cobertura = **enriquecer ou regenerar o catálogo oficial**, não mexer mais na arquitetura da calibração.
