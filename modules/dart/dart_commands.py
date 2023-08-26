from rich.console import Console
from rich.progress import Progress
from abc import ABC

# commands
from modules.dart.commands.dart_init_command import DartInitCommand as commands

console = Console()


class DartCommands(ABC):
    @staticmethod
    def init(
        name: str,
    ):
        with Progress() as progress:
            task1 = progress.add_task(
                "[#734AC9 bold]Creating project files[/]",
                total=5,
            )
            task2 = progress.add_task(
                "[#734AC9 bold]Setting up project[/]",
                total=4,
            )
            progress.update(task1, advance=1)
            commands.create_project(name)
            progress.update(task1, advance=1)
            commands.create_core_folder(name)
            progress.update(task1, advance=1)
            commands.create_modules_folder(name)
            progress.update(task1, advance=1)
            commands.copy_analysis_options(name)
            progress.update(task1, advance=1)
            progress.update(task2, advance=1)
            commands.add_very_good_analysis(name)
            progress.update(task2, advance=1)
            commands.get_packages(name)
            progress.update(task2, advance=1)
            commands.git_init(name)
            progress.update(task2, advance=1)
        console.print(f"[bold green]Project {name} created successfully![/]")
