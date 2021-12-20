import os, json, requests, shutil, sys, subprocess
from termcolor import colored

from command import ErrorAndLog


with open("database/consoleStartMessage.json") as file:# console start ligne
    consoleStartMessage = json.load(file)


def consoleInput(inputText=False, lower=True):#console Input
    try:
        if not inputText:
            consoleInput = input("{}>> ".format(colored(consoleStartMessage["user"], "green")))
        else:
            consoleInput = input("{} / {}>> ".format(colored(inputText, "cyan"), colored(consoleStartMessage["user"], "green")))
        
        if lower:
            consoleInput.lower()

        if consoleInput == "exit":
            print("Restart not show ? -> CTRL-C or shutdown command for your bot")
            exit(0)

        elif consoleInput != "":
            ErrorAndLog.log(consoleInput, False, "user")

        return consoleInput

    except Exception as e:
        return ErrorAndLog.error(e, "Console consoleInput")


def menu():#show start menu
    try:
        print(colored("▀█████████▄     ▄████████    ▄████████    ▄████████           ████████▄     ▄████████ ▄█      █▄ ", "yellow"))
        print(colored("  ███    ███   ███    ███   ███    ███   ███    ███           ███   ▀███   ███    ███ ██      ██ ", "yellow"))
        print(colored("  ███    ███   ███    ███   ███    █▀    ███    █▀            ███    ███   ███    █▀  ███    ███ ", "yellow"))
        print(colored(" ▄███▄▄▄██▀    ███    ███   ███         ▄███▄▄▄     ▄███████▄ ███    ███  ▄███▄▄▄     ▀██    ██▀ ", "yellow"))
        print(colored("▀▀███▀▀▀██▄  ▀███████████ ▀███████████ ▀▀███▀▀▀     ▀███████▀ ███    ███ ▀▀███▀▀▀      ██    ██  ", "yellow"))
        print(colored("  ███    ██▄   ███    ███          ███   ███    █▄            ███    ███   ███    █▄   ███  ███  ", "yellow"))
        print(colored("  ███    ███   ███    ███    ▄█    ███   ███    ███           ███   ▄███   ███    ███   ██  ██   ", "yellow"))
        print(colored("▄█████████▀    ███    █▀   ▄████████▀    ████████▀            ████████▀    ████████▀    ▀████▀   ", "yellow"))
        print(colored("_________________________________________________________________________________________________", "green")) 
        print(colored("\nWelcome", "green"), "for Base Dev shell", colored("\n[?]", "cyan"), "For Help commande\n")

    except Exception as e:
        return ErrorAndLog.error(e, "Console menu")


def clear():#use clear commande
    try:
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

    except Exception as e:
        return ErrorAndLog.error(e, 'Console clear')

