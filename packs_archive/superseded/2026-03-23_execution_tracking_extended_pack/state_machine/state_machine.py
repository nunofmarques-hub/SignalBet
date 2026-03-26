from __future__ import annotations
from .transition_rules import ALLOWED_TRANSITIONS


class StateTransitionError(Exception):
    pass


class StateMachine:
    def ensure_allowed(self, from_state: str, to_state: str) -> None:
        allowed = ALLOWED_TRANSITIONS.get(from_state, set())
        if to_state not in allowed:
            raise StateTransitionError(f"Blocked transition: {from_state} -> {to_state}")
