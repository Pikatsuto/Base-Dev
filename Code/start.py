import os
from sys import platform

from command import Console, ErrorAndLog

try:
    from termcolor import colored
except ModuleNotFoundError:
    if platform in ["linux", "linux2"]:
        os.system("python -m pip install termcolor")
    elif platform == "win32":
        os.system("py -m pip install termcolor")
    from termcolor import colored


def checkAndInstall():
    try:
        if not os.path.exists("database"):
            os.makedirs("database")

        if not os.path.exists("command"):
            return(ErrorAndLog.error("[FATAL] Command folder missing", "StartPrograme CheckAndInstall"))

    except Exception as e:
        return ErrorAndLog.error(e, "StartPrograme CheckAndInstall")


def startAndRestart():
    try:
        while True:
            if platform in ["linux", "linux2"]:
                os.system("python main.py")
            elif platform == "win32":
                os.system("py main.py")
            ifRestart = input("Restart {} ? {} {}>> ".format(colored("PikaUtils", "yellow"), colored("[N for no]", "cyan"), colored("(U)", "green")))
            if ifRestart == "n":
                Console.clear()
                break
        
    except Exception as e:
        return ErrorAndLog.error(e, "StartPrograme startAndRestart")


def startInit():
    try:
        checkAndInstall()
        startAndRestart()

    except Exception as e:
        return ErrorAndLog.error(e, "StartPrograme startInit")

startInit()