#!/usr/bin/env python3

# simulat menus
import os
from rich import print
from rich.prompt import IntPrompt

def main_menu():
    # main menu
    os.system('clear')
    print("""
1. New Game
2. Load Game
3. Exit
""")
    choice = IntPrompt.ask('Main Menu', choices=['1', '2', '3'])
    if choice == 1:
        raise Exception('Not miplememe') # create a new game
    elif choice == 2:
        pass # load a game
    elif choice == 3:
        pass # exit