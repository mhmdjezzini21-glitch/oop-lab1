# Lab 1 — OOP Fundamentals: Designing a Class

**Variant 1.8.2 — Turing Machine** (Python).

## Structure

- `turing_machine/rule.py` — one transition rule.
- `turing_machine/turing_machine.py` — the machine (tape, head, state, rules).
- `turing_machine/cli.py` — console menu, separated from the domain.
- `turing_machine/tests/` — pytest unit tests.

## Running

```bash
pip install -r requirements.txt
python main.py

pytest --cov=lab1.turing_machine --cov-report=term-missing lab1/turing_machine/tests