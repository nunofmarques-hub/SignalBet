# Known limits

- Este pack assume como válido o handoff oficial do chefe para leitura do tronco.
- O código já aponta a serviços oficiais da `data_api` e não deve voltar a ler diretamente a API externa se o recurso existir no tronco.
- O smoke test depende da presença real dos serviços `data_api.services.*` no ambiente de integração.
