#!/usr/bin/env python3

# simulat menus

from rich import print
from rich.prompt import IntPrompt

def menu():
    # main menu
    print("""
Welcome to...[bold green]
          _                    _         _   
         (_)                  | |       | |  
     ___  _  _ __ ___   _   _ | |  __ _ | |_ 
    / __|| || '_ ` _ \ | | | || | / _` || __|
    \__ \| || | | | | || |_| || || (_| || |_ 
    |___/|_||_| |_| |_| \__,_||_| \__,_| \__|[/bold green]
          [italic]by pufereq [[bold]Work in Progress[/bold]][/italic]

1. New Game
2. Load Game \[wip]
3. Exit
""")
    choice = IntPrompt.ask('Main Menu', choices=['1', '2', '3'])
    if choice == 1:
        raise Exception('Not miplememe') # create a new game
    elif choice == 2:
        pass # load a game
    elif choice == 3:
        pass # exit