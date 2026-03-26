# Integration Note

## O que já está real neste pack
- O caso de handoff da Banca foi montado a partir dos ficheiros reais do pack `bankroll_gps_handoff_freeze_pack_v1_8`.
- O intake testado usa esse payload enriquecido como candidato real de entrada da Execution.
- O caso de ledger e analytics já está estabilizado em formato de output da Execution.

## O que ainda está em formato-alvo
- O payload de fixture em `settlement/fixture_real_payload/` ainda é um contrato-alvo porque a Data/API Layer não congelou o provider oficial desta frente.

## Próximo bloqueio real
Congelar o payload final Banca -> Execution e alinhar o hook oficial Data/API -> Execution para settlement.
