"""Normal Markov Algorithm implementation."""
from __future__ import annotations
from typing import Iterable, List
from .rule import Rule

class MarkovAlgorithm:
    __slots__ = ("_rules", "_text", "_steps")

    def __init__(self, text: str, rules: Iterable[Rule] = ()) -> None:
        self._text = text
        self._rules: List[Rule] = list(rules)
        self._steps = 0

    @property
    def text(self) -> str: return self._text
    @property
    def rules(self) -> tuple[Rule, ...]: return tuple(self._rules)
    @property
    def steps(self) -> int: return self._steps

    def add_rule(self, rule: Rule) -> None:
        if not isinstance(rule, Rule): raise TypeError("Expected a Rule instance")
        self._rules.append(rule)

    def set_text(self, text: str) -> None:
        self._text = text
        self._steps = 0

    def step(self) -> bool:
        for rule in self._rules:
            new_text, applied = rule.apply_to(self._text)
            if applied:
                self._text = new_text
                self._steps += 1
                return not rule.terminal
        return False

    def run(self, max_steps: int = 10_000) -> str:
        if max_steps <= 0: raise ValueError("max_steps must be positive")
        executed = 0
        while executed < max_steps:
            if not self.step(): break
            executed += 1
        return self._text
