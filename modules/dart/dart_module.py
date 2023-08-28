from rich.console import Console
import typer

# commands
from modules.dart.commands.create_command import app as create_command


console = Console()
app = typer.Typer()


# subcommands
app.add_typer(
    create_command,
    name="create",
    help="Create a new module, usecase, repository, datasource or driver.",
)


@app.command()
def init():
    print("init")


if __name__ == "__main__":
    app()
