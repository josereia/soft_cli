from dataclasses import dataclass


@dataclass
class Assets:
    logo = """
    _____        __ _    _____ _ _
    / ____|      / _| |  / ____| (_)
    | (___   ___ | |_| |_| |    | |_|
    \___ \ / _ \|  _| __| |    | | |
    ____) | (_) | | | |_| |____| | |
    |_____/ \___/|_|  \__|\_____|_|_|
                create by SoftYes TI"""

    intro_txt = (
        "Run [italic dim]soft create project <project_name>[/]"
        + " to create a new project.\n"
        + "Run [italic grey42]soft --config[/] to setup environment of "
        + "cli in a already created project."
    )

    # create_command help
    datasource_help = """
    :page_facing_up: Create [b]datasource[/] files in modules folder.
    """

    datasource_name_help = (
        "Name of file. "
        + "[italic]:cross_mark: Don't add language extension.[/]"
    )

    datasource_module_name_help = """
    Name of module where the file will be created."""

    driver_help = """
    :page_facing_up: Create [b]driver[/] file in module folder.
    """

    error_help = """
    :page_facing_up: Create [b]error[/] file in modules folder.
    """

    module_help = (
        ":file_folder: Create [b]module[/]"
        + " folder and its children in project folder."
    )

    presentation_help = (
        ":page_facing_up: Create [b]presentation[/] file in modules folder."
    )

    project_help = (
        ":package: Create a [b]project[/] in"
        + " the language/framework configured in softfile."
    )

    repository_help = """
    :page_facing_up: Create [b]repository[/] files in module folder.
    """

    usecase_help = """
    :page_facing_up: Create [b]usecases[/] files in modules folder.
    """


"""
floppy_disk - 💾
package - 📦
file_folder - 📁
page_facing_up
bookmark_tabs
inbox_tray
lock
whale
snake
direct hit
hot beverage
construction sign
rocket

"""
