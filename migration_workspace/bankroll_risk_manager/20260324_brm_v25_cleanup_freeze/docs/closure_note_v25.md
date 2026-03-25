# Closure Note v25

- A linha oficial ativa da Banca é a v24.
- O upstream oficial desta linha é o GPS v6.
- O contrato `gps_to_bank_v24` fica mantido como contrato congelado nesta fase.
- A resposta `bank_resp_v24` permanece estável para os estados `APPROVED`, `APPROVED_REDUCED`, `BLOCKED` e `RESERVE`.
- O `bank_to_exec_v24` mantém-se como payload final oficial da Banca para a Execution.
- Apenas `APPROVED` e `APPROVED_REDUCED` seguem para placement / intake da Execution.
- `BLOCKED` e `RESERVE` ficam auditados na Banca e não seguem para placement.
- Este pack remove resíduos de ambiente (`__pycache__`, `.pyc`) e formaliza a linha congelada do corredor.
