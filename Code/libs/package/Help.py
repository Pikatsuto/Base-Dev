import json, os
from termcolor import colored

from libs.package import Console
from libs.package import ErrorAndLog


def startInit(devMode=False):
    try:
        if os.path.exists("database/help.json") and not devMode:
            with open("database/help.json", "r") as file:
                helpJson = json.load(file)
        elif os.path.exists("database/devHelp.json") and devMode:
            with open("database/devHelp.json", "r") as file:
                helpJson = json.load(file)
        else:
            return ErrorAndLog.error("Help file not existe", "Help helpCommande")

        Console.clear()
        print(colored("Help info : \n", "green"))

        for helpCommand in helpJson["help"]:
            print("  ", colored(helpCommand["name"], "cyan"), colored(":\n", "cyan"),
            colored("     Utilitis :", "yellow"), helpCommand["Utilitis"])

            if helpCommand["arguments"] != False:
                print(colored("      Arguments :", "yellow"))
                for helpArguments in helpCommand["arguments"]:
                    print("        ", helpArguments)
            
            print("")

    except Exception as e:
        return ErrorAndLog.error(e, "Help helpCommande")