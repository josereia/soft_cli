from rich.console import Console

from rich.progress import Progress
from dart_functions import DartFunctions
from commands_abc import CreateCommandsABC
import typer

console = Console()

app = typer.Typer()


class DartCreateCommands2(CreateCommandsABC):
    @app.command()
    def qualquer_coisa(
        name: str,
    ):
        commands = DartFunctions(name)

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
            commands.create_project()
            progress.update(task1, advance=1)
            commands.create_core_folder()
            progress.update(task1, advance=1)
            commands.create_modules_folder()
            progress.update(task1, advance=1)
            commands.copy_analysis_options()
            progress.update(task1, advance=1)
            progress.update(task2, advance=1)
            commands.add_very_good_analysis()
            progress.update(task2, advance=1)
            commands.get_packages()
            progress.update(task2, advance=1)
            commands.git_init()
            progress.update(task2, advance=1)
        console.print(f"[bold green]Project {name} created successfully![/]")
        print("qualquer_coisa")
