import os
from rich.console import Console
console = Console()

def error(message, exit = True):
    console.print(f"[red][bold]✗[/bold]  {message}[/red]\n")
    if exit: os._exit(1)
def success(message, pad=True):
    console.print(f"[green][bold]✓[/bold]  {message}[/green]" + ("\n" if pad else ""))
def info(message, pad=True):
    console.print(f"[blue][bold]ⓘ[/bold]  {message}[/blue]" + ("\n" if pad else ""))