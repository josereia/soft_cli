from logging_helper import get_logger
from modules.dart.create_dart_functions import create_project_manager, make_module
from pathlib import Path
from sys import argv
from typer import Argument, Exit, Option
from typing_extensions import Annotated

logger = get_logger(__file__)


def project(name: Annotated[str, Argument(..., help="")]) -> None:
    try:
        create_project_manager(Path(f"{Path.cwd()}/{name}"), name)
    except Exception as error:
        logger.error(
            f"{error}. ** Add error on try block in create_project(dart)",
        )
        raise Exit(code=1)
    raise Exit()


def module(
    name: Annotated[str, Argument(..., help="")],
    domain: Annotated[bool, Option("--domain")] = False,
    infra: Annotated[bool, Option("--infra")] = False,
    external: Annotated[bool, Option("--external")] = False,
) -> None:
    if len(argv) - 1 > 4:
        logger.error(
            f"You send {len(argv) - 1} arguments but only 2 are supported.",
        )
        raise Exit(code=1)
    if not domain and infra and external:
        try:
            make_module(name)
        except Exception as error:
            logger.error(
                f"{error}. **Add error on try block in create_project(dart)",
            )
            raise Exit(code=1)
    else:
        if domain:
            logger.info("domain")
        elif infra:
            logger.info("infra")
        elif external:
            logger.info("external")
    raise Exit()


def datasource(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()


def repository(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()


def driver(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()


def presentation(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()


def usecase(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()


def error(name: Annotated[str, Argument(..., help="")]) -> None:
    raise Exit()
