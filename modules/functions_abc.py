from abc import ABC, abstractmethod
from assets.path_getter import ASSETS_DIR


class FunctionsABC(ABC):
    def __init__(self, name: str) -> None:
        super().__init__()
        self._assets = ASSETS_DIR
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @abstractmethod
    def create_project(self):
        ...

    @abstractmethod
    def create_folders(self):
        ...

    @abstractmethod
    def get_dependencies(self):
        ...

    @abstractmethod
    def git_init(self):
        ...


if __name__ == "__main__":
    ...
