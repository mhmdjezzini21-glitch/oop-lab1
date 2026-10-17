"""Console UI for the Markov Algorithm."""
from __future__ import annotations
from .rule import Rule
from .markov_algorithm import MarkovAlgorithm

MENU = """
============================
      MARKOV ALGORITHM
============================
 1. Show current state
 2. Make one step
 3. Run completely
 4. Reset text
 5. Show rules
 6. Exit
============================"""

def run_cli() -> None:
    print("============================================")
    print("     MARKOV ALGORITHM  (Lab 1.8.3)")
    print("============================================")
    text = input("Enter initial text: ")
    rules = [
        Rule("a", "b"),
        Rule("b", "c", terminal=True),
    ]
    algo = MarkovAlgorithm(text, rules)
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print(f"\nText: {algo.text}\nSteps: {algo.steps}")
        elif choice == "2":
            is_running = algo.step()
            print(f"\nText: {algo.text}")
            if not is_running: print("(Algorithm halted)")
        elif choice == "3":
            result = algo.run()
            print(f"\nFinal text: {result}\nTotal steps: {algo.steps}")
        elif choice == "4":
            new_text = input("New text: ")
            algo.set_text(new_text)
            print(f"Text reset to: {algo.text}")
        elif choice == "5":
            print("\nRules:")
            for r in algo.rules: print("  ", r)
        elif choice == "6":
            print("\nGoodbye.")
            break
