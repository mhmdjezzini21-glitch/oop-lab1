import pytest
from lab1.markov_algorithm.rule import Rule

def test_rule_creation():
    r = Rule("a", "b", terminal=True)
    assert r.left == "a"
    assert r.right == "b"
    assert r.terminal is True

def test_empty_left_raises():
    with pytest.raises(ValueError): Rule("", "b")

def test_from_string():
    r1 = Rule.from_string("ab -> c")
    assert r1.left == "ab"
    assert r1.right == "c"
    assert r1.terminal is False
    r2 = Rule.from_string("x ->. y")
    assert r2.left == "x"
    assert r2.right == "y"
    assert r2.terminal is True

def test_apply_to():
    r = Rule("ab", "x")
    assert r.apply_to("abcab") == ("xcab", True)
    assert r.apply_to("hello") == ("hello", False)
