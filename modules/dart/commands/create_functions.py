"""Class with all functions for create command in version dart"""
from os import getcwd
from pathlib import Path
import shutil
import subprocess
from modules.functions_abc import FunctionsABC


class DartCreateFunctions(FunctionsABC):
    def create_project(self):
        """Create a dart project"""
        subprocess.run(
            f"dart create {self.name} --force",
            shell=True,
            stdout=subprocess.DEVNULL,
        )

    def create_module(self):
        ...

    def create_folders(self):
        """Create lib, core and modules folders"""
        Path(f"{getcwd()}/{self.name}/lib/core").mkdir(
            parents=True,
            exist_ok=True,
        )
        Path(f"{getcwd()}/{self.name}/lib/modules").mkdir(
            parents=True,
            exist_ok=True,
        )

    def get_dependencies(self):
        """Run dart pub get"""
        subprocess.run(
            "dart pub get",
            cwd=f"{self.name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )

    def git_init(self):
        """Run git init and initialize a repository"""
        subprocess.run(
            "git init",
            cwd=f"{self.name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )

    def copy_analysis_options(self):
        """Make a copy to analysis_options.yaml from assets of cli"""
        shutil.copyfile(
            Path(f"{self._assets}/dart/analysis_options.yaml"),
            Path(f"{getcwd()}/{self.name}/analysis_options.yaml"),
        )

    def add_very_good_analysis(self):
        """Run dart add to install very_good_analysis"""
        subprocess.run(
            "dart pub add very_good_analysis",
            cwd=f"{self.name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )
