
"""Tests for the Markov Algorithm CLI."""

from lab1.markov_algorithm.cli import run_cli


def test_cli_all_menu_options(monkeypatch, capsys):
    """Test all six CLI menu options in one session."""

    user_inputs = iter([
        "a",       # Initial text
        "1",       # Show current state
        "2",       # Make one step: a -> b
        "1",       # Show updated state
        "3",       # Run completely: b -> c
        "2",       # Try another step: algorithm halted
        "4",       # Reset text
        "abc",     # New text
        "5",       # Show rules
        "6",       # Exit
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(user_inputs),
    )

    run_cli()

    output = capsys.readouterr().out

    assert "MARKOV ALGORITHM" in output
    assert "Text: a" in output
    assert "Text: b" in output
    assert "Final text: c" in output
    assert "Total steps: 2" in output
    assert "(Algorithm halted)" in output
    assert "Text reset to: abc" in output
    assert "Rules:" in output
    assert "a -> b" in output
    assert "b ->. c" in output
    assert "Goodbye." in output
