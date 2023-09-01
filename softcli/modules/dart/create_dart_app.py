from logging_helper import get_logger
from modules.dart.create_dart_functions import (
    class_name_formatter,
    create_project_manager,
    cwd,
    make_domain,
    make_external,
    make_infra,
    make_module,
    make_couple_files,
)
from pathlib import Path
from rich.console import Console
from sys import argv
from tui import Assets
from typer import Argument, Exit, Option
from typing_extensions import Annotated
from utils import get_config_info, make_folder, make_class_file

console = Console()
logger = get_logger(__file__)


def project(name: Annotated[str, Argument(..., help="")]) -> None:
    """Create a dart project"""
    try:
        create_project_manager(Path(f"{cwd}/{name}"), name)
    except Exception as error:
        logger.error(
            f"{error}. ** Add error on try block in create_project(dart)",
        )
        raise Exit(code=1)
    else:
        logger.debug("Created a dart project. [dart create <name>]")
    raise Exit()


def module(
    name: Annotated[str, Argument(..., help="")],
    domain: Annotated[bool, Option("--domain")] = False,
    infra: Annotated[bool, Option("--infra")] = False,
    external: Annotated[bool, Option("--external")] = False,
) -> None:
    """Create a clean dart module"""
    if len(argv) - 1 > 4:
        logger.error(
            f"You send {len(argv) - 1} arguments but only 2 are supported.",
        )
        raise Exit(code=1)
    if domain and infra and external is not True:
        try:
            print("make_module")
            make_module(name)
        except Exception as error:
            logger.error(
                f"{error}. **Add error on try block in create_project(dart)",
            )
            raise Exit(code=1)
    else:
        if domain:
            print("domain")
            make_domain(name)
        elif infra:
            make_infra(name)
        elif external:
            make_external(name)


def datasource(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=Assets.datasource_module_name_help),
    ],
) -> None:
    project_name = get_config_info()[2]
    abstract_class = class_name_formatter(name)
    impl_class = class_name_formatter(f"{name}_impl")

    make_couple_files(
        name,
        project_name,
        module_name,
        abstract_class,
        "infra/datasources",
        "abstract_template.dart",
        impl_class,
        "external/datasources",
        "datasource_impl_template.dart",
    )
    console.print("[green]✓ Datasources files created successfully.")
    raise Exit()


def repository(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    project_name = get_config_info()[2]
    abstract_class = class_name_formatter(name)
    impl_class = class_name_formatter(f"{name}_impl")
    make_couple_files(
        name,
        project_name,
        module_name,
        abstract_class,
        "domain/repositories",
        "abstract_template.dart",
        impl_class,
        "infra/repositories",
        "repository_impl_template.dart",
    )
    console.print("[green]✓ Repository files created successfully.")
    raise Exit()


def driver(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    project_name = get_config_info()[2]
    abstract_class = class_name_formatter(name)
    impl_class = class_name_formatter(f"{name}_impl")
    make_couple_files(
        name,
        project_name,
        module_name,
        abstract_class,
        "infra/drivers",
        "abstract_template.dart",
        impl_class,
        "external/drivers",
        "drivers_impl_template.dart",
    )
    console.print("[green]✓ Driver files created successfully.")
    raise Exit()


def presentation(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    class_name = class_name_formatter(name)
    make_class_file(
        name,
        Path(f"{cwd}/lib/modules/{module_name}/presentation"),
        "presentation_template.dart",
        {
            "class_name": class_name,
        },
    )
    raise Exit()


def usecase(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    project_name = get_config_info()[2]
    abstract_class = class_name_formatter(name)
    impl_class = class_name_formatter(f"{name}_impl")
    make_folder(
        name,
        "domain",
        Path(f"{cwd}/lib/modules/{module_name}/domain/usecases"),
    )
    make_couple_files(
        name,
        project_name,
        module_name,
        abstract_class,
        f"domain/usecases/{name}",
        "usecase_template.dart",
        impl_class,
        f"domain/usecases/{name}",
        "usecase_impl_template.dart",
        name,
    )
    console.print("[green]✓ Usecase files created successfully.")
    raise Exit()


def error(
    name: Annotated[str, Argument(..., help="")],
    module_name: Annotated[
        str,
        Argument(..., help=""),
    ],
) -> None:
    project_name = get_config_info()[2]
    abstract_class = class_name_formatter(name)
    impl_class = class_name_formatter(f"{name}_impl")
    make_couple_files(
        name,
        project_name,
        module_name,
        abstract_class,
        "domain/errors",
        "error_template.dart",
        impl_class,
        "domain/errors",
        "error_impl_template.dart",
    )
    console.print("[green]✓ Error files created successfully.")
    raise Exit()


if __name__ == "__main__":
    ...
