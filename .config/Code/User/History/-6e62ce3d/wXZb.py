from rich.console import Console
import time

con = Console()

with con.status('sus', spinner='arrow'):
    input()