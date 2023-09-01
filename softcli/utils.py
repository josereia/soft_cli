"""Useful Functions to make files, folders and verifications"""
# from contextlib import contextmanager
from logging_helper import get_logger
from models.dart.templates.path_getter import TEMPLATE_DIR
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt
from string import Template
from typer import Exit
import yaml

cwd = Path.cwd()
console = Console()
logger = get_logger(__file__)

d = {
    "class_name": "BlocDatasourceImpl",
    "project_name": "zzz",
    "module_name": "bloc",
    "abstract_file": "bloc_datasource.dart",
}


class CustomTemplate(Template):
    delimiter = "%$"
    idpattern = r"[a-z][_a-z0-9]*"


def make_class_file(
    name: str,
    create_path: Path,
    template_name: str,
    content: dict,
    parent: str = "parent",
):
    """Make a class file from template"""
    with open(f"{TEMPLATE_DIR}/{template_name}", "rt") as template:
        src = CustomTemplate(template.read())
        template_content = src.substitute(content)
    try:
        with open(f"{create_path}/{name}.dart", "wt") as file:
            file.writelines(template_content)
    except TypeError:
        logger.debug("Template vazio **trocar dps.")
        raise Exit(code=1)
    except FileExistsError:
        logger.info(f"File {name} already exist. check the {parent} folder.")
        raise Exit(code=1)
    except FileNotFoundError:
        logger.error(f"Something wrong with path provided, check the {parent}")
        raise Exit(code=1)
    else:
        logger.info(f"File {name}.dart created successfully.")


def make_folder(name: str, parent: str = "parent", path: Path = Path.cwd()):
    """
    Make a new folder in path provided.\n
    Path(f"{path}/{name}").mkdir()
    """
    try:
        Path(f"{path}/{name}").mkdir()
    except FileExistsError:
        logger.error(
            f"Folder {name} already exist, check your {parent} folder.",
        )
        raise Exit(code=1)
    except FileNotFoundError:
        logger.error(f"Something wrong with path provided, check the {parent}")
        raise Exit(code=1)
    else:
        logger.debug(f"Folder {name} created in {parent}.")


def make_softfile(project_name: str, path: Path = Path.cwd()):
    """Make a softfile.yaml in path provided"""
    language = Prompt.ask(
        "Chose which language your project written:",
        choices=["dart", "javascript", "python"],
    )
    database = Prompt.ask(
        "Chose which database your project uses:",
        choices=["postgresql", "mongodb", "mysql"],
    )
    content = [
        {
            "Config": {
                "language": f"{language}",
                "database": f"{database}",
                "project_name": f"{project_name}",
            },
        }
    ]
    if not Path(path).exists():
        Path(f"{path}").mkdir(parents=True)
    try:
        with open(Path(f"{path}/.softfile.yaml"), "w") as yamlfile:
            data = yaml.dump(content, yamlfile)
            print(data)
    except NameError as error:
        logger.debug(f"The {error} not defined verify imports and var names.")
    except Exception as error:
        logger.error(f"{error}. **Add error no try da make_softfile**")
    else:
        console.print(
            "[green]✓ File softfile.yaml created in successfully.[/]",
        )


def get_config_info(path: Path = Path.cwd()) -> tuple | None:
    """Get info from softfile.yaml"""
    if not Path(f"{path}/.softfile.yaml").exists():
        logger.error(
            "File softfile.yaml does not exist. check if you in root project",
        )
        return None, "not_exist"
    try:
        with open(f"{path}/.softfile.yaml", "r") as softfile:
            data = yaml.load(softfile, Loader=yaml.FullLoader)
            language = data[0]["Config"]["language"]
            database = data[0]["Config"]["database"]
            project_name = data[0]["Config"]["project_name"]

        if language is None:
            raise AttributeError("language")
        if database is None:
            raise AttributeError("database")
        if language is None:
            raise AttributeError("project_name")
        logger.debug(
            f"Get info return language: {language}"
            + f", database: {database} and project_name: {project_name}",
        )
    except AttributeError as error:
        logger.error(
            f"Value for {error} is None. run  \
             soft --config for make new softfile.",
        )
        return None
    except KeyError as key:
        logger.error(f"The key {key.args[0]} not found in softfile.yaml.")
        return None
    except Exception as error:
        logger.error(f"{error}. **Add error no try da make_softfile**")
        return None
    return language, database, project_name


def soft_file_manager(name: str, path: Path = Path.cwd()) -> tuple | object:
    """Manages the process to get info and create a softfile.yaml if needed"""
    infos = get_config_info(path)
    if infos is not None and infos.__contains__("not_exist"):
        logger.info("Generating softfile.yaml")
        make_softfile(name, path)
        return soft_file_manager(name, path)

    if infos is not None:
        return infos
    else:
        logger.info("Empty softfile.yaml. Regenerating softfile.yaml")
        make_softfile(name, path)
        return soft_file_manager(name, path)


if __name__ == "__main__":
    content = {
        "class_name": "TesteErrro",
        "project_name": "acb",
        "module_name": "module_name",
        "import_file": "teste.dart",
        "abstract_class": "tetste",
    }
