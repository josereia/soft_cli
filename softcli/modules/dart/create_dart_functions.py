"""Class with all functions for create command in version dart"""
from logging_helper import get_logger
from models.dart.path_getter import MODELS_DIR
from pathlib import Path
from rich.console import Console
from rich.progress import Progress
import shutil
import subprocess
from typer import Exit
from utils import make_folder, make_class_file, cwd

console = Console()
logger = get_logger(__file__)


# utils
def class_name_formatter(name: str) -> str:
    capitalize_parts = [part.capitalize() for part in name.split("_")]
    class_name = "".join(capitalize_parts)
    return class_name


def make_couple_files(
    name: str,
    project_name: str,
    module_name: str,
    abstract_class: str,
    path_abs: str,
    abstract_template: str,
    impl_class: str,
    path_impl: str,
    impl_template: str,
    folder_name: str = "",
):
    # make a abstract class file
    try:
        make_class_file(
            name,
            Path(f"{cwd}/lib/modules/{module_name}/{path_abs}"),
            abstract_template,
            {
                "class_name": abstract_class,
            },
        )
    except IOError:
        logger.error("Error writing file.")
        raise Exit(code=1)
    else:
        logger.debug(f"File {name}.dart created successfully.")

    # make a implements class file
    if not folder_name:
        try:
            make_class_file(
                f"{name}_impl",
                Path(
                    f"{cwd}/lib/modules/{module_name}/{path_impl}",
                ),
                impl_template,
                {
                    "class_name": impl_class,
                    "project_name": project_name,
                    "module_name": module_name,
                    "import_file": f"{name}.dart",
                    "abstract_class": abstract_class,
                },
            )
        except IOError as error:
            logger.error(f"{error}. Error writing file.")
            raise Exit(code=1)
        except Exception as error:
            if error == ".":
                logger.debug("Rethrow error from make_class_file.")

            logger.info(
                "On make class file throw error in path or file already exist",
            )
            raise Exit(code=1)
        else:
            logger.debug(f"File {name}_impl.dart created successfully.")

    if folder_name:
        try:
            make_class_file(
                f"{name}_impl",
                Path(
                    f"{cwd}/lib/modules/{module_name}/{path_impl}",
                ),
                impl_template,
                {
                    "class_name": impl_class,
                    "project_name": project_name,
                    "module_name": module_name,
                    "import_file": f"{name}.dart",
                    "abstract_class": abstract_class,
                    "folder_name": folder_name,
                },
            )
        except IOError as error:
            logger.error(f"{error}. Error writing file.")
            raise Exit(code=1)
        except Exception as error:
            logger.error(
                f"{error}. **Add error on try block in make_couple_files",
            )
            raise Exit(code=1)
        else:
            logger.debug(f"File {name}_impl.dart created successfully.")


# functions to command project
def create_dart_project(name: str = "new_project") -> bool:
    """Create a dart project"""
    try:
        subprocess.run(
            f"dart create {name} --force",
            shell=True,
            stdout=subprocess.DEVNULL,
        )
    except Exception as e:
        logger.error(
            f"{e} -> Add in try on create_dart_functions(create_dart_project)",
        )
        return False
    else:
        return True


def create_folders(name: str = "new_project"):
    """Create folders lib, core and modules."""
    Path(f"{Path.cwd()}/{name}/lib/core").mkdir(
        parents=True,
        exist_ok=True,
    )
    Path(f"{Path.cwd()}/{name}/lib/modules").mkdir(
        parents=True,
        exist_ok=True,
    )


def get_dependencies(name: str = "new_project"):
    """Run dart pub get"""
    subprocess.run(
        "dart pub get",
        cwd=f"{name}",
        shell=True,
        stdout=subprocess.DEVNULL,
    )


def git_init(name: str = "new_project"):
    """Run git init and initialize a repository"""
    subprocess.run(
        "git init",
        cwd=f"{name}",
        shell=True,
        stdout=subprocess.DEVNULL,
    )


