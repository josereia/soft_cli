from modules.dart.create_dart_functions import create_project_manager
from typer import Argument, Exit, Typer
from typing_extensions import Annotated

create_dart_app = Typer()


@create_dart_app.command(
    help="Create a project in the language/framework configured in softfile.",
)
def project(name: Annotated[str, Argument(..., help="")]) -> None:
    create_project_manager(name)
    raise Exit()


@create_dart_app.command(help="Create module folder in project folder.")
def module(name=Argument(..., help="")) -> None:
    raise Exit()


@create_dart_app.command(help="Create datasource files in module folder.")
def datasource(name=Argument(..., help="")) -> None:
    raise Exit()


@create_dart_app.command(help="Create repository files in module folder.")
def repository(name=Argument(..., help="")) -> None:
    raise Exit()


@create_dart_app.command(help="Create driver file in module folder.")
def driver(name=Argument(..., help="")) -> None:
    raise Exit()


@create_dart_app.command(help="Create presentation file in module folder.")
def presentation(name=Argument(..., help="")) -> None:
    raise Exit()


@create_dart_app.command(help="Create usecase files in module folder.")
def usecase(name=Argument(..., help="")) -> None:
    raise Exit()


@create_dart_app.command(help="Create error file in module folder.")
def error(name=Argument(..., help="")) -> None:
    raise Exit()
