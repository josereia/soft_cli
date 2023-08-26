from rich.console import Console
import typer

# modules
from modules.dart.dart_module import typer as dart_module

console = Console()
typer = typer.Typer()

# typers
typer.add_typer(dart_module, name="dart")


if __name__ == "__main__":
    typer()
