"""
Create app for command create with your subcommands and config which class uses
"""
from typer import Typer, Argument, Exit
from typing_extensions import Annotated
from enum import Enum
from utils.functions import soft_file_manager
from utils.logging_helper import get_logger
from modules.dart.commands.create_command import DartCreateCommand

command_language_instance = None
app_create = Typer()

logger = get_logger(__file__)


class CliLanguages(Enum):
    dart = DartCreateCommand()
    flutter = None


def set_language_instance(language: str):
    """Set which class provides the subcommand"""
    if language == "dart":
        return CliLanguages.dart.value
    elif language == "flutter":
        return CliLanguages.flutter.value
    else:
        logger.error(
            "Something wrong, language in "
            + "soft_file.yaml is not a supported language."
            + "Go to soft_file.yaml and set language to any language supported"
        )
    raise Exit()


@app_create.command()
def project(
    name: Annotated[str, Argument(..., help="")],
    # database=Annotated[str, Argument(..., help=""), Option("--database")],
) -> None:
    language, database = soft_file_manager(name)
    # elif language is None:
    #     print("You miss set language, please use --language <language>")
    # elif database is None:
    #     print("You miss set database, please use --database <database>")

    command_language_instance = set_language_instance(language)
    command_language_instance.name = name
    command_language_instance.project()
    raise Exit()


@app_create.command()
def module(name=Argument(..., help="")) -> None:
    language, database = soft_file_manager(name)
    command_language_instance = set_language_instance(language)
    command_language_instance.name = name
    command_language_instance.module()
    raise Exit()


@app_create.command()
def datasource(name=Argument(..., help="")) -> None:
    language, database = soft_file_manager(name)
    command_language_instance = set_language_instance(language)
    command_language_instance.name = name
    command_language_instance.datasource()
    raise Exit()


@app_create.command()
def repository(name=Argument(..., help="")) -> None:
    language, database = soft_file_manager(name)
    command_language_instance = set_language_instance(language)
    command_language_instance.name = name
    command_language_instance.repository()
    raise Exit()


@app_create.command()
def driver(name=Argument(..., help="")) -> None:
    language, database = soft_file_manager(name)
    command_language_instance = set_language_instance(language)
    command_language_instance.name = name
    command_language_instance.driver()
    raise Exit()


@app_create.command()
def presentation(name=Argument(..., help="")) -> None:
    language, database = soft_file_manager(name)
    command_language_instance = set_language_instance(language)
    command_language_instance.name = name
    command_language_instance.presentation()
    raise Exit()


@app_create.command()
def usecase(name=Argument(..., help="")) -> None:
    language, database = soft_file_manager(name)
    command_language_instance = set_language_instance(language)
    command_language_instance.name = name
    command_language_instance.usecase()
    raise Exit()


@app_create.command()
def error(name=Argument(..., help="")) -> None:
    language, database = soft_file_manager(name)
    command_language_instance = set_language_instance(language)
    command_language_instance.name = name
    command_language_instance.error()
    raise Exit()
