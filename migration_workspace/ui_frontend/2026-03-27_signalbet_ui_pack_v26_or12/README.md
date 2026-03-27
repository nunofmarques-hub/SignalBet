# UI Frontend SignalBet v26 — OR12 Protected Payload Integration Pack

## Objective
Integrate the protected payload exposed by OR12 into the UI without opening direct access to the real source.

## Focus of this pack
- make the main CTA reflect protected operational state
- make the status panel reflect the protected baseline validated by OR12
- keep the UI as a protected consumer only
- preserve reversibility and structural discipline

## Current status
This pack remains in **staging**.
It does **not** connect the UI directly to the physical trunk or a real provider.
It does consume and present the protected OR12 payload shape for:
- readiness
- CTA state
- bridge status
- final status
- protected baseline status fields

## Official source in this stage
The UI consumes the **protected payload exposed by OR12 / Orchestrator / App Core**.
It must not consume:
- physical trunk directly
- real provider directly
- parallel bridge outside the central corridor
- alternative feed outside OR12
