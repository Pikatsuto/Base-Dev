import json
import os

from termcolor import colored

from libs.package import Console
from libs.package import ErrorAndLog

fileName = "Help"


def start_init(dev_mode=False):
    functionName = "startInit"

    try:
        ErrorAndLog.debug_test(function=functionName, my_file=fileName, number=0, condition="Initial while")
        if os.path.exists("database/help.json") and not dev_mode:
            ErrorAndLog.debug_test(function=functionName, my_file=fileName, number=1, condition="If help.json exist")
            with open("database/help.json", "r") as file:
                helpJson = json.load(file)
        elif os.path.exists("database/devHelp.json") and dev_mode:
            ErrorAndLog.debug_test(function=functionName, my_file=fileName, number=1, condition="If devHelp.json exist")
            with open("database/devHelp.json", "r") as file:
                helpJson = json.load(file)
        else:
            ErrorAndLog.debug_test(function=functionName, my_file=fileName, number=1,
                                   condition="If and devHelp help.json dont exist")
            return ErrorAndLog.error_handler("Help file not existe", "Help helpCommande")

        Console.clear()
        print(colored("Help info : \n", "green"))

        for help_command in helpJson["help"]:
            ErrorAndLog.debug_test(function=functionName, my_file=fileName, number=2,
                                   condition="for help in help or devHelp")
            print("  ", colored(help_command["name"], "cyan"), colored(":\n", "cyan"),
                  colored("     Utilities :", "yellow"), help_command["Utilities"])

            if help_command["arguments"]:
                ErrorAndLog.debug_test(function=functionName, my_file=fileName, number=3,
                                       condition="If help have argument")
                print(colored("      Arguments :", "yellow"))
                for helpArguments in help_command["arguments"]:
                    print("        ", helpArguments)

            print("")

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{fileName} {functionName}")
