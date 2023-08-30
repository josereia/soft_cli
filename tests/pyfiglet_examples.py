from time import sleep
import pyfiglet
import sys
from pathlib import Path

test = pyfiglet.figlet_format("SoftCli")
print(test)

with open("./tests/pyfigletfonts.txt", "r") as file:
    fonts = file.read().splitlines()

with open(Path(f"{Path.cwd()}/tests/result_font_test.txt"), "a") as sys.stdout:
    for fonty in fonts:
        print("Testing font " + fonty)
        f = pyfiglet.Figlet(font=fonty, width=80)
        print(f.renderText("SoftCli"))
        sleep(0.8)
