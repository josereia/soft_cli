from rich.console import Console
from typer import Typer, run
from os import getcwd, path
from utils.functions import make_soft_file

# modules
from modules.dart.dart_module import app as dart_module

ROOT_DIR: str = path.dirname(path.abspath(__file__))

console = Console()
app = Typer()

# typers
app.add_typer(dart_module, name="dart")


def welcome():
    file_path = f"{getcwd()}/soft_file.yaml"
    if path.exists(file_path):
        ...
    else:
        make_soft_file()


if __name__ == "__main__":
    app()
    run(welcome)