def copy_analysis_options(name: str = "new_project"):
    """Make a copy to analysis_options.yaml from assets of cli"""
    shutil.copyfile(
        Path(f"{MODELS_DIR}/analysis_options.yaml"),
        Path(f"{cwd}/{name}/analysis_options.yaml"),
    )


def add_very_good_analysis(name: str = "new_project"):
    """Run dart add to install very_good_analysis"""
    subprocess.run(
        "dart pub add very_good_analysis",
        cwd=f"{name}",
        shell=True,
        stdout=subprocess.DEVNULL,
    )


def create_project_manager(path: Path, name: str = "new_project"):
    with Progress() as progress:
        task1 = progress.add_task(
            "[purple4 bold]Creating project files[/]",
            total=4,
        )
        task2 = progress.add_task(
            "[purple4 bold]Setting up project[/]",
            total=4,
        )
        progress.update(task1, advance=1)
        create_dart_project(name)
        progress.update(task1, advance=1)
        create_folders(name)
        progress.update(task1, advance=1)
        copy_analysis_options(name)
        progress.update(task1, advance=1)
        progress.update(task2, advance=1)
        add_very_good_analysis(name)
        progress.update(task2, advance=1)
        get_dependencies(name)
        progress.update(task2, advance=1)
        git_init(name)
        progress.update(task2, advance=1)
        progress.stop()
        console.print(
            "[green] ✓"
            + f" Project [b]{name}[/b] created successfully![/]"
            + f" Run [italic b dim]cd {name}[/].",
        )


# functions to make_module
def make_domain(module_name: str):
    path_domain = Path(f"{cwd}/lib/modules/{module_name}")
    path_subfolders = Path(f"{cwd}/lib/modules/{module_name}/domain")

    if not path_domain.exists():
        path_domain.mkdir()

    try:
        make_folder("domain", module_name, path_domain)
        make_folder("entities", module_name, path_subfolders)
        make_folder("usecases", module_name, path_subfolders)
        make_folder("repositories", module_name, path_subfolders)
        make_folder("errors", module_name, path_subfolders)
    except Exception as error:
        logger.error(f"{error}. ** add error on try bloc in make_domain.")
    else:
        console.print(
            "[green]✓ Folder domain created  \
            in {module_name} successfully.[/]",
        )


def make_infra(module_name: str):
    path_infra = Path(f"{cwd}/lib/modules/{module_name}")
    path_subfolders = Path(f"{cwd}/lib/modules/{module_name}/infra")

    if not path_infra.exists():
        path_infra.mkdir()

    try:
        make_folder("infra", module_name, path_infra)
        make_folder("datasources", module_name, path_subfolders)
        make_folder("models", module_name, path_subfolders)
        make_folder("repositories", module_name, path_subfolders)
        make_folder("drivers", module_name, path_subfolders)
    except Exception as error:
        logger.error(f"{error}. **add error on bloc try in make_infra")
    else:
        console.print(
            f"[green]✓ Folder infra created in {module_name} successfully.[/]",
        )


def make_external(module_name: str):
    path_external = Path(f"{cwd}/lib/modules/{module_name}")
    path_subfolders = Path(f"{cwd}/lib/modules/{module_name}/external")

    if not path_external.exists():
        path_external.mkdir()

    try:
        make_folder("external", module_name, path_external)
        make_folder("datasources", module_name, path_subfolders)
        make_folder("drivers", module_name, path_subfolders)
    except Exception as error:
        logger.error(f"{error}. **add error on try bloc in make_external.")
    else:
        console.print(
            f"[green]✓ Folder external created in \
            {module_name} successfully.[/]"
        )


def make_module(name: str):
    make_folder(name=name, path=Path(f"{cwd}/lib/modules"))
    make_domain(name)
    make_infra(name)
    make_external(name)
    make_folder(
        "presentation",
        name,
        Path(
            f"{cwd}/lib/modules/{name}",
        ),
    )
    console.print(
        f"[green]✓ Module {name} created successfully.[/]",
    )


# another function make_folders(module_name, main_name, path_main, path_sub)
if __name__ == "__main__":
    ...
