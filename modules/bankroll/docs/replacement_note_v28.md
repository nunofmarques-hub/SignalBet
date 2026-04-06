# Replacement Note — v28

## O que este pack substitui
Substitui integralmente a pasta viva `modules/bankroll/`.

## O que passa a ser a linha ativa física
A mesma linha oficial do corredor já congelada: base ativa v24, estabilizada pelo cleanup/freeze v25.

## O que sai da pasta viva
- resíduos `__pycache__`
- ficheiros `.pyc`
- duplicações redundantes dos ficheiros `banking_decisions_phase1_*` fora de `contracts/app_phase1/`
- notas de fecho antigas já absorvidas pela leitura oficial da linha

## O que fica congelado
- `gps_to_bank_v24`
- `bank_resp_v24`
- `bank_to_exec_v24`
- `rules`, `policy`, `edge_cases` e docs/contracts úteis da linha
