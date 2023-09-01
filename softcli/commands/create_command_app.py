from enum import Enum
from logging_helper import get_logger
from modules.dart import create_dart_app
from pathlib import Path
from rich.console import Console
from tui import Assets
from typer import Argument, Exit, Typer, Option
from typing_extensions import Annotated
from utils import soft_file_manager, cwd

console = Console()
command_language = None
create_app = Typer(rich_markup_mode="rich")
logger = get_logger(__file__)


class CliLanguage(Enum):
    dart = create_dart_app
    flutter = None
    react = None


def set_cli_language(language: str):
    if language == "dart":
        return CliLanguage.dart.value
    elif language == "flutter":
        return CliLanguage.flutter.value
    elif language == "react":
        return CliLanguage.react.value
    else:
        logger.error("Language provided not supported by SoftCli.")


@create_app.command(help=Assets.project_help)
def project(name: Annotated[str, Argument(..., help="")]) -> None:
    project_path = Path(f"{cwd}/{name}")
    if project_path.exists():
        logger.error(f"Project {name} already exist. Run cd {name}.")
        raise Exit(code=1)
    language = soft_file_manager(name, Path(project_path))
    command_language = set_cli_language(language[0])
    command_language.project(name)
    raise Exit()


@create_app.command(help=Assets.module_help)
def module(
    name: Annotated[str, Argument(..., help="")],
    domain: Annotated[
        bool,
        Option(
            "--domain",
            help="Make only domain folder in module.",
        ),
    ] = False,
    infra: Annotated[
        bool,
        Option(
            "--infra",
            help="Make only infra folder in module.",
        ),
    ] = False,
    external: Annotated[
        bool,
        Option("--external", help="Make only external folder in module."),
    ] = False,
):
    language = soft_file_manager(Path(cwd))[0]
    command_language = set_cli_language(language)
    try:
        command_language.module(name, domain, infra, external)
    except Exception as error:
        logger.error(f"{error}. ** add on try bloc in module command.")
        raise Exit(code=1)
    else:
        raise Exit()


@create_app.command(help=Assets.datasource_help)
def datasource(
    name: Annotated[str, Argument(..., help=Assets.datasource_name_help)],
    module_name: Annotated[
        str,
        Argument(..., help=Assets.datasource_module_name_help),
    ],
) -> None:
    language = soft_file_manager(Path(cwd))
    command_language = set_cli_language(language[0])
    command_language.datasource(name, module_name)


@create_app.command(help=Assets.repository_help)
def repository(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    language = soft_file_manager(Path(cwd))
    command_language = set_cli_language(language[0])
    command_language.repository(name, module_name)
    raise Exit()


@create_app.command(help=Assets.driver_help)
def driver(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    language = soft_file_manager(Path(cwd))
    command_language = set_cli_language(language[0])
    command_language.driver(name, module_name)
    raise Exit()


@create_app.command(help=Assets.presentation_help)
def presentation(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    language = soft_file_manager(Path(cwd))
    command_language = set_cli_language(language[0])
    command_language.presentation(name, module_name)
    raise Exit()


@create_app.command(help=Assets.usecase_help)
def usecase(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    language = soft_file_manager(Path(cwd))
    command_language = set_cli_language(language[0])
    command_language.usecase(name, module_name)
    raise Exit()


@create_app.command(help=Assets.error_help)
def error(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    language = soft_file_manager(Path(cwd))
    command_language = set_cli_language(language[0])
    command_language.error(name, module_name)
    raise Exit()
