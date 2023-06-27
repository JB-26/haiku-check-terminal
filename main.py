from rich import print
from rich.console import Console
from rich.panel import Panel

from check import checkHaiku


def main():
	"""
	The main function for the application
	"""
	console = Console()
	while True:
		console.print(Panel.fit("Welcome to [bold green]Haiku Check![/bold green]"))
		console.print(Panel.fit("[italic yellow]Please type the letters that are highlighted in green to access the functions[/italic yellow]\n[bold green]C[/bold green]heck Haiku\n[bold green]Q[/bold green]uit", title="Haiku Check ⛩️", subtitle="By Joshua Blewitt"))

		choice = input().upper()

		if choice == 'C':
			checkHaiku()
		elif choice == 'Q':
			console.print("Goodbye!")
			break
		else:
			console.print("[bold red]Your command was invalid! Please try again![/bold red]")

if __name__ == "__main__":
    main()