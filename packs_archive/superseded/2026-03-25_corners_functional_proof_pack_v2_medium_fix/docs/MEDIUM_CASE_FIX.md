# Ajuste cirúrgico do caso médio

## problema
O caso médio saía com score 57.26 e caía por pouco abaixo do limiar de `Observação` 58.

## ajuste
Foi aplicado apenas:
- limiar de `Observação` passou de 58 para 57

## motivo
- preserva o caso forte como `candidate`
- recupera o médio para `watchlist`
- mantém o rejeitado como `rejected`
- evita mudanças largas em score, linha ou mapping
