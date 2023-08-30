from modules.dart.create_dart_app import create_dart_app
from models.tui import logo, intro_txt
from pathlib import Path
from rich.console import Console
from typer import Typer, Option, Exit
from typing_extensions import Annotated
from utils import make_softfile


console = Console()
cli = Typer()
cli.add_typer(
    typer_instance=create_dart_app,
    name="create",
    help="""
    Command to create datasource, driver, error, module, presentation,
     project, repository, usecase
    """,
)


@cli.command()
def soft(
    config: Annotated[
        bool,
        Option(
            "--config",
            help="Uses for generate a softfile (env_file)",
        ),
    ] = False
):
    if config:
        make_softfile(Path.cwd())
    else:
        console.print(f"[purple4 b]{logo}\n[/]", justify="center")
        console.print(f"[b]{intro_txt}[/]")
    raise Exit()


if __name__ == "__main__":
    cli()
