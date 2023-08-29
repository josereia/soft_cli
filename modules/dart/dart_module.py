from rich.console import Console
import typer

# commands
from modules.create_command_app import app_create


console = Console()
app = typer.Typer()


# subcommands
app.add_typer(
    app_create,
    name="create",
    help="Create a new module, usecase, repository, datasource or driver.",
)


@app.command()
def init():
    print("init")


if __name__ == "__main__":
    app()
