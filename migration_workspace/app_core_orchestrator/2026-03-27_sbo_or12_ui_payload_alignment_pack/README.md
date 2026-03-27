# SBO OR12 — UI Payload Alignment Pack

## objetivo
Fechar de forma curta o baseline control flow e aproximar o payload exposto ao formato que a UI v25/v26 irá consumir no botão principal e no painel.

## foco desta ronda
- consolidar OR11 como linha ativa de baseline control flow
- manter intake nativo do trunk
- produzir payload protegido mais próximo da UI
- manter perímetro fechado: sem live total, sem UI direta à fonte real

## referência de legibilidade da UI
Campos enfatizados pela UI:
- requested_mode
- observed_mode
- fallback_used
- bridge_status
- bridge_scope
- stability_status
- source_transition
- bridge_decision_reason
