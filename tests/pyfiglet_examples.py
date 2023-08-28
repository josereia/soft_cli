from time import sleep
import pyfiglet
import sys

with open("./tests/pyfigletfonts.txt", "r") as file:
    fonts = file.read().splitlines()

with open("./tests/result_font_test.txt", "a") as sys.stdout:
    for fonty in fonts:
        print("Testing font " + fonty)
        f = pyfiglet.Figlet(font=fonty, width=80)
        print(f.renderText("SoftCli"))
        sleep(0.8)
