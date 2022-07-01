from rich.console import Console
import time

con = Console()

with con.status('sus', spinner='line'):
    input()