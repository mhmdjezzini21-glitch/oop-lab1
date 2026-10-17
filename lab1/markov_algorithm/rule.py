"""A single rule for a normal Markov algorithm."""
import re

class Rule:
    __slots__ = ("_left", "_right", "_terminal")

    def __init__(self, left: str, right: str, terminal: bool = False) -> None:
        if not left: raise ValueError("Left side (pattern) cannot be empty")
        self._left = left
        self._right = right
        self._terminal = terminal

    @property
    def left(self) -> str: return self._left
    @property
    def right(self) -> str: return self._right
    @property
    def terminal(self) -> bool: return self._terminal

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rule): return NotImplemented
        return (self._left == other._left and self._right == other._right and self._terminal == other._terminal)

    def __hash__(self) -> int:
        return hash((self._left, self._right, self._terminal))

    def __str__(self) -> str:
        arrow = "->." if self._terminal else "->"
        return f"{self._left} {arrow} {self._right}"

    def __repr__(self) -> str:
        return f"Rule({self._left!r}, {self._right!r}, terminal={self._terminal})"

    @classmethod
    def from_string(cls, text: str) -> "Rule":
        match = re.match(r"^(.*?)->\.?\s*(.*)$", text)
        if not match: raise ValueError(f"Invalid rule format: {text!r}")
        left = match.group(1).strip()
        right_raw = match.group(2)
        terminal = "->." in text
        if not left: raise ValueError("Left side cannot be empty")
        return cls(left, right_raw.strip(), terminal)

    def apply_to(self, text: str) -> tuple[str, bool]:
        if self._left in text:
            new_text = text.replace(self._left, self._right, 1)
            return new_text, True
        return text, False
