# Closure Gates — Execution / Tracking

## Quando a Execution pode ser considerada fechada
A frente só deve ser considerada **fechada** quando os três gates abaixo estiverem verdes ao mesmo tempo.

### Gate 1 — Input oficial da Banca
A Execution deve consumir diretamente o `bank_to_exec_v24` **físico** vindo da Banca.

Estado neste pack:
- **Parcialmente verde**
- existe contrato-alvo e exemplo pronto para consumo
- falta confirmação física do pack BRM v24 no ambiente

### Gate 2 — Settlement oficial do tronco
O settlement deve ler um payload físico e congelado do `Data_API_Official_Trunk_v1`.

Estado neste pack:
- **Parcialmente verde**
- existe contrato-alvo oficial e fluxo E2E preparado
- falta congelar o shape final do provider de fixture

### Gate 3 — E2E auditável do corredor
É preciso provar um caso ponta a ponta com:
- intake aprovado
- execução registada
- settlement fechado
- ledger gerado
- analytics gerado
- audit gerado

Estado neste pack:
- **Verde em staging**
- smoke test gera ledger, analytics e audit

## Leitura final
A Execution está fechada em **estrutura e operação de staging**.
Para ficar fechada em **integração real**, só depende de dois artefactos externos: `bank_to_exec_v24` físico e provider físico de fixture do tronco oficial.
