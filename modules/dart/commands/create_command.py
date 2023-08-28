from rich.console import Console
import typer

from modules.dart.commands.create_command_functions import DartCreateCommandFunctions

console = Console()
app = typer.Typer()

functions = DartCreateCommandFunctions("")


@app.command()
def project(name=typer.Argument(..., help="Project name")) -> None:
    functions.name = name
    functions.project()
