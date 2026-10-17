"""A single transition rule of a Turing machine."""
from __future__ import annotations
from typing import Tuple

BLANK = "_"
DIRECTIONS = ("L", "R", "N")

class Rule:
    __slots__ = ("_initial_state", "_target_state")

    def __init__(self, initial_state: Tuple[str, str], target_state: Tuple[str, str, str]) -> None:
        if not (isinstance(initial_state, tuple) and len(initial_state) == 2):
            raise ValueError("initial_state must be a (state, symbol) tuple")
        if not (isinstance(target_state, tuple) and len(target_state) == 3):
            raise ValueError("target_state must be a (state, symbol, direction) tuple")

        state, symbol = initial_state
        next_state, new_symbol, direction = target_state

        if not state: raise ValueError("state must be a non-empty string")
        if not next_state: raise ValueError("next_state must be a non-empty string")
        if len(symbol) != 1: raise ValueError("symbol must be a single character")
        if len(new_symbol) != 1: raise ValueError("new_symbol must be a single character")
        if direction not in DIRECTIONS: raise ValueError(f"direction must be one of {DIRECTIONS}")

        self._initial_state = (state, symbol)
        self._target_state = (next_state, new_symbol, direction)

    @property
    def initial_state(self) -> Tuple[str, str]: return self._initial_state

    @property
    def target_state(self) -> Tuple[str, str, str]: return self._target_state

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rule): return NotImplemented
        return self._initial_state == other._initial_state and self._target_state == other._target_state

    def __hash__(self) -> int:
        return hash((self._initial_state, self._target_state))

    def __str__(self) -> str:
        return f"{self._initial_state[0]},{self._initial_state[1]} -> {self._target_state[0]},{self._target_state[1]},{self._target_state[2]}"

    def __repr__(self) -> str:
        return f"Rule({self._initial_state!r}, {self._target_state!r})"

    @classmethod
    def from_string(cls, text: str) -> "Rule":
        if "->" not in text: raise ValueError(f"Invalid rule line: {text!r}")
        left, right = text.split("->", 1)
        left_parts = [p.strip() for p in left.split(",")]
        right_parts = [p.strip() for p in right.split(",")]
        if len(left_parts) != 2: raise ValueError(f"Invalid left part: {left!r}")
        if len(right_parts) != 3: raise ValueError(f"Invalid right part: {right!r}")
        return cls((left_parts[0], left_parts[1]), (right_parts[0], right_parts[1], right_parts[2]))

    def to_string(self) -> str: return str(self)
