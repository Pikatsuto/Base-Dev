import os
import shutil

from libs.package import ErrorAndLog

file_name = "Main"


def check_env():
    function_name = "checkEnv"

    try:
        if not os.path.exists(".env"):
            ErrorAndLog.python_sys("-m venv .env")
            ErrorAndLog.python("-m pip install --upgrade pip")

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{file_name} {function_name}")


def check_and_install():
    function_name = "checkAndInstall"

    try:
        if not os.path.exists("database"):
            os.makedirs("database")

        if not os.path.exists("libs"):
            return ErrorAndLog.error_handler("[FATAL] Command folder missing", "StartProgram CheckAndInstall")

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{file_name} {function_name}")


def start_and_restart():
    function_name = "startAndRestart"

    try:
        while True:
            ErrorAndLog.python("main.py")

            if not os.path.exists("database/restart"):
                break
            else:
                shutil.rmtree("database/restart")

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{file_name} {function_name}")


def start_init():
    function_name = "startInit"

    try:
        check_env()
        check_and_install()
        start_and_restart()

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{file_name} {function_name}")


start_init()
