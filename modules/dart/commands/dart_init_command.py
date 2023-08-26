from abc import ABC
import os
import shutil
import subprocess


class DartInitCommand(ABC):
    @staticmethod
    def create_project(
        name: str,
    ):
        subprocess.run(
            f"dart create {name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )

    @staticmethod
    def create_core_folder(
        name: str,
    ):
        os.mkdir(f"{name}/lib/core")

    @staticmethod
    def create_modules_folder(
        name: str,
    ):
        os.mkdir(f"{name}/lib/modules")

    @staticmethod
    def copy_analysis_options(
        name: str,
    ):
        shutil.copyfile(
            "assets/dart/analysis_options.yaml",
            f"{name}/analysis_options.yaml",
        )

    @staticmethod
    def add_very_good_analysis(
        name: str,
    ):
        subprocess.run(
            "dart pub add very_good_analysis",
            cwd=f"{name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )

    @staticmethod
    def get_packages(
        name: str,
    ):
        subprocess.run(
            "dart pub get",
            cwd=f"{name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )

    @staticmethod
    def git_init(
        name: str,
    ):
        subprocess.run(
            "git init",
            cwd=f"{name}",
            shell=True,
            stdout=subprocess.DEVNULL,
        )
