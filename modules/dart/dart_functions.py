from os import getcwd
import shutil
import subprocess
from modules.functions_abc import FunctionsABC
from pathlib import Path


class DartFunctions(FunctionsABC):
    def create_project(self):
        subprocess.run(
            f"dart create {self.name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )

    def create_module(self):
        ...

    def create_folders(self):
        Path(f"{getcwd()}/{self.name}/lib/core").mkdir(
            parents=True,
            exist_ok=True,
        )
        Path(f"{getcwd()}/{self.name}/lib/modules").mkdir(
            parents=True,
            exist_ok=True,
        )

    def get_dependencies(self):
        subprocess.run(
            "dart pub get",
            cwd=f"{self.name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )

    def git_init(self):
        subprocess.run(
            "git init",
            cwd=f"{self.name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )

    def copy_analysis_options(self):
        shutil.copyfile(
            Path(f"{self._assets}/dart/analysis_options.yaml"),
            Path(f"{getcwd()}/{self.name}/analysis_options.yaml"),
        )

    def add_very_good_analysis(self):
        subprocess.run(
            "dart pub add very_good_analysis",
            cwd=f"{self.name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )
