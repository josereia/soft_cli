"""Class for create command contains all subcommands in dart version"""
from rich.console import Console
from rich.progress import Progress
from modules.commands_abc import CreateCommandsABC
from modules.dart.commands.create_functions import DartCreateFunctions

console = Console()


class DartCreateCommand(CreateCommandsABC):
    def project(self):
        functions = DartCreateFunctions(self.name)
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
            functions.create_project()
            progress.update(task1, advance=1)
            functions.create_folders()
            progress.update(task1, advance=1)
            functions.copy_analysis_options()
            progress.update(task1, advance=1)
            progress.update(task2, advance=1)
            functions.add_very_good_analysis()
            progress.update(task2, advance=1)
            functions.get_dependencies()
            progress.update(task2, advance=1)
            functions.git_init()
            progress.update(task2, advance=1)
        console.print(
            "[bold green][SUCC][/]"
            + f" Project [b]{self.name}[/b] created successfully!",
        )

    def module(self):
        ...

    def usecase(self):
        ...

    def presentation(self):
        ...

    def repository(self):
        ...

    def datasource(self):
        ...

    def driver(self):
        ...

    def error(self):
        ...
