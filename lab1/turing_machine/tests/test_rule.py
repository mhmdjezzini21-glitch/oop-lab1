<<<<<<< HEAD
"""Unit tests for :class:`Rule`."""

import pytest

from lab1.turing_machine.rule import Rule


=======
﻿"""Unit tests for Rule."""
import pytest
from lab1.turing_machine.rule import Rule

>>>>>>> feature/lab1-markov
def test_create_and_properties():
    r = Rule(("q0", "0"), ("q0", "1", "R"))
    assert r.initial_state == ("q0", "0")
    assert r.target_state == ("q0", "1", "R")

<<<<<<< HEAD

=======
>>>>>>> feature/lab1-markov
def test_equality_and_hash():
    r1 = Rule(("q0", "0"), ("q0", "1", "R"))
    r2 = Rule(("q0", "0"), ("q0", "1", "R"))
    r3 = Rule(("q0", "1"), ("q0", "0", "R"))
<<<<<<< HEAD

=======
>>>>>>> feature/lab1-markov
    assert r1 == r2
    assert r1 != r3
    assert hash(r1) == hash(r2)
    assert r1 != "not a rule"

<<<<<<< HEAD

def test_validation_errors():
    with pytest.raises(ValueError):
        Rule(("q0",), ("q0", "1", "R"))
    with pytest.raises(ValueError):
        Rule(("q0", "0"), ("q0", "1"))
    with pytest.raises(ValueError):
        Rule(("", "0"), ("q0", "1", "R"))
    with pytest.raises(ValueError):
        Rule(("q0", "00"), ("q0", "1", "R"))
    with pytest.raises(ValueError):
        Rule(("q0", "0"), ("q0", "1", "X"))
    with pytest.raises(ValueError):
        Rule(("q0", "0"), ("", "1", "R"))

=======
def test_validation_errors():
    with pytest.raises(ValueError): Rule(("q0",), ("q0", "1", "R"))
    with pytest.raises(ValueError): Rule(("q0", "0"), ("q0", "1"))
    with pytest.raises(ValueError): Rule(("", "0"), ("q0", "1", "R"))
    with pytest.raises(ValueError): Rule(("q0", "00"), ("q0", "1", "R"))
    with pytest.raises(ValueError): Rule(("q0", "0"), ("q0", "1", "X"))
    with pytest.raises(ValueError): Rule(("q0", "0"), ("", "1", "R"))
>>>>>>> feature/lab1-markov

def test_from_string_roundtrip():
    r = Rule.from_string("q0,0 -> q1,1,R")
    assert r.initial_state == ("q0", "0")
    assert r.target_state == ("q1", "1", "R")
    assert r.to_string() == "q0,0 -> q1,1,R"

<<<<<<< HEAD

def test_from_string_errors():
    with pytest.raises(ValueError):
        Rule.from_string("garbage")
    with pytest.raises(ValueError):
        Rule.from_string("q0 -> q1,1,R")
    with pytest.raises(ValueError):
        Rule.from_string("q0,0 -> q1,1")


def test_repr_contains_state():
    r = Rule(("q0", "0"), ("q0", "1", "R"))
    assert "q0" in repr(r)
=======
def test_from_string_errors():
    with pytest.raises(ValueError): Rule.from_string("garbage")
    with pytest.raises(ValueError): Rule.from_string("q0 -> q1,1,R")
    with pytest.raises(ValueError): Rule.from_string("q0,0 -> q1,1")

def test_repr_contains_state():
    r = Rule(("q0", "0"), ("q0", "1", "R"))
    assert "q0" in repr(r)
>>>>>>> feature/lab1-markov
