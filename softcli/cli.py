from commands.create_command_app import create_app
from logging_helper import get_logger
from rich.console import Console
from tui import Assets
from typer import Argument, Exit, Option, Typer
from typing_extensions import Annotated
from utils import make_softfile

logger = get_logger(__file__)


console = Console()
cli = Typer(
    rich_markup_mode="rich",
)
cli.add_typer(
    typer_instance=create_app,
    name="create",
    help="""
    Command to create datasource, driver, error, module, presentation,
     project, repository, usecase
    """,
)


@cli.command()
def soft(
    name: Annotated[str, Argument(..., help="Name of project")],
    config: Annotated[
        bool,
        Option(
            "--config",
            help="Uses for generate a softfile (env_file)",
        ),
    ] = False,
):
    if config:
        make_softfile(name)
    else:
        console.print(f"[purple4 b]{Assets.logo}\n[/]", justify="center")
        console.print(f"[b]{Assets.intro_txt}[/]")
    raise Exit()


if __name__ == "__main__":
    cli()
