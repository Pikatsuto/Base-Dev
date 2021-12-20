import os, shutil, json
from time import strftime
from termcolor import colored

def timeGet(getType):# get time for easy read and name file compatible
    timeRead = strftime("%Y-%m-%d %H:%M:%S")
    timeFile = strftime("%Y-%m-%d_%H-%M-%S")

    if getType == "read":
        return timeRead
    elif getType == "file":
        return timeFile
    else:
        return "error time"

with open("database/consoleStartMessage.json") as file:# console start ligne
    consoleStartMessage = json.load(file)

def log(output, ifPrint, user):#send and save logs
    if not os.path.exists("logs"):
        os.makedirs("logs")

    timeRead = timeGet("read")
    timeFile = timeGet("file")

    if user == "log":
        logMessage = "{}>> {}".format(colored(consoleStartMessage[user], "blue"), output)
    elif user == "error":
        logMessage = "{}>> {}".format(colored(consoleStartMessage[user], "red"), output)
    elif user == "user":
        logMessage = "{}>> {}".format(colored(consoleStartMessage[user], "green"), output)
    elif user == "console":
        logMessage = "{}>> {}".format(colored(consoleStartMessage[user], "yellow"), output)
    logMessageText = "{}>> {}".format(consoleStartMessage[user], output)

    if ifPrint:
        print(logMessage)            

    if os.path.exists("logs/logs.txt"):# read, count logs and add time in logs
        with open("logs/logs.txt", "r+") as file:
            logsFile = file.read()

        with open("logs/logs.txt") as file:
            ligneOfLogs = sum(1 for _ in file)
    
    else:
        logsFile = (f"Start logs file : {timeRead}\n")
        ligneOfLogs = 3
    
    with open("logs/logs.txt", "w+") as file:# save logs
        file.write(f"{logsFile}\n{timeRead} / {logMessageText}")
    
    if ligneOfLogs >= 997:# create new logs file if logs ligne is > 1000
        if not os.path.exists("logs/old"):
            os.makedirs("logs/old")
    
        with open("logs/logs.txt", "w+") as file:
            file.write(f"{logsFile}\n{timeRead} / {logMessageText}\n\nEnd logs file : {timeRead}")

        shutil.move("logs/logs.txt", f"logs/old/logs_end_{timeFile}.txt")

        oldLogsFiles = os.listdir("logs/old")
        if len(oldLogsFiles) >= 10:
            shutil.make_archive(f"logs/oldZip/logs_end_{timeFile}", "zip", "logs/old")
            shutil.rmtree(f"logs/old")


    return logMessage


def error(error, function):#send and save errors
    FATALE = False

    timeRead = timeGet("read")
    timeFile = timeGet("file")

    errorMessage = "{}>> {} : {}".format(colored(consoleStartMessage["error"], "red"), function, error)
    errorMessageText = "{}>> {} : {}".format(consoleStartMessage["error"], function, error)
    logErrorMessage = "{} : {}".format(function, error)

    if not os.path.exists("errors"):
        os.makedirs("errors")

    if os.path.exists("errors/errorsPerSecond.json"):# read file of count error in one second
        with open("errors/errorsPerSecond.json", "r+") as file:
            errorsNumberJson = json.load(file)
            errorsNumber = errorsNumberJson["errorsNumber"]
            timeForLastError = errorsNumberJson["timeForLastError"]
            readErrorMessage = errorsNumberJson["readErrorMessage"]
    else:
        errorsNumber = 0
        timeForLastError = ""

    errorsNumber += 1

    if errorsNumber >= 5 and timeForLastError == timeFile and readErrorMessage == errorMessage:# stop programe if 5 repetitive error
        errorsNumber = 0
        errorMessage = "{}>> [FATALE] {} : {}".format(colored(consoleStartMessage["error"], "red"), function, error)
        logErrorMessage = "[FATALE] {} : {}".format(function, error)
        FATALE = True
    
    elif timeForLastError != timeFile:# reset file count error if one seconde over
        errorsNumber = 0

    errorsNumberJson = {
        "errorsNumber": errorsNumber,
        "timeForLastError": timeFile,
        "readErrorMessage": errorMessage
    }

    with open("errors/errorsPerSecond.json", "w+") as file:# right file error in one seconde
        json.dump(errorsNumberJson, file)

    log(logErrorMessage, False, "error")
    log(logErrorMessage, True, "error")

    if os.path.exists("errors/errors.txt"):# read, count errors and add time in errors
        with open("errors/errors.txt", "r+") as file:
            errorsFile = file.read()

        with open("errors/errors.txt") as file:
            ligneOfErrors = sum(1 for _ in file)
    
    else:
        errorsFile = (f"Start errors file : {timeRead}\n")
        ligneOfErrors = 3
    
    with open("errors/errors.txt", "w+") as file:
        file.write(f"{errorsFile}\n{timeRead} / {errorMessageText}")
    
    if ligneOfErrors >= 997:# create new errors file if errors ligne is > 1000
        if not os.path.exists("errors/old"):
            os.makedirs("errors/old")
    
        with open("errors/errors.txt", "w+") as file:
            file.write(f"{errorsFile}\n{timeRead} / {errorMessageText}\n\nEnd errors file : {timeRead}")

        shutil.move("errors/errors.txt", f"errors/old/errors_end_{timeFile}.txt")

        oldErrorsFiles = os.listdir("errors/old")
        if len(oldErrorsFiles) >= 10:
            shutil.make_archive(f"errors/oldZip/errors_end_{timeFile}", "zip", "errors/old")
            shutil.rmtree(f"errors/old")
    
    if FATALE:
        exit(0)

    return errorMessage