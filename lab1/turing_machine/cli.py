<<<<<<< HEAD
"""Console UI for the Turing machine.

This module knows nothing about the internal tape representation of
:class:`TuringMachine` — it only uses the public API.
"""

from __future__ import annotations

from .rule import Rule
from .turing_machine import TuringMachine


=======
﻿"""Console UI for the Turing machine."""

from __future__ import annotations
from .rule import Rule
from .turing_machine import TuringMachine

>>>>>>> feature/lab1-markov
MENU = """
============================
        TURING MACHINE
============================
 1. Show machine
 2. Make one step
 3. Run machine (max N steps)
 4. Show current symbol
 5. Reset machine
 6. Exit
============================"""

<<<<<<< HEAD

def run_cli() -> None:
    """Start the interactive console menu."""
    print("============================================")
    print("        TURING MACHINE  ")
    print("============================================")
    print("Tip: blank symbol is '_'.")

    tape_input = input("Enter the tape : ").strip() or "_"

=======
def run_cli() -> None:
    print("============================================")
    print("        TURING MACHINE  (Lab 1.8.2)")
    print("============================================")
    print("Tip: blank symbol is '_'.")
    tape_input = input("Enter the tape (e.g. 0101): ").strip() or "_"
>>>>>>> feature/lab1-markov
    default_rules = [
        Rule(("q0", "0"), ("q0", "1", "R")),
        Rule(("q0", "1"), ("q0", "0", "R")),
    ]
    machine = TuringMachine(tape_input, default_rules)
<<<<<<< HEAD

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print()
            print(machine)

        elif choice == "2":
            if machine.step():
                print("\nStep performed.")
            else:
                print("\nNo matching rule — machine halted.")
            print(machine)

=======
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("\n" + str(machine))
        elif choice == "2":
            if machine.step(): print("\nStep performed.")
            else: print("\nNo matching rule — machine halted.")
            print(machine)
>>>>>>> feature/lab1-markov
        elif choice == "3":
            raw = input("Max steps [100]: ").strip() or "100"
            try:
                max_steps = int(raw)
            except ValueError:
<<<<<<< HEAD
                print("Invalid number.")
                continue
            executed = machine.run(max_steps)
            print(f"\nExecuted {executed} step(s). Machine stopped.")
            print(machine)

        elif choice == "4":
            print("\nCurrent symbol:", machine.read())

=======
                print("Invalid number."); continue
            executed = machine.run(max_steps)
            print(f"\nExecuted {executed} step(s). Machine stopped.")
            print(machine)
        elif choice == "4":
            print("\nCurrent symbol:", machine.read())
>>>>>>> feature/lab1-markov
        elif choice == "5":
            new_tape = input("New tape: ").strip() or "_"
            machine.set_tape(new_tape)
            print("Machine reset.")
            print(machine)
<<<<<<< HEAD

        elif choice == "6":
            print("\nGoodbye.")
            break

        else:
            print("\nInvalid choice. Enter a number from 1 to 6.")
=======
        elif choice == "6":
            print("\nGoodbye."); break
        else:
            print("\nInvalid choice. Enter a number from 1 to 6.")
>>>>>>> feature/lab1-markov
