from termcolor import colored

from .command import CommandGroup
from libs.package import utils, console

fileName = "Main"


def main():
    is_running = True

    console.clear()
    print(
        colored(f"# {'-' * 75} #", "green"),
        '\n'
        '   888888b.                                     8888888b.\n'
        '   888  "88b                                    888  "Y88b\n'
        '   888  .88P                                    888    888\n'
        '   8888888K.   8888b.  .d8888b   .d88b.         888    888  .d88b.  888  888\n'
        '   888  "Y88b     "88b 88K      d8P  Y8b        888    888 d8P  Y8b 888  888\n'
        '   888    888 .d888888 "Y8888b. 88888888        888    888 88888888 Y88  88P\n'
        '   888   d88P 888  888      X88 Y8b.            888  .d88P Y8b.      Y8bd8P\n'
        '   8888888P"  "Y888888  88888P\'  "Y8888         8888888P"   "Y8888    Y88P\n'
        '\n'
        '                                  By Pikatsuto\n'
        + colored(f"# {'-' * 75} #", "green"),
        '\n\n'
        + colored("Welcome", "green"), "for Base Dev shell\n"
        + colored("[?]", "cyan"), "For Help command\n",
    )

    while is_running:
        action = input(f'{colored("green")}>> ')
        CommandGroup.methods.get(action)[0]()


if __name__ == '__main__':
    main()
