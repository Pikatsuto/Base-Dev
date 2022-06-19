import json
import os

from termcolor import colored

from libs.package import console
from libs.package import error_and_log

fileName = "Help"


def start_init(dev_mode=False):
    func_name = "startInit"

    try:
        error_and_log.debug_test(
            function=func_name, my_file=fileName, number=0, condition="Initial while"
        )
        if os.path.exists("database/help.json") and not dev_mode:
            error_and_log.debug_test(
                function=func_name,
                my_file=fileName,
                number=1,
                condition="If help.json exist",
            )
            with open("database/help.json", "r") as file:
                help_json = json.load(file)
        elif os.path.exists("database/devHelp.json") and dev_mode:
            error_and_log.debug_test(
                function=func_name,
                my_file=fileName,
                number=1,
                condition="If devHelp.json exist",
            )
            with open("database/devHelp.json", "r") as file:
                help_json = json.load(file)
        else:
            error_and_log.debug_test(
                function=func_name,
                my_file=fileName,
                number=1,
                condition="If and devHelp help.json dont exist",
            )
            return error_and_log.error_handler(
                "Help file not exist", "Help helpCommand"
            )

        console.clear()
        print(colored("Help info : \n", "green"))

        for help_command in help_json["help"]:
            error_and_log.debug_test(
                function=func_name,
                my_file=fileName,
                number=2,
                condition="for help in help or devHelp",
            )
            print(
                "  ",
                colored(help_command["name"], "cyan"),
                colored(":\n", "cyan"),
                colored("     Utilities :", "yellow"),
                help_command["Utilities"],
            )

            if help_command["arguments"]:
                error_and_log.debug_test(
                    function=func_name,
                    my_file=fileName,
                    number=3,
                    condition="If help have argument",
                )
                print(colored("      Arguments :", "yellow"))
                for helpArguments in help_command["arguments"]:
                    print("        ", helpArguments)

            print("")

    except Exception as e:
        return error_and_log.error_handler(e, f"{fileName} {func_name}")
