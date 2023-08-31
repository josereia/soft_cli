from enum import Enum
from logging_helper import get_logger
from modules.dart import create_dart_app
from pathlib import Path
from rich.console import Console
from tui import Assets
from typer import Argument, Exit, Typer, Option
from typing_extensions import Annotated
from utils import soft_file_manager, make_class_file, get_config_info

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


# def class_name_formatter(name: str) -> str:
#     print(name)
#     split_name = name.split("_")
#     capitalize_parts = [x.capitalize() for x in split_name]
#     concat_parts = capitalize_parts[0] + capitalize_parts[1] + capitalize_parts[3]
#     return concat_parts


@create_app.command(help=Assets.project_help)
def project(name: Annotated[str, Argument(..., help="")]) -> None:
    project_path = Path(f"{Path.cwd()}/{name}")
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
    language = soft_file_manager(Path(Path.cwd()))
    command_language = set_cli_language(language[0])
    command_language.module(name, domain, infra, external)
    raise Exit()


@create_app.command(help=Assets.datasource_help)
def datasource(
    name: Annotated[str, Argument(..., help=Assets.datasource_name_help)],
    module_name: Annotated[
        str,
        Argument(..., help=Assets.datasource_module_name_help),
    ],
) -> None:
    config_info = get_config_info()
    project_name = config_info[2]
    # reformular esse bloco
    split_name1 = name.split("_")
    capitalize_parts1 = [x.capitalize() for x in split_name1]
    abstract_class = capitalize_parts1[0] + capitalize_parts1[1]
    split_name = f"{name}_impl".split("_")
    capitalize_parts = [x.capitalize() for x in split_name]
    impl_class = capitalize_parts[0] + capitalize_parts[1] + capitalize_parts[2]
    # ------------------- fim bloco
    try:
        make_class_file(
            name,
            Path(f"{Path.cwd()}/lib/modules/{module_name}/infra/datasources"),
            "datasource_template.dart",
            {
                "class_name": abstract_class,
            },
        )
    except IOError:
        logger.error("Error writing file.")
        raise Exit(code=1)
    except Exception as error:
        logger.error(
            f"{error}. **Add error on try block in datasource command",
        )
        raise Exit(code=1)

    try:
        make_class_file(
            f"{name}_impl",
            Path(f"{Path.cwd()}/lib/modules/{module_name}/external/datasources"),
            "datasource_impl_template.dart",
            {
                "class_name": impl_class,
                "project_name": project_name,
                "module_name": module_name,
                "abstract_file": f"{name}.dart",
                "abstract_class": abstract_class,
            },
        )
    except IOError:
        logger.error("Error writing file.")
        raise Exit(code=1)
    except Exception as error:
        logger.error(
            f"{error}. **Add error on try block in datasource command",
        )
        raise Exit(code=1)
    else:
        console.print("")
    raise Exit()


@create_app.command(help=Assets.repository_help)
def repository(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()


@create_app.command(help=Assets.driver_help)
def driver(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()


@create_app.command(help=Assets.presentation_help)
def presentation(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()


@create_app.command(help=Assets.usecase_help)
def usecase(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()


@create_app.command(help=Assets.error_help)
def error(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()
