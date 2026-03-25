# Execution Intake Bridge Note v1

## objetivo
Dar à Execution um payload mínimo claro do que chega depois da decisão da Banca.

## o que deve entrar na Execution
A Execution deve receber apenas picks:
- aprovadas
ou
- aprovadas com redução

## campos mínimos para intake
- identidade da pick
- leitura comparável vinda do GPS
- decisão financeira vinda da Banca
- ordem de execução
- janela de odds aprovada
- nota operacional

## regra prática
A Execution não deve reinterpretar score global nem recalcular stake.
A Execution recebe uma ordem operacional pronta a tentar colocar.

## resultado esperado
A partir deste payload, a Execution consegue:
- registar intake
- tentar placement
- guardar accepted odds
- devolver estado para analytics / audit
