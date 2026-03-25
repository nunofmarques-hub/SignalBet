# Integration Note v2.3

Este pack prova o corredor operacional em staging:

GPS batch final -> resposta batch da banca -> payload final para intake da Execution.

O upstream direto da banca é o Global Pick Selector. O downstream direto é a Execution / Tracking.

Somente decisões `APPROVED` e `APPROVED_REDUCED` são encaminhadas para execution.
Decisões `BLOCKED` e `RESERVE` ficam registadas na banca, mas não seguem para placement.
