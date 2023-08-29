from abc import ABC, abstractmethod

# from typer import Option
# from typing_extensions import Annotated
# from typing import Optional


class CreateCommandsABC(ABC):
    def __init__(self, name: str = "new_project") -> None:
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @abstractmethod
    def project(
        self,
        # database: Annotated[
        #     Optional[str],
        #     Option("--database"),
        # ] = None,
    ):
        ...

    @abstractmethod
    def module(self):
        ...

    @abstractmethod
    def usecase(self):
        ...

    @abstractmethod
    def presentation(self):
        ...

    @abstractmethod
    def repository(self):
        ...

    @abstractmethod
    def datasource(self):
        ...

    @abstractmethod
    def driver(self):
        ...

    @abstractmethod
    def error(self):
        ...


class UpdateCommand(ABC):
    ...
