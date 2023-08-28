import os
from os import getcwd, path
import shutil
import subprocess
from modules.functions_abc import FunctionsABC


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
        os.mkdir(path.normpath(f"{getcwd()}/{self.name}/lib/core"))
        os.mkdir(path.normpath(f"{getcwd()}/{self.name}/lib/modules"))

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
            path.normpath(f"{self._assets}/dart/analysis_options.yaml"),
            path.normpath(f"{getcwd()}/{self.name}/analysis_options.yaml"),
        )

    def add_very_good_analysis(self):
        subprocess.run(
            "dart pub add very_good_analysis",
            cwd=f"{self.name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )
