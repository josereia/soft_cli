"""Functions useful for make files and verifications."""
import yaml
from rich.prompt import Prompt
from os import getcwd, path
from pathlib import Path
from utils.logging_helper import get_logger

logger = get_logger(__file__)


def verify_str_input(input: str) -> bool:
    if isinstance(input, str):
        return True
    else:
        return f"You response is {type(input)}, but must be string."


def make_soft_file(name: str = "new_project") -> None:
    """
    Make soft_file.yaml.
    :param name: set name from project. [default: new_project]
    """
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
            },
        }
    ]

    if not path.isdir(f"./{name}"):
        Path(f"./{name}").mkdir(exist_ok=True)
        with open(Path(f"./{name}/.soft_file.yaml"), "w") as yamlfile:
            data = yaml.dump(content, yamlfile)
            print(data)

    logger.info("File soft_file.yaml created.")


def get_soft_file_info(name: str = "new_project") -> tuple:
    """
    Get all info to setting commands
    :return: tuple -> ('language', 'database')
    """
    with open(f"./{name}/.soft_file.yaml", "r") as soft_file:
        data = yaml.load(soft_file, Loader=yaml.FullLoader)
        language = data[0]["Config"]["language"]
        database = data[0]["Config"]["database"]
    return language, database


def get_soft_file(name: str = "new_project") -> bool:
    """Get soft_file.yaml if exist."""
    file_path = f"{getcwd()}/{name}/.soft_file.yaml"
    if path.exists(file_path):
        return True
    else:
        return False


def soft_file_manager(name: str = "new_project") -> tuple:
    """
    Uses functions for verify if soft_file.yaml exist.

    If exist get all infos, else make a soft_file.yaml
    and get all infos
    :return: tuple -> ('language', 'database')
    """
    if get_soft_file(name):
        return get_soft_file_info(name)
    else:
        make_soft_file(name)
        return soft_file_manager(name)


if __name__ == "__main__":
    t = soft_file_manager("dart")
    print(t)
