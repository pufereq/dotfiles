#!/usr/bin/env python3

# simulat menus
from hashlib import new
import os
from rich import print
from rich.prompt import IntPrompt

from dialogs.game import new_game

def main_menu():
    # main menu
    print("""
1. New Game
2. Load Game
3. Exit
""")
    choice = IntPrompt.ask('Main Menu', choices=['1', '2', '3'])
    if choice == 1:
        # raise NotImplementedError('Not Implemented')
        new_game()
    elif choice == 2:
        pass # load a game
    elif choice == 3:
        pass # exit