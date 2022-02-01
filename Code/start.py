import os, shutil

from command import ErrorAndLog, Console
from termcolor import colored


def checkEnv():
    try:
        if not os.path.exists(".env"):
            if os.name == "posix":
                os.system("python3 -m venv .env")
            else:
                os.system("py -m venv .env")
            os.system(".env/bin/python -m pip install --upgrade pip")

    except Exception as e:
        return ErrorAndLog.error(e, "StartPrograme checkEnv")


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
            os.system(".env/bin/python main.py")
            
            if not os.path.exists("database/restart"):
                break
            else:
                shutil.rmtree("database/restart")
        
    except Exception as e:
        return ErrorAndLog.error(e, "StartPrograme startAndRestart")


def startInit():
    try:
        checkEnv()
        checkAndInstall()
        startAndRestart()

    except Exception as e:
        return ErrorAndLog.error(e, "StartPrograme startInit")

startInit()