import json
import os
import shutil
import subprocess
import sys

import requests
from termcolor import colored

from libs.package import error_and_log

fileName = "console"


with open("database/consoleStartMessage.json") as file:
    consoleStartMessage = json.load(file)


def console_input_handler(input_text=False, lower=True):
    function_name = "consoleInput"

    try:
        error_and_log.debug_test(
            function=function_name,
            my_file=fileName,
            number=0,
            condition="Initial While",
        )
        if not input_text:
            error_and_log.debug_test(
                function=function_name,
                my_file=fileName,
                number=1,
                condition="If not input text",
            )
            console_input = input(f'{colored(consoleStartMessage["user"], "green")}>> ')
        else:
            error_and_log.debug_test(
                function=function_name,
                my_file=fileName,
                number=1,
                condition="If input text",
            )
            console_input = input(
                f'{colored(input_text, "cyan")} / {colored(consoleStartMessage["user"], "green")}>> '
            )

        if lower:
            error_and_log.debug_test(
                function=function_name, my_file=fileName, number=1, condition="If lower"
            )
            console_input.lower()

        if console_input == "exit":
            error_and_log.debug_test(
                function=function_name, my_file=fileName, number=1, condition="If exit"
            )
            error_and_log.exit_command()

        if console_input == "restart":
            error_and_log.debug_test(
                function=function_name,
                my_file=fileName,
                number=1,
                condition="If restart",
            )
            error_and_log.restart()

        elif console_input != "":
            error_and_log.debug_test(
                function=function_name,
                my_file=fileName,
                number=1,
                condition="If console input is void",
            )
            error_and_log.log_handler(console_input, False, "user")

        return console_input

    except Exception as e:
        return error_and_log.error_handler(e, f"{fileName} {function_name}")


def motd():  # show start menu
    function_name = "motd"

    try:
        error_and_log.debug_test(
            function=function_name, my_file=fileName, number=0, condition="Print MOTD"
        )

        print(
            colored(
                "# --------------------------------------------------------------------------- #",
                "green",
            )
        )
        print()
        print("   888888b.                                     8888888b.")
        print('   888  "88b                                    888  "Y88b')
        print("   888  .88P                                    888    888")
        print(
            "   8888888K.   8888b.  .d8888b   .d88b.         888    888  .d88b.  888  888"
        )
        print(
            '   888  "Y88b     "88b 88K      d8P  Y8b        888    888 d8P  Y8b 888  888'
        )
        print(
            '   888    888 .d888888 "Y8888b. 88888888        888    888 88888888 Y88  88P'
        )
        print(
            "   888   d88P 888  888      X88 Y8b.            888  .d88P Y8b.      Y8bd8P"
        )
        print(
            '   8888888P"  "Y888888  88888P\'  "Y8888         8888888P"   "Y8888    Y88P'
        )
        print()
        print("                                  By Pikatsuto")
        print(
            colored(
                "# --------------------------------------------------------------------------- #",
                "green",
            )
        )
        print(
            colored("\nWelcome", "green"),
            "for Base Dev shell",
            colored("\n[?]", "cyan"),
            "For Help command\n",
        )

    except Exception as e:
        return error_and_log.error_handler(e, f"{fileName} {function_name}")


def clear():  # use clear command
    function_name = "clear"

    try:
        error_and_log.debug_test(
            function=function_name,
            my_file=fileName,
            number=0,
            condition="Initial While",
        )
        if os.name == "posix":
            error_and_log.debug_test(
                function=function_name,
                my_file=fileName,
                number=1,
                condition="If on Linux",
            )
            os.system("clear")
        else:
            error_and_log.debug_test(
                function=function_name,
                my_file=fileName,
                number=1,
                condition="If on Wine",
            )
            os.system("cls")

    except Exception as e:
        return error_and_log.error_handler(e, f"{fileName} {function_name}")


def wget(file_name, file_link):
    function_name = "wget"

    try:
        error_and_log.debug_test(
            function=function_name,
            my_file=file_name,
            number=0,
            condition="Initial While Wget",
        )
        if os.path.exists("database/dl"):
            error_and_log.debug_test(
                function=function_name,
                my_file=file_name,
                number=1,
                condition="Initial if download file exist",
            )
            shutil.rmtree("database/dl")
        os.mkdir("database/dl")

        file_name = f"database/dl/{file_name}"
        with open(file_name, "wb") as f:
            error_and_log.debug_test(
                function=function_name,
                my_file=file_name,
                number=1,
                condition="Open download file",
            )
            print(f"Downloading {file_name}")
            response = requests.get(file_link, stream=True)
            total_length = response.headers.get("content-length")

            if total_length is None:
                error_and_log.debug_test(
                    function=function_name,
                    my_file=file_name,
                    number=2,
                    condition="if Length of file si void",
                )
                f.write(response.content)
            else:
                error_and_log.debug_test(
                    function=function_name,
                    my_file=file_name,
                    number=2,
                    condition="if Length of file is defined",
                )
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    error_and_log.debug_test(
                        function=function_name,
                        my_file=file_name,
                        number=3,
                        condition="for write data fin file",
                    )
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ("=" * done, " " * (50 - done)))
                    sys.stdout.flush()

        return file_name

    except Exception as e:
        return error_and_log.error_handler(e, f"{file_name} {function_name}")


def delete_dl_folder():
    function_name = "deleteDlFolder"

    try:
        if os.path.exists("database/dl"):
            error_and_log.debug_test(
                function=function_name,
                my_file=fileName,
                number=0,
                condition="if download folder exist",
            )
            shutil.rmtree("database/dl")

    except Exception as e:
        return error_and_log.error_handler(e, f"{fileName} {function_name}")


def get_memory():
    function_name = "getMemory"

    try:
        error_and_log.debug_test(
            function=function_name,
            my_file=fileName,
            number=0,
            condition="Initial While",
        )
        if os.name == "posix":
            error_and_log.debug_test(
                function=function_name,
                my_file=fileName,
                number=1,
                condition="if on Linux",
            )
            total_memory, used_memory, free_memory = map(
                int, os.popen("free -t -m").readlines()[-1].split()[1:]
            )

        else:
            error_and_log.debug_test(
                function=function_name,
                my_file=fileName,
                number=0,
                condition="if on Windows",
            )
            memory_info = subprocess.getoutput("wmic MemoryChip get /format:list")
            memory_info = memory_info.split("\n")

            total_memory = sum(
                int(line.split("Capacity=")[-1]) // 1073741824
                for line in memory_info
                if line.startswith("Capacity=")
            )

        return total_memory

    except Exception as e:
        return error_and_log.error_handler(e, f"{fileName} {function_name}")


def start_init():  # on start clear and shows menu
    function_name = "startInit"

    try:
        error_and_log.debug_test(
            function=function_name,
            my_file=fileName,
            number=0,
            condition="Initial while",
        )
        clear()
        motd()

    except Exception as e:
        return error_and_log.error_handler(e, f"{fileName} {function_name}")
