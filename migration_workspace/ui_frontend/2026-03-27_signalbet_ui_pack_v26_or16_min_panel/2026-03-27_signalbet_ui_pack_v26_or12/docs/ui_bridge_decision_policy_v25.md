# UI v25 — Bridge Decision Policy

## Reuse
The bridge reuses a snapshot when:
- a protected snapshot exists
- freshness remains valid
- no invalidation trigger is active
- force refresh is not requested

## Refresh
The bridge attempts refresh when:
- the snapshot is stale
- a new protected read is allowed
- force refresh is requested
- policy says freshness is insufficient for safe reuse

## Reuse blocked
Reuse is blocked when:
- snapshot_invalidated = true
- forceRefresh = true
- freshness falls outside the accepted window
- bridge policy requires new read attempt first

## Accept stale snapshot
A stale snapshot may still be reused only when:
- refresh was attempted and failed
- fallback to protected stale reuse is explicitly allowed
- UX continuity is preferable to empty/failure state
- the bridge records the decision reason

## Fallback
The bridge falls back when:
- protected real read is unavailable or rejected
- refresh fails and reuse is not allowed
- observed shape is insufficient after adaptation
- policy determines that mock fallback is safer than broken UX

## Stable vs experimental
### Already stable in this phase
- explicit reuse path
- explicit refresh attempt path
- explicit fallback path
- requested_mode vs observed_mode visibility
- protected snapshot persistence and reuse

### Still experimental
- scope growth of protected real read
- tighter freshness thresholds under mixed conditions
- future partial live entry point
