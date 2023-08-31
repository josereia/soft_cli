"""Class with all functions for create command in version dart"""
from logging_helper import get_logger
from models.dart.path_getter import MODELS_DIR
from pathlib import Path
from rich.console import Console
from rich.progress import Progress
import shutil
import subprocess
from utils import make_folder

console = Console()
logger = get_logger(__file__)


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


def create_module(name: str = "new_project"):
    ...


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
        Path(f"{Path.cwd()}/{name}/analysis_options.yaml"),
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
            "[green] ✓" + f" Project [b]{name}[/b] created successfully![/]",
        )


def make_domain(module_name: str):
    path_domain = Path(f"{Path.cwd()}/lib/modules/{module_name}")
    path_subfolders = Path(f"{Path.cwd()}/lib/modules/{module_name}/domain")

    make_folder("domain", module_name, path_domain)
    make_folder("entities", module_name, path_subfolders)
    make_folder("usecases", module_name, path_subfolders)
    make_folder("repositories", module_name, path_subfolders)
    make_folder("errors", module_name, path_subfolders)
    console.print(
        f"[green]✓ Folder domain created in {module_name} successfully.[/]",
    )


def make_infra(module_name: str):
    path_infra = Path(f"{Path.cwd()}/lib/modules/{module_name}")
    path_subfolders = Path(f"{Path.cwd()}/lib/modules/{module_name}/infra")

    make_folder("infra", module_name, path_infra)
    make_folder("datasources", module_name, path_subfolders)
    make_folder("models", module_name, path_subfolders)
    make_folder("repositories", module_name, path_subfolders)
    console.print(
        f"[green]✓ Folder infra created in {module_name} successfully.[/]",
    )


def make_external(module_name: str):
    path_external = Path(f"{Path.cwd()}/lib/modules/{module_name}")
    path_subfolders = Path(f"{Path.cwd()}/lib/modules/{module_name}/external")

    make_folder("external", module_name, path_external)
    make_folder("datasources", module_name, path_subfolders)
    make_folder("drivers", module_name, path_subfolders)
    console.print(
        f"[green]✓ Folder external created in {module_name} successfully.[/]",
    )


def make_module(name: str):
    make_folder(name=name, path=Path(f"{Path.cwd()}/lib/modules"))
    make_domain(name)
    make_infra(name)
    make_external(name)
    make_folder(
        "presentation",
        name,
        Path(
            f"{Path.cwd()}/lib/modules/{name}",
        ),
    )
    console.print(
        f"[green]✓ Module {name} created successfully.[/]",
    )


# another function make_folders(module_name, main_name, path_main, path_sub)
if __name__ == "__main__":
    ...
