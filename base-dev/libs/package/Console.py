import json
import os
import shutil
import subprocess
import sys

from libs.package import ErrorAndLog

fileName = "Console"

try:
    from termcolor import colored

    ErrorAndLog.debug_test(function="No Function", my_file=fileName, number=0, condition="Check termcolor libs")
except ModuleNotFoundError:
    ErrorAndLog.debug_test(function="No Function", my_file=fileName, number=0, condition="Check install libs")
    ErrorAndLog.install_python_libs("termcolor")

try:
    import requests

    ErrorAndLog.debug_test(function="No Function", my_file=fileName, number=0, condition="Check request libs")
except ModuleNotFoundError:
    ErrorAndLog.debug_test(function="No Function", my_file=fileName, number=0, condition="Check request libs")
    ErrorAndLog.install_python_libs("requests")

with open("database/consoleStartMessage.json") as file:
    consoleStartMessage = json.load(file)


def console_input_handler(input_text=False, lower=True):
    function_name = "consoleInput"

    try:
        ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=0, condition="Initial While")
        if not input_text:
            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1, condition="If not input text")
            console_input = input(f'{colored(consoleStartMessage["user"], "green")}>> ')
        else:
            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1, condition="If input text")
            console_input = input(
                f'{colored(input_text, "cyan")} / {colored(consoleStartMessage["user"], "green")}>> '
            )

        if lower:
            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1, condition="If lower")
            console_input.lower()

        if console_input == "exit":
            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1, condition="If exit")
            ErrorAndLog.exit_command()

        if console_input == "restart":
            ErrorAndLog.debug_test(
                function=function_name, my_file=fileName, number=1, condition="If restart"
            )
            ErrorAndLog.restart()

        elif console_input != "":
            ErrorAndLog.debug_test(
                function=function_name, my_file=fileName, number=1, condition="If console input is void"
            )
            ErrorAndLog.log_handler(console_input, False, "user")

        return console_input

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{fileName} {function_name}")


def motd():  # show start menu
    function_name = "motd"

    try:
        ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=0, condition="Print MOTD")

        print(colored("# --------------------------------------------------------------------------- #", "green"))
        print()
        print("   888888b.                                     8888888b.")
        print("   888  \"88b                                    888  \"Y88b")
        print("   888  .88P                                    888    888")
        print("   8888888K.   8888b.  .d8888b   .d88b.         888    888  .d88b.  888  888")
        print("   888  \"Y88b     \"88b 88K      d8P  Y8b        888    888 d8P  Y8b 888  888")
        print("   888    888 .d888888 \"Y8888b. 88888888        888    888 88888888 Y88  88P")
        print("   888   d88P 888  888      X88 Y8b.            888  .d88P Y8b.      Y8bd8P")
        print("   8888888P\"  \"Y888888  88888P'  \"Y8888         8888888P\"   \"Y8888    Y88P")
        print()
        print("                                  By Pikatsuto")
        print(colored("# --------------------------------------------------------------------------- #", "green"))
        print(colored("\nWelcome", "green"), "for Base Dev shell", colored("\n[?]", "cyan"), "For Help commande\n")

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{fileName} {function_name}")


def clear():  # use clear commande
    function_name = "clear"

    try:
        ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=0, condition="Initial While")
        if os.name == "posix":
            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1, condition="If on Linux")
            os.system("clear")
        else:
            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1, condition="If on Wine")
            os.system("cls")

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{fileName} {function_name}")


def wget(file_name, file_link):
    function_name = "wget"

    try:
        ErrorAndLog.debug_test(function=function_name, my_file=file_name, number=0, condition="Initial While Wget")
        if os.path.exists("database/dl"):
            ErrorAndLog.debug_test(function=function_name, my_file=file_name, number=1,
                                   condition="Initial if download file exist")
            shutil.rmtree("database/dl")
        os.mkdir("database/dl")

        file_name = f"database/dl/{file_name}"
        with open(file_name, "wb") as f:
            ErrorAndLog.debug_test(function=function_name, my_file=file_name, number=1, condition="Open download file")
            print(f"Downloading {file_name}")
            response = requests.get(file_link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:
                ErrorAndLog.debug_test(function=function_name, my_file=file_name, number=2,
                                       condition="if Length of file si void")
                f.write(response.content)
            else:
                ErrorAndLog.debug_test(function=function_name, my_file=file_name, number=2,
                                       condition="if Length of file is defined")
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    ErrorAndLog.debug_test(function=function_name, my_file=file_name, number=3,
                                           condition="for write data fin file")
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                    sys.stdout.flush()

        return file_name

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{file_name} {function_name}")


def delete_dl_folder():
    function_name = "deleteDlFolder"

    try:
        if os.path.exists("database/dl"):
            ErrorAndLog.debug_test(
                function=function_name, my_file=fileName, number=0, condition="if download folder exist"
            )
            shutil.rmtree("database/dl")

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{fileName} {function_name}")


def get_memory():
    function_name = "getMemory"

    try:
        ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=0, condition="Initial While")
        if os.name == "posix":
            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1, condition="if on Linux")
            total_memory, used_memory, free_memory = map(
                int, os.popen('free -t -m').readlines()[-1].split()[1:])

        else:
            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=0, condition="if on Windows")
            memory_info = subprocess.getoutput("wmic MemoryChip get /format:list")
            memory_info = memory_info.split("\n")

            total_memory = sum(
                int(line.split("Capacity=")[-1]) // 1073741824 for line in memory_info if line.startswith("Capacity="))

        return total_memory

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{fileName} {function_name}")


def start_init():  # on start clear and shows menu
    function_name = "startInit"

    try:
        ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=0, condition="Initial while")
        clear()
        motd()

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{fileName} {function_name}")
