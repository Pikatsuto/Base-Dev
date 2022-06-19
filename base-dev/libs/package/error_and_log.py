import json
import os
import shutil
from time import strftime

from database.info import Info


def python(command):
    if os.name == "posix":
        os.system(f"venv/bin/python {command}")
    else:
        os.system(f"venv\\Scripts\\python.exe {command}")


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
    time_read = strftime("%Y-%m-%d %H:%M:%S")
    time_file = strftime("%Y-%m-%d_%H-%M-%S")

    if get_type == "read":
        return time_read
    elif get_type == "file":
        return time_file
    else:
        return "error time"


with open("database/consoleStartMessage.json") as file:  # console start line
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

    time_read = time_get("read")
    time_file = time_get("file")

    if user == "log":
        my_log_message = f'{colored(consoleStartMessage[user], "blue")}>> {output}'
    elif user == "error":
        my_log_message = f'{colored(consoleStartMessage[user], "red")}>> {output}'
    elif user == "user":
        my_log_message = f'{colored(consoleStartMessage[user], "green")}>> {output}'
    elif user == "console":
        my_log_message = f'{colored(consoleStartMessage[user], "yellow")}>> {output}'
    log_message_text = f"{consoleStartMessage[user]}>> {output}"

    if if_print:
        print(my_log_message)

    if os.path.exists("logs/logs.txt"):  # read, count logs and add time in logs
        with open("logs/logs.txt", "r+") as f:
            logs_file = f.read()

        with open("logs/logs.txt") as f:
            lines_of_logs = sum(1 for _ in f)

    else:
        logs_file = f"Start logs file : {time_read}\n"
        lines_of_logs = 3

    with open("logs/logs.txt", "w+") as f:  # save logs
        f.write(f"{logs_file}\n{time_read} / {log_message_text}")

    if lines_of_logs >= 997:  # create new logs file if logs line is > 1000
        if not os.path.exists("logs/old"):
            os.makedirs("logs/old")

        with open("logs/logs.txt", "w+") as f:
            f.write(f"{logs_file}\n{time_read} / {log_message_text}\n\nEnd logs file : {time_read}")

        shutil.move("logs/logs.txt", f"logs/old/logs_end_{time_file}.txt")

        old_logs_files = os.listdir("logs/old")
        if len(old_logs_files) >= 10:
            shutil.make_archive(f"logs/oldZip/logs_end_{time_file}", "zip", "logs/old")
            shutil.rmtree("logs/old")

    return my_log_message


def error_handler(error, function):  # send and save errors
    fatal = False

    time_read = time_get("read")
    time_file = time_get("file")

    error_message = f'{colored(consoleStartMessage["error"], "red")}>> {function} : {error}'
    error_message_text = f'{consoleStartMessage["error"]}>> {function} : {error}'
    log_error_message = f"{function} : {error}"

    if not os.path.exists("errors"):
        os.makedirs("errors")

    if os.path.exists("errors/errorsPerSecond.json"):  # read file of count error in one second
        with open("errors/errorsPerSecond.json", "r+") as f:
            errors_number_json = json.load(f)
            errors_number = errors_number_json["errors_number"]
            time_for_last_error = errors_number_json["time_for_last_error"]
            read_error_message = errors_number_json["read_error_message"]
    else:
        errors_number_json = {
            "errors_number": None,
            "time_for_last_error": None,
            "read_error_message": None
        }
        with open("errors/errorsPerSecond.json", "w+") as f:
            json.dump(errors_number_json, f)

        errors_number = 0
        time_for_last_error = ""

    errors_number += 1

    if errors_number >= 5 and time_for_last_error == time_file and read_error_message == error_message:  # stop program if 5
        # repetitive error
        errors_number = 0
        error_message = f'{colored(consoleStartMessage["error"], "red")}>> [FATAL] {function} : {error}'
        log_error_message = f"[FATAL] {function} : {error}"
        fatal = True

    elif time_for_last_error != time_file:  # reset file count error if one second over
        errors_number = 0

    errors_number_json = {
        "errors_number": errors_number,
        "time_for_last_error": time_file,
        "read_error_message": error_message
    }

    with open("errors/errorsPerSecond.json", "w+") as f:  # right file error in one second
        json.dump(errors_number_json, f)

    log_handler(log_error_message, False, "error")
    log_handler(log_error_message, True, "error")

    if os.path.exists("errors/errors.txt"):  # read, count errors and add time in errors
        with open("errors/errors.txt", "r+") as f:
            errors_file = f.read()

        with open("errors/errors.txt") as f:
            lines_of_errors = sum(1 for _ in f)

    else:
        errors_file = f"Start errors file : {time_read}\n"
        lines_of_errors = 3

    with open("errors/errors.txt", "w+") as f:
        f.write(f"{errors_file}\n{time_read} / {error_message_text}")

    if lines_of_errors >= 997:  # create new errors file if errors line is > 1000
        if not os.path.exists("errors/old"):
            os.makedirs("errors/old")

        with open("errors/errors.txt", "w+") as f:
            f.write(f"{errors_file}\n{time_read} / {error_message_text}\n\nEnd errors file : {time_read}")

        shutil.move("errors/errors.txt", f"errors/old/errors_end_{time_file}.txt")

        old_errors_files = os.listdir("errors/old")
        if len(old_errors_files) >= 10:
            shutil.make_archive(f"errors/oldZip/errors_end_{time_file}", "zip", "errors/old")
            shutil.rmtree("errors/old")

    if fatal:
        exit(0)

    return error_message
