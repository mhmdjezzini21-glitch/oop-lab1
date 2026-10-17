import pytest
from lab1.markov_algorithm.rule import Rule
from lab1.markov_algorithm.markov_algorithm import MarkovAlgorithm

def test_init():
    algo = MarkovAlgorithm("test")
    assert algo.text == "test"
    assert algo.steps == 0

def test_step_no_match():
    algo = MarkovAlgorithm("abc")
    algo.add_rule(Rule("x", "y"))
    assert algo.step() is False

def test_step_with_match():
    algo = MarkovAlgorithm("abc")
    algo.add_rule(Rule("a", "z"))
    assert algo.step() is True
    assert algo.text == "zbc"
    assert algo.steps == 1

def test_terminal_rule_halts():
    algo = MarkovAlgorithm("abc")
    algo.add_rule(Rule("a", "z", terminal=True))
    assert algo.step() is False
    assert algo.text == "zbc"

def test_run_to_completion():
    algo = MarkovAlgorithm("a")
    algo.add_rule(Rule("a", "b"))
    algo.add_rule(Rule("b", "c", terminal=True))
    assert algo.run() == "c"

def test_run_max_steps():
    algo = MarkovAlgorithm("a")
    algo.add_rule(Rule("a", "aa"))
    algo.run(max_steps=5)
    assert len(algo.text) == 6
    assert algo.steps == 5
