#!/usr/bin/env python3
"""
Flashcard study tool.
- All cards live in flashcards.json (same directory as this script)
Run: python3 flashcards.py [topic_filter]
"""

import json
import os
import random
import sys

JSON_PATH = os.path.join(os.path.dirname(__file__), "flashcards.json")

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RED    = "\033[91m"
DIM    = "\033[2m"


def load_cards(topic_filter=None):
    if not os.path.exists(JSON_PATH):
        print(f"flashcards.json not found at {JSON_PATH}")
        sys.exit(1)
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)
    cards = []
    for entry in data:
        if topic_filter and topic_filter.lower() not in entry["id"].lower():
            continue
        cards.append((entry["id"], entry["question"], entry["answer"]))
    return cards


def run_session(cards):
    random.shuffle(cards)
    total   = len(cards)
    correct = 0
    skipped = 0

    print(f"\n{BOLD}{CYAN}=== Flashcard Session: {total} card(s) ==={RESET}")
    print(f"{DIM}Commands: press Enter to reveal answer, then y/n/s (skip){RESET}\n")

    for i, (name, question, answer) in enumerate(cards, 1):
        print(f"{BOLD}[{i}/{total}] {DIM}({name}){RESET}")
        print(f"{BOLD}{CYAN}Q: {question}{RESET}")

        try:
            input(f"{DIM}  [Enter to reveal]{RESET} ")
        except (KeyboardInterrupt, EOFError):
            print("\nQuitting early.")
            break

        print(f"{GREEN}A: {answer}{RESET}\n")

        while True:
            try:
                resp = input(f"  Did you get it right? [{GREEN}y{RESET}/{RED}n{RESET}/{YELLOW}s{RESET}kip]: ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                resp = "s"
            if resp in ("y", "yes"):
                correct += 1
                break
            elif resp in ("n", "no"):
                break
            elif resp in ("s", "skip", ""):
                skipped += 1
                break
            else:
                print("  Please enter y, n, or s.")

        print()

    answered = total - skipped
    pct = int(correct / answered * 100) if answered else 0
    print(f"{BOLD}=== Results ==={RESET}")
    print(f"  Correct : {GREEN}{correct}{RESET} / {answered} answered")
    print(f"  Skipped : {YELLOW}{skipped}{RESET}")
    print(f"  Score   : {BOLD}{pct}%{RESET}\n")


def main():
    topic_filter = sys.argv[1] if len(sys.argv) > 1 else None

    cards = load_cards(topic_filter)

    if not cards:
        if topic_filter:
            print(f"No cards found matching '{topic_filter}'.")
        else:
            print("No cards found. Add entries to flashcards.json.")
        sys.exit(1)

    while True:
        run_session(cards)
        try:
            again = input("Study again? (y/n): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            again = "n"
        if again not in ("y", "yes"):
            print("Good luck!")
            break


if __name__ == "__main__":
    main()
