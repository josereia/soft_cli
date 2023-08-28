from typing import Annotated
from rich.console import Console
import typer

# commands
from modules.dart.dart_commands import DartCommands as commands

console = Console()
app = typer.Typer()


@app.command()
def init(
    name: Annotated[str, "The name of the project"],
):
    commands.init(name)


if __name__ == "__main__":
    app()
