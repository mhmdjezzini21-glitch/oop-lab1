"""Console UI for the Turing machine."""
from __future__ import annotations
from .rule import Rule
from .turing_machine import TuringMachine

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

def run_cli() -> None:
    print("============================================")
    print("        TURING MACHINE  (Lab 1.8.2)")
    print("============================================")
    print("Tip: blank symbol is '_'.")
    tape_input = input("Enter the tape (e.g. 0101): ").strip() or "_"

    default_rules = [
        Rule(("q0", "0"), ("q0", "1", "R")),
        Rule(("q0", "1"), ("q0", "0", "R")),
    ]

    machine = TuringMachine(tape_input, default_rules)
    while True:

        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1": print("\n" + str(machine))
        elif choice == "2":

            if machine.step(): print("\nStep performed.")
            else: print("\nNo matching rule — machine halted.")
            print(machine)

        elif choice == "3":

            raw = input("Max steps [100]: ").strip() or "100"
            try: max_steps = int(raw)
            except ValueError: print("Invalid number."); continue
            executed = machine.run(max_steps)
            print(f"\nExecuted {executed} step(s). Machine stopped.")
            print(machine)

        elif choice == "4": print("\nCurrent symbol:", machine.read())

        elif choice == "5":

            new_tape = input("New tape: ").strip() or "_"
            machine.set_tape(new_tape)
            print("Machine reset.")
            print(machine)

        elif choice == "6": print("\nGoodbye."); break

        else: print("\nInvalid choice. Enter a number from 1 to 6.")
