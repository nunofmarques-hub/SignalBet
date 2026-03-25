# Data/API Layer — Semana 1

Objetivo:
- fechar B01 e B02
- criar estrutura oficial
- centralizar config
- separar raw / normalized / derived / state / logs

Regras:
- nenhum módulo deve evoluir como consumidor direto da API externa
- toda a credencial vem de `api.env.txt`
- toda a persistência futura entra por `data_api/storage/`
- toda a nomenclatura principal usa chaves estáveis
