from rich.console import Console
from typer import Typer

# modules
from modules.dart.dart_module import app as dart_module


console = Console()
cli = Typer()

# typers
cli.add_typer(dart_module, name="create")


if __name__ == "__main__":
    cli()
