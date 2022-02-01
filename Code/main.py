import os

from command import Console, ErrorAndLog, Help

def console():
    try:
        commandListe = {
            "allCommand": [
                {
                    "clear": {
                        "command": Console.clear,
                        "arguments": False
                    },
                    "?": {
                        "command": Help.startInit,
                        "arguments": {
                            "default": False,
                            "dev": [
                                True
                            ]
                        }
                    }
                }
            ]
        }
        
        start = False
        while True:
            consoleInput = Console.consoleInput()

            if start:
                start = False
                Console.clear()

            elif consoleInput == "":
                pass
            
            else: # check if console input is on command json
                consoleInputSplit = consoleInput.split(" ")
                argumentsListe = consoleInputSplit
                commandSave = False
                arguments = False

                for command in commandListe["allCommand"]:
                    if consoleInputSplit[0] in command:
                        if command[consoleInputSplit[0]]:
                            commandSave = command[consoleInputSplit[0]]["command"]
                            if command[consoleInputSplit[0]]["arguments"]:
                                if command[consoleInputSplit[0]]["arguments"]["default"]:
                                    arguments = command[consoleInputSplit[0]]["arguments"]["default"]
                                    break
                                else:
                                    for argumentsInput in argumentsListe:
                                        if argumentsInput in command[consoleInputSplit[0]]["arguments"]:
                                            arguments = command[consoleInputSplit[0]]["arguments"][argumentsInput]
                                            break

                if commandSave and arguments: #Execute fonction for command
                    commandSave(arguments)

                elif commandSave:
                    commandSave()
                else:
                    ErrorAndLog.log(f"command \"{consoleInput}\" no fund", True, "log")
        
    except Exception as e:
        return ErrorAndLog.error(e, "Main console")

def startInit():
    try:
        if os.path.exists("exitAll"):
            os.remove("exitAll")
        Console.startInit()
        console()
        
    except Exception as e:
        return ErrorAndLog.error(e, "Main startInit")

startInit()