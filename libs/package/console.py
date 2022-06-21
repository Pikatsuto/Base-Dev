import os
import sys
from termcolor import colored
from libs.package import info


def restart_program():
    info.restart = True
    sys.exit()


class ConsoleInput:
    def __init__(self):
        self.input_prefix = None

    def set_input_prefix(self, prefix=False):
        if prefix:
            self.input_prefix = f"{colored(prefix, 'cyan')} / {colored('(U)', 'green')} >> "
        else:
            self.input_prefix = f"{colored('(U)', 'green')} >> "

    def start(self, user, prefix=False):
        self.set_input_prefix(user, prefix)

        cmd = input(self.input_prefix)

        if cmd == "exit":
            sys.exit()
        elif cmd == "restart":
            restart_program()
        elif cmd != "":
            return cmd
        else:
            return False


console_input_class = ConsoleInput()


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

    return True


def motd():  # show start menu
    clear()
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


class Help(CommandGroup):
    def __init__(self):
        super().__init__()
        self.commands = CommandGroup.methods

    @command("help")
    def helping(self):
        for cmd in self.commands:
            print(cmd.__doc__)

        print("")


help_class = Help()