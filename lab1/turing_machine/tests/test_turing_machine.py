<<<<<<< HEAD
﻿"""Unit tests for :class:`TuringMachine`."""

import copy

import pytest

from lab1.turing_machine.rule import Rule
from lab1.turing_machine.turing_machine import TuringMachine


=======
﻿"""Unit tests for TuringMachine."""
import copy
import pytest
from lab1.turing_machine.rule import Rule
from lab1.turing_machine.turing_machine import TuringMachine

>>>>>>> feature/lab1-markov
def make_machine():
    rules = [
        Rule(("q0", "0"), ("q0", "1", "R")),
        Rule(("q0", "1"), ("q0", "0", "R")),
    ]
    return TuringMachine("0101", rules)

<<<<<<< HEAD

=======
>>>>>>> feature/lab1-markov
def test_init_defaults():
    m = TuringMachine("_", [])
    assert m.tape == ("_",)
    assert m.head == 0
    assert m.state == "q0"
    assert m.steps == 0

<<<<<<< HEAD

def test_init_validations():
    with pytest.raises(ValueError):
        TuringMachine("", [])
    with pytest.raises(ValueError):
        TuringMachine(["ab"], [])
    with pytest.raises(ValueError):
        TuringMachine("_", [], start_state="")

=======
def test_init_validations():
    with pytest.raises(ValueError): TuringMachine("", [])
    with pytest.raises(ValueError): TuringMachine(["ab"], [])
    with pytest.raises(ValueError): TuringMachine("_", [], start_state="")
>>>>>>> feature/lab1-markov

def test_copy_constructor_and_assignment():
    m1 = make_machine()
    m1.step()
    m2 = TuringMachine.from_machine(m1)
    assert m1 == m2
<<<<<<< HEAD

    m3 = TuringMachine("_", [])
    m3.copy_from(m1)
    assert m3 == m1

    m2.step()
    assert m2 != m1

    with pytest.raises(TypeError):
        TuringMachine.from_machine("nope")
    with pytest.raises(TypeError):
        m3.copy_from("nope")


def test_deep_and_shallow_copy():
    m1 = make_machine()
    m2 = copy.copy(m1)
    m3 = copy.deepcopy(m1)
    assert m2 == m1
    assert m3 == m1

=======
    m3 = TuringMachine("_", [])
    m3.copy_from(m1)
    assert m3 == m1
    m2.step()
    assert m2 != m1
    with pytest.raises(TypeError): TuringMachine.from_machine("nope")
    with pytest.raises(TypeError): m3.copy_from("nope")

def test_deep_and_shallow_copy():
    m1 = make_machine()
    assert copy.copy(m1) == m1
    assert copy.deepcopy(m1) == m1
>>>>>>> feature/lab1-markov

def test_read_write_and_tape_ops():
    m = TuringMachine("0", [])
    assert m.read() == "0"
    m.write("1")
    assert m.read() == "1"
<<<<<<< HEAD

    with pytest.raises(ValueError):
        m.write("ab")

    m.move_right()
    assert m.head == 1
    assert m.tape == ("1", "_")

=======
    with pytest.raises(ValueError): m.write("ab")
    m.move_right()
    assert m.head == 1
    assert m.tape == ("1", "_")
>>>>>>> feature/lab1-markov
    m.move_right()
    m.move_left()
    assert m.head == 1

<<<<<<< HEAD

=======
>>>>>>> feature/lab1-markov
def test_move_left_at_start_extends_tape():
    m = TuringMachine("0", [])
    m.move_left()
    assert m.tape[0] == "_"
    assert m.head == 0

<<<<<<< HEAD

=======
>>>>>>> feature/lab1-markov
def test_add_remove_and_find_rule():
    m = TuringMachine("0", [])
    r = Rule(("q0", "0"), ("q0", "1", "R"))
    m.add_rule(r)
    m.add_rule(r)
    assert len(m.rules) == 1
    assert m.find_rule() == r
<<<<<<< HEAD

    with pytest.raises(TypeError):
        m.add_rule("nope")

=======
    with pytest.raises(TypeError): m.add_rule("nope")
>>>>>>> feature/lab1-markov
    m.remove_rule(r)
    assert m.rules == ()
    m.remove_rule(r)
    assert m.find_rule() is None

<<<<<<< HEAD

=======
>>>>>>> feature/lab1-markov
def test_step_and_run_to_halt():
    m = make_machine()
    assert m.step() is True
    assert m.read() == "1"
<<<<<<< HEAD

    executed = m.run(max_steps=100)
    assert executed > 0
    assert m.state == "q0"

=======
    executed = m.run(max_steps=100)
    assert executed > 0
    assert m.state == "q0"
>>>>>>> feature/lab1-markov
    m2 = TuringMachine("_", [])
    assert m2.step() is False
    assert m2.run() == 0

<<<<<<< HEAD

def test_run_validates_max_steps():
    m = make_machine()
    with pytest.raises(ValueError):
        m.run(max_steps=0)

=======
def test_run_validates_max_steps():
    m = make_machine()
    with pytest.raises(ValueError): m.run(max_steps=0)
>>>>>>> feature/lab1-markov

def test_set_tape_and_reset():
    m = make_machine()
    m.step()
    m.set_tape("abc")
    assert m.tape == ("a", "b", "c")
<<<<<<< HEAD
    assert m.head == 0
    assert m.steps == 0

    with pytest.raises(ValueError):
        m.set_tape("")
    with pytest.raises(ValueError):
        m.set_tape(["ab"])

=======
    with pytest.raises(ValueError): m.set_tape("")
    with pytest.raises(ValueError): m.set_tape(["ab"])
>>>>>>> feature/lab1-markov
    m.step()
    m.reset()
    assert m.head == 0
    assert m.steps == 0
<<<<<<< HEAD
    assert m.state == "q0"

=======
>>>>>>> feature/lab1-markov

def test_eq_and_str():
    m1 = make_machine()
    m2 = make_machine()
    assert m1 == m2
    assert m1 != "not a machine"
<<<<<<< HEAD

    s = str(m1)
    assert "Tape" in s and "State" in s
    assert "TuringMachine" in repr(m1)


=======
    s = str(m1)
    assert "Tape" in s
    assert "TuringMachine" in repr(m1)

>>>>>>> feature/lab1-markov
def test_full_execution_changes_tape():
    m = make_machine()
    m.run(max_steps=10)
    assert "".join(m.tape[:4]) == "1010"
