from rich.console import Console
from rich.prompt import Prompt
import typer
from os import getcwd, path
from utils.utils import make_soft_file

# modules
from modules.dart.dart_module import app as dart_module

ROOT_DIR: str = path.dirname(path.abspath(__file__))

console = Console()
app = typer.Typer()

# typers
app.add_typer(dart_module, name="dart")


def welcome():
    file_path = f"{getcwd()}/soft_file.yaml"
    if path.exists(file_path):
        ...
    else:
        language = Prompt.ask(
            "Chose which language your project written:",
            choices=["dart", "javascript", "python"],
        )
        database = Prompt.ask(
            "Chose which database your project uses:",
            choices=["postgresql", "mongodb", "mysql"],
        )
        make_soft_file(language, database)


if __name__ == "__main__":
    app()
    typer.run(welcome)
