from rich.console import Console
import time

con = Console()

with con.status('simpleDots'):
    time.sleep(10)