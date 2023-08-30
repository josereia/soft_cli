"""Useful Functions to make files, folders and verifications"""
# from contextlib import contextmanager
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt
from logging_helper import get_logger
from typer import Exit
import yaml


console = Console()
logger = get_logger(__file__)


# @contextmanager
# def opened_w_error(filename, mode="r"):
#     try:
#         f = open(filename, mode)
#     except IOError, err:
#         yield None, err
#     else:
#         try:
#             yield f, None
#         finally:
#             f.close()


def make_folder(name: str, path: Path = Path.cwd()):
    """Make a new folder in path provided"""
    try:
        Path(f"{path}/{name}").mkdir()
    except FileExistsError:
        logger.error("File already exist, check your parent folder.")
    except FileNotFoundError:
        logger.error("Something wrong with path provided, check the path.")
    else:
        console.print(
            f"[green]✓ Folder {name} created in {path} successfully.[/]",
        )


def make_softfile(path: Path):
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
            },
        }
    ]
    try:
        with open(Path(f"{path}/.softfile.yaml"), "w") as yamlfile:
            data = yaml.dump(content, yamlfile)
            print(data)
    except Exception as error:
        logger.error(f"{error}. **Add error no try da make_softfile**")
    else:
        console.print(
            "[green]✓ File softfile.yaml created in successfully.[/]",
        )
        raise Exit()


def get_config_info() -> tuple | None:
    """Get info from softfile.yaml"""
    if not Path(f"{Path.cwd()}/.softfile.yaml").exists():
        logger.error(
            "File softfile.yaml does not exist. go to root folder of project?",
        )
    try:
        with open(f"{Path.cwd()}/.softfile.yaml", "r") as softfile:
            data = yaml.load(softfile, Loader=yaml.FullLoader)
            language = data[0]["Config"]["language"]
            database = data[0]["Config"]["database"]

        if language is None:
            raise AttributeError("language")
        if database is None:
            raise ValueError()
        logger.info(
            f"Get info return language: {language}"
            + f" and database: {database}",
        )
    except AttributeError as error:
        logger.error(
            f"Value for {error} is None. run "
            + "soft --config for make new softfile.",
        )
        return None
    except KeyError as key:
        logger.error(f"The key {key.args[0]} not found in softfile.yaml.")
        return None
    except Exception as error:
        logger.error(f"{error}. **Add error no try da make_softfile**")
        return None
    return language, database


def soft_file_manager(path: Path):
    """Manages the process to get info and create a softfile.yaml if needed"""
    infos = get_config_info()
    if infos is None:
        logger.error("")


if __name__ == "__main__":
    # make_softfile(Path("/tests"))
    var = get_config_info()
    print(var)
