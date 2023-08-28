from rich.console import Console
import typer
from os import path

# modules
from modules.dart.dart_module import app as dart_module

ROOT_DIR: str = path.dirname(path.abspath(__file__))

console = Console()
app = typer.Typer()

# typers
app.add_typer(dart_module, name="dart")


if __name__ == "__main__":
    app()
