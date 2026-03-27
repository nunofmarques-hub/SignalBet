# UI v26 Architecture Note

This pack does not redesign the frontend.
It updates the UI to consume the protected payload shape exposed by OR12 and present it clearly.

## Architectural rule
The UI only:
- reads
- interprets
- presents

The UI does not:
- decide runtime policy
- talk directly to the physical trunk
- talk directly to the real provider
- duplicate orchestrator logic
