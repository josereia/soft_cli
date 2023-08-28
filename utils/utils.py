import yaml


def verify_str_input(input: str) -> bool:
    if isinstance(input, str):
        return True
    else:
        return f"You response is {type(input)}, but must be string."


def make_soft_file(language: str, database: str) -> str:
    """
    Make soft_file.yaml.
    :param language: str config which language class the cli uses
    :param database: str config which database class the cli uses
    :return: None, just add soft_file.yaml in root of the project
    """

    content = [
        {
            "Config": {
                "language": f"{language}",
                "database": f"{database}",
            },
        }
    ]

    with open("./soft_file.yaml", "w") as yamlfile:
        data = yaml.dump(content, yamlfile)
        print(data)
        return "Archive soft_file.yaml created."


if __name__ == "__main__":
    make_soft_file("dart", "postgres")
