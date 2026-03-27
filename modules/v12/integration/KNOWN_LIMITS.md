# Known limits

- Este pack já elimina fallback preferencial para staging/local no caminho principal.
- O smoke test real depende da presença efetiva dos serviços `data_api.services.*` no ambiente de integração.
- O output estável do módulo está fechado no contrato `market_pick.v1.1`, mas a robustez final depende da qualidade do payload entregue pelo tronco oficial.