# varNameListe is liste of variable name
# messageList is a message liste for variable value input
# prefix is e préfix for message input (All prefix in database/consoleStartMessage)
# varDefautListe is default value liste for varNameListe
# path is a path for tour json (default is database)
# name is name for your json questionaire
# makeDir is if make (path/name) for your json
# header is if start jsont on {"name":[]}
# nameFile is name for json file
# varDefList is if your variable is (str / int / float / bin / hex) default is str
def jsonAdd(varNameList, messageList, prefix, varDefautList=False, path="database", name=False, makeDir=False, header=False, nameFile=False, varDefList=False):
    try:
        resetInfo = False
        while True:
            jsonInfoPrintList = []
            if not name or resetInfo:
                name = ""
                while name == "":
                    clear()
                    print(f"{prefix}\n")
                    name = consoleInput("Enter name", lower=False)
                    if name != "":
                        jsonInfoPrintList.append("{}: {}".format(colored(f"{prefix} name", "blue"), colored(name, "green", attrs=["dark"])))

            if not nameFile:
                nameFile = name

            if os.path.exists(f"{path}/{nameFile}.json"):
                with open(f"{path}/{nameFile}.json", "r") as file:
                    jsonInfo = json.load(file)
            
            elif header:
                jsonInfo = {
                    f"{name}":[

                    ]
                }
                
            else:
                jsonInfo = {
                    f"name": f"{name}"
                }
            
            clockCount = 0
            for varName in varNameList:
                varInput = ""
                varDefautSave = False
                varDefSave = False

                if varDefautList:
                    for varDefaut in varDefautList:
                        if varDefaut[0] == clockCount:
                            varDefautSave = varDefaut[1]

                if varDefList:
                    for varDef in varDefList:
                        if varDef[0] == clockCount:
                            varDefSave = varDef[1]

                while varInput == "":
                    clear()
                    print(f"{prefix}\n")
                    if jsonInfoPrintList != []:
                        for jsonInfoPrint in jsonInfoPrintList:
                            print(jsonInfoPrint)

                    if varInput == "":
                        varInput = consoleInput("{} {}".format(prefix, messageList[clockCount]), lower=False)

                    if varInput == "" and varDefautSave != False:
                        varInput = varDefautSave
                    
                    else:
                        try:
                            if varDefSave != False:
                                if varDefSave == "int":
                                    varInput = int(varInput)
                                if varDefSave == "hex":
                                    varInput = hex(int(varInput, 16))
                                if varDefSave == "bin":
                                    varInput = bin(int(varInput, 2))
                        except (ValueError, TypeError):
                            varInput = ""

                    if varInput != "":
                        jsonInfoPrintList.append("{}: {}".format(colored(f"{prefix} {varName}", "blue"), colored(varInput, "green", attrs=["dark"])))

                        jsonInfoAppend = {
                            f"{varName}": varInput
                        }
                        if header:
                            if clockCount >= 1:
                                jsonInfo[f"{name}"][0].update(jsonInfoAppend)
                            else:
                                jsonInfo[f"{name}"].append(jsonInfoAppend)
                        else:
                            jsonInfo.update(jsonInfoAppend)


                clockCount += 1
        
            checkInfo = None
            while checkInfo not in ["y", "n", ""]:
                clear()

                print(f"{prefix}\n")
                for jsonInfoPrint in jsonInfoPrintList:
                    print(jsonInfoPrint)

                checkInfo = consoleInput("this info is good ? [Y/n]")
                if checkInfo == "y" or checkInfo == "":
                    if makeDir:
                        path = f"{path}/{name}"
                        if not os.path.exists(path):
                            os.makedirs(path)

                    with open(f"{path}/{nameFile}.json", "w+") as file:
                        json.dump(jsonInfo, file)
                    
                    return jsonInfo
                elif checkInfo == "n":
                    resetInfo = True
            
    
    except Exception as e:
        return ErrorAndLog.error(e, 'Console jsonAdd')



def wget(fileName, fileLink):
    try:
        if os.path.exists("database/dl"):
            shutil.rmtree("database/dl")
        os.mkdir("database/dl")

        fileName = (f"database/dl/{fileName}")
        with open(fileName, "wb") as f:
            print("Downloading %s" % fileName)
            response = requests.get(fileLink, stream=True)
            totalLength = response.headers.get('content-length')

            if totalLength is None:
                f.write(response.content)
            else:
                dl = 0
                totalLength = int(totalLength)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / totalLength)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()
        
        return fileName

    except Exception as e:
        return ErrorAndLog.error(e, 'Console wget')


def deleteDlFolder():
    try:
        if os.path.exists("database/dl"):
            shutil.rmtree("database/dl")
    
    except Exception as e: 
        return ErrorAndLog.error(e, "nstallApps deleteDlFolder")

def getMemory():
    try:
        if os.name == "posix":
            totalMemory, usedMemory, freeMemory = map(
            int, os.popen('free -t -m').readlines()[-1].split()[1:])

        else:
            memoryInfo = subprocess.getoutput("wmic MemoryChip get /format:list")
            memoryInfo = memoryInfo.split("\n")
            
            totalMemory = 0
            for line in memoryInfo:
                if line.startswith("Capacity="):
                    totalMemory += int(int(line.split("Capacity=")[-1]) / 1073741824)
            
        return totalMemory

    except Exception as e:
        return ErrorAndLog.error(e, 'Console getMemory')


def startInit():#on start clear and shows menu
    try:
        clear()
        menu()

    except Exception as e:
        return ErrorAndLog.error(e, 'Console startInit')