<<<<<<< HEAD
"""Turing machine implementation.

The machine owns:
  * a tape (mutable list of single-character symbols),
  * a head index,
  * a current state,
  * a list of :class:`Rule` objects.

Blank symbol is ``"_"``.
"""

from __future__ import annotations

from typing import Iterable, List, Optional, Tuple

from .rule import Rule

BLANK = "_"
HALT_STATE = "HALT"


class TuringMachineError(Exception):
    """Base exception for Turing machine errors."""


class NoMatchingRuleError(TuringMachineError):
    """Raised when no rule matches the current (state, symbol)."""


class TuringMachine:
    """A single-tape, single-head Turing machine."""

    __slots__ = ("_tape", "_head", "_state", "_rules", "_steps")

    def __init__(
        self,
        tape: Iterable[str],
        rules: Iterable[Rule],
        start_state: str = "q0",
    ) -> None:
        tape_list = list(tape)
        if not tape_list:
            raise ValueError("tape cannot be empty")

        for symbol in tape_list:
            if not isinstance(symbol, str) or len(symbol) != 1:
                raise ValueError(
                    "Every tape symbol must be a single character"
                )

        if not start_state:
            raise ValueError("start_state must be a non-empty string")

        self._tape: List[str] = tape_list
        self._head: int = 0
        self._state: str = start_state
        self._rules: List[Rule] = list(rules)
        self._steps: int = 0

    @classmethod
    def from_machine(cls, other: "TuringMachine") -> "TuringMachine":
        """Deep copy of another machine (copy-constructor equivalent)."""
        if not isinstance(other, TuringMachine):
            raise TypeError("from_machine expects a TuringMachine")
        clone = cls(
            tape=list(other._tape),
            rules=list(other._rules),
            start_state=other._state,
        )
=======
﻿"""Turing machine implementation."""
from __future__ import annotations
from typing import Iterable, List, Optional, Tuple
from .rule import Rule

BLANK = "_"

class TuringMachine:
    __slots__ = ("_tape", "_head", "_state", "_rules", "_steps")

    def __init__(self, tape: Iterable[str], rules: Iterable[Rule], start_state: str = "q0") -> None:
        tape_list = list(tape)
        if not tape_list: raise ValueError("tape cannot be empty")
        for symbol in tape_list:
            if not isinstance(symbol, str) or len(symbol) != 1:
                raise ValueError("Every tape symbol must be a single character")
        if not start_state: raise ValueError("start_state must be a non-empty string")
        self._tape = tape_list
        self._head = 0
        self._state = start_state
        self._rules = list(rules)
        self._steps = 0

    @classmethod
    def from_machine(cls, other: "TuringMachine") -> "TuringMachine":
        if not isinstance(other, TuringMachine): raise TypeError("from_machine expects a TuringMachine")
        clone = cls(tape=list(other._tape), rules=list(other._rules), start_state=other._state)
>>>>>>> feature/lab1-markov
        clone._head = other._head
        clone._steps = other._steps
        return clone

<<<<<<< HEAD
    def __copy__(self) -> "TuringMachine":
        return TuringMachine.from_machine(self)

    def __deepcopy__(self, memo) -> "TuringMachine":
        return TuringMachine.from_machine(self)

    def copy_from(self, other: "TuringMachine") -> None:
        """Copy-assignment equivalent."""
        if not isinstance(other, TuringMachine):
            raise TypeError("copy_from expects a TuringMachine")
=======
    def copy_from(self, other: "TuringMachine") -> None:
        if not isinstance(other, TuringMachine): raise TypeError("copy_from expects a TuringMachine")
>>>>>>> feature/lab1-markov
        self._tape = list(other._tape)
        self._head = other._head
        self._state = other._state
        self._rules = list(other._rules)
        self._steps = other._steps

    @property
<<<<<<< HEAD
    def tape(self) -> Tuple[str, ...]:
        return tuple(self._tape)

    @property
    def head(self) -> int:
        return self._head

    @property
    def state(self) -> str:
        return self._state

    @property
    def steps(self) -> int:
        return self._steps

    @property
    def rules(self) -> Tuple[Rule, ...]:
        return tuple(self._rules)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TuringMachine):
            return NotImplemented
        return (
            self._tape == other._tape
            and self._head == other._head
            and self._state == other._state
            and self._rules == other._rules
        )

    def __hash__(self) -> int:
        return hash(
            (tuple(self._tape), self._head, self._state, tuple(self._rules))
        )

    def add_rule(self, rule: Rule) -> None:
        if not isinstance(rule, Rule):
            raise TypeError("add_rule expects a Rule")
        if rule not in self._rules:
            self._rules.append(rule)

    def remove_rule(self, rule: Rule) -> None:
        if rule in self._rules:
            self._rules.remove(rule)
=======
    def tape(self) -> Tuple[str, ...]: return tuple(self._tape)
    @property
    def head(self) -> int: return self._head
    @property
    def state(self) -> str: return self._state
    @property
    def steps(self) -> int: return self._steps
    @property
    def rules(self) -> Tuple[Rule, ...]: return tuple(self._rules)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TuringMachine): return NotImplemented
        return (self._tape == other._tape and self._head == other._head and self._state == other._state and self._rules == other._rules)

    def __hash__(self) -> int:
        return hash((tuple(self._tape), self._head, self._state, tuple(self._rules)))

    def add_rule(self, rule: Rule) -> None:
        if not isinstance(rule, Rule): raise TypeError("add_rule expects a Rule")
        if rule not in self._rules: self._rules.append(rule)

    def remove_rule(self, rule: Rule) -> None:
        if rule in self._rules: self._rules.remove(rule)
>>>>>>> feature/lab1-markov

    def find_rule(self) -> Optional[Rule]:
        key = (self._state, self._tape[self._head])
        for rule in self._rules:
<<<<<<< HEAD
            if rule.initial_state == key:
                return rule
        return None

    def read(self) -> str:
        return self._tape[self._head]

    def write(self, symbol: str) -> None:
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("symbol must be a single character")
=======
            if rule.initial_state == key: return rule
        return None

    def read(self) -> str: return self._tape[self._head]

    def write(self, symbol: str) -> None:
        if not isinstance(symbol, str) or len(symbol) != 1: raise ValueError("symbol must be a single character")
>>>>>>> feature/lab1-markov
        self._tape[self._head] = symbol

    def move_right(self) -> None:
        self._head += 1
<<<<<<< HEAD
        if self._head >= len(self._tape):
            self._tape.append(BLANK)

    def move_left(self) -> None:
        if self._head == 0:
            self._tape.insert(0, BLANK)
        else:
            self._head -= 1

    def set_tape(self, tape: Iterable[str]) -> None:
        tape_list = list(tape)
        if not tape_list:
            raise ValueError("tape cannot be empty")
        for symbol in tape_list:
            if not isinstance(symbol, str) or len(symbol) != 1:
                raise ValueError("Every tape symbol must be a single char")
=======
        if self._head >= len(self._tape): self._tape.append(BLANK)

    def move_left(self) -> None:
        if self._head == 0: self._tape.insert(0, BLANK)
        else: self._head -= 1

    def set_tape(self, tape: Iterable[str]) -> None:
        tape_list = list(tape)
        if not tape_list: raise ValueError("tape cannot be empty")
        for symbol in tape_list:
            if not isinstance(symbol, str) or len(symbol) != 1: raise ValueError("Every tape symbol must be a single char")
>>>>>>> feature/lab1-markov
        self._tape = tape_list
        self._head = 0
        self._steps = 0

    def step(self) -> bool:
<<<<<<< HEAD
        """Execute one transition. Returns False if the machine halts."""
        rule = self.find_rule()
        if rule is None:
            return False

        next_state, new_symbol, direction = rule.target_state
        self.write(new_symbol)

        if direction == "R":
            self.move_right()
        elif direction == "L":
            self.move_left()

=======
        rule = self.find_rule()
        if rule is None: return False
        next_state, new_symbol, direction = rule.target_state
        self.write(new_symbol)
        if direction == "R": self.move_right()
        elif direction == "L": self.move_left()
>>>>>>> feature/lab1-markov
        self._state = next_state
        self._steps += 1
        return True

    def run(self, max_steps: int = 10_000) -> int:
<<<<<<< HEAD
        """Run until halt or ``max_steps``. Returns executed steps."""
        if max_steps <= 0:
            raise ValueError("max_steps must be positive")

        executed = 0
        while executed < max_steps:
            if not self.step():
                break
=======
        if max_steps <= 0: raise ValueError("max_steps must be positive")
        executed = 0
        while executed < max_steps:
            if not self.step(): break
>>>>>>> feature/lab1-markov
            executed += 1
        return executed

    def reset(self, start_state: str = "q0") -> None:
        self._head = 0
        self._state = start_state
        self._steps = 0

<<<<<<< HEAD
    # --- Text representation -------------------------------------------

    def __str__(self) -> str:
        return (
            f"Tape:   {''.join(self._tape)}\n"
            f"Head:   {self._head}\n"
            f"State:  {self._state}\n"
            f"Steps:  {self._steps}"
        )

    def __repr__(self) -> str:
        return (
            f"TuringMachine(tape={self._tape!r}, state={self._state!r}, "
            f"head={self._head})"
        )
=======
    def __str__(self) -> str:
        return f"Tape:   {''.join(self._tape)}\nHead:   {self._head}\nState:  {self._state}\nSteps:  {self._steps}"

    def __repr__(self) -> str:
        return f"TuringMachine(tape={self._tape!r}, state={self._state!r}, head={self._head})"
>>>>>>> feature/lab1-markov
