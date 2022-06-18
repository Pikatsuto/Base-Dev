import json
import os
import shutil
from time import strftime

from database.info import Info


def python(command):
    if os.name == "posix":
        os.system(f".env/bin/python {command}")
    else:
        os.system(f".env\\Scripts\\python.exe {command}")


def python_sys(command):
    if os.name == "posix":
        os.system(f"python3 {command}")
    else:
        os.system(f"py {command}")


def restart():
    os.mkdir("database/restart")
    print("Program not exit ? -> CTRL-C\n")
    exit(0)


def exit_command():
    print("Program not exit ? -> CTRL-C\n")
    exit(0)


def install_python_libs(lib):
    python(f"-m pip install {lib}")
    restart()


try:
    from termcolor import colored
except ModuleNotFoundError:
    install_python_libs("termcolor")


def time_get(get_type):  # get time for easy read and name file compatible
    timeRead = strftime("%Y-%m-%d %H:%M:%S")
    timeFile = strftime("%Y-%m-%d_%H-%M-%S")

    if get_type == "read":
        return timeRead
    elif get_type == "file":
        return timeFile
    else:
        return "error time"


with open("database/consoleStartMessage.json") as file:  # console start ligne
    consoleStartMessage = json.load(file)


def debug_mode(active_debug_mode):
    if active_debug_mode in [True, False]:
        Info.debugMode = active_debug_mode


def debug_test(function: str, my_file: str, number: int, condition: str = ""):
    if Info.debugMode:
        if condition:
            print(
                f'{colored(consoleStartMessage["console"], "yellow")}'
                f'>> {my_file} {function} Test: {number} OK / Condition: {condition}'
            )

        else:
            print(f'{colored(consoleStartMessage["console"], "yellow")}>> {my_file} {function} Test: {number} OK')


def log_handler(output, if_print, user):  # send and save logs
    if not os.path.exists("logs"):
        os.makedirs("logs")

    timeRead = time_get("read")
    timeFile = time_get("file")

    if user == "log":
        my_log_message = f'{colored(consoleStartMessage[user], "blue")}>> {output}'
    elif user == "error":
        my_log_message = f'{colored(consoleStartMessage[user], "red")}>> {output}'
    elif user == "user":
        my_log_message = f'{colored(consoleStartMessage[user], "green")}>> {output}'
    elif user == "console":
        my_log_message = f'{colored(consoleStartMessage[user], "yellow")}>> {output}'
    logMessageText = f"{consoleStartMessage[user]}>> {output}"

    if if_print:
        print(my_log_message)

    if os.path.exists("logs/logs.txt"):  # read, count logs and add time in logs
        with open("logs/logs.txt", "r+") as f:
            logsFile = f.read()

        with open("logs/logs.txt") as f:
            ligneOfLogs = sum(1 for _ in f)

    else:
        logsFile = f"Start logs file : {timeRead}\n"
        ligneOfLogs = 3

    with open("logs/logs.txt", "w+") as f:  # save logs
        f.write(f"{logsFile}\n{timeRead} / {logMessageText}")

    if ligneOfLogs >= 997:  # create new logs file if logs ligne is > 1000
        if not os.path.exists("logs/old"):
            os.makedirs("logs/old")

        with open("logs/logs.txt", "w+") as f:
            f.write(f"{logsFile}\n{timeRead} / {logMessageText}\n\nEnd logs file : {timeRead}")

        shutil.move("logs/logs.txt", f"logs/old/logs_end_{timeFile}.txt")

        oldLogsFiles = os.listdir("logs/old")
        if len(oldLogsFiles) >= 10:
            shutil.make_archive(f"logs/oldZip/logs_end_{timeFile}", "zip", "logs/old")
            shutil.rmtree("logs/old")

    return my_log_message


def error_handler(error, function):  # send and save errors
    FATALE = False

    timeRead = time_get("read")
    timeFile = time_get("file")

    errorMessage = f'{colored(consoleStartMessage["error"], "red")}>> {function} : {error}'
    errorMessageText = f'{consoleStartMessage["error"]}>> {function} : {error}'
    logErrorMessage = f"{function} : {error}"

    if not os.path.exists("errors"):
        os.makedirs("errors")

    if os.path.exists("errors/errorsPerSecond.json"):  # read file of count error in one second
        with open("errors/errorsPerSecond.json", "r+") as f:
            errorsNumberJson = json.load(f)
            errorsNumber = errorsNumberJson["errorsNumber"]
            timeForLastError = errorsNumberJson["timeForLastError"]
            readErrorMessage = errorsNumberJson["readErrorMessage"]
    else:
        errorsNumberJson = {
            "errorsNumber": None,
            "timeForLastError": None,
            "readErrorMessage": None
        }
        with open("errors/errorsPerSecond.json", "w+") as f:
            json.dump(errorsNumberJson, f)

        errorsNumber = 0
        timeForLastError = ""

    errorsNumber += 1

    if errorsNumber >= 5 and timeForLastError == timeFile and readErrorMessage == errorMessage:  # stop program if 5
        # repetitive error
        errorsNumber = 0
        errorMessage = f'{colored(consoleStartMessage["error"], "red")}>> [FATALE] {function} : {error}'
        logErrorMessage = f"[FATALE] {function} : {error}"
        FATALE = True

    elif timeForLastError != timeFile:  # reset file count error if one second over
        errorsNumber = 0

    errorsNumberJson = {
        "errorsNumber": errorsNumber,
        "timeForLastError": timeFile,
        "readErrorMessage": errorMessage
    }

    with open("errors/errorsPerSecond.json", "w+") as f:  # right file error in one second
        json.dump(errorsNumberJson, f)

    log_handler(logErrorMessage, False, "error")
    log_handler(logErrorMessage, True, "error")

    if os.path.exists("errors/errors.txt"):  # read, count errors and add time in errors
        with open("errors/errors.txt", "r+") as f:
            errorsFile = f.read()

        with open("errors/errors.txt") as f:
            ligneOfErrors = sum(1 for _ in f)

    else:
        errorsFile = f"Start errors file : {timeRead}\n"
        ligneOfErrors = 3

    with open("errors/errors.txt", "w+") as f:
        f.write(f"{errorsFile}\n{timeRead} / {errorMessageText}")

    if ligneOfErrors >= 997:  # create new errors file if errors ligne is > 1000
        if not os.path.exists("errors/old"):
            os.makedirs("errors/old")

        with open("errors/errors.txt", "w+") as f:
            f.write(f"{errorsFile}\n{timeRead} / {errorMessageText}\n\nEnd errors file : {timeRead}")

        shutil.move("errors/errors.txt", f"errors/old/errors_end_{timeFile}.txt")

        oldErrorsFiles = os.listdir("errors/old")
        if len(oldErrorsFiles) >= 10:
            shutil.make_archive(f"errors/oldZip/errors_end_{timeFile}", "zip", "errors/old")
            shutil.rmtree("errors/old")

    if FATALE:
        exit(0)

    return errorMessage
