# Integration Note v2.4

## upstream oficial
- Global Pick Selector v6

## ponto de fecho procurado
- congelar `gps_to_bank`
- congelar `bank_resp`
- congelar `bank_to_exec`
- manter 4 estados finais estáveis
- reduzir ambiguidade de roteamento para Execution

## regra de corredor
Só `APPROVED` e `APPROVED_REDUCED` seguem para Execution.
`BLOCKED` e `RESERVE` ficam auditados na banca e fora do placement.
