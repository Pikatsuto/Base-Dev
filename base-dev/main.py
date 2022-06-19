from libs.package import Console, Help, ErrorAndLog

fileName = "Main"


def console():
    function_name = "console"

    try:
        commands = {
            "allCommand": {
                "clear": {
                    "command": Console.clear,
                    "arguments": False
                },
                "?": {
                    "command": Help.start_init,
                    "arguments": {
                        "default": [False],
                        "dev": True
                    }
                },
                "debug": {
                    "command": ErrorAndLog.debug_mode,
                    "arguments": {
                        "default": [True],
                        "o": True,
                        "n": False
                    }
                }
            }
        }

        start = False
        while True:
            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=0, condition="Initial")
            console_input = Console.console_input_handler()

            if start:
                ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1, condition="if first start")
                start = False
                Console.clear()

            elif console_input == "":
                ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1,
                                       condition="elif consoleInput == \"\"")
            else:  # check if console input is on command json
                ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1,
                                       condition="else: check json command")
                console_input_split = console_input.split(" ")
                arguments = console_input_split
                command_save = False
                arguments_ok = False

                command = commands["allCommand"]
                if console_input_split[0] in command:
                    ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=2,
                                           condition="if your command in all command")
                    command_save = command[console_input_split[0]]["command"]
                    if command[console_input_split[0]]["arguments"]:
                        ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=3,
                                               condition="if your command have argument")
                        if not command[console_input_split[0]]["arguments"]["default"] and len(arguments) == 1:
                            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=4,
                                                   condition="if your command have default argument")
                            arguments = command[console_input_split[0]]["arguments"]["default"][0]
                            arguments_ok = True
                        else:
                            ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=4,
                                                   condition="else your command not have default argument")
                            for argumentsInput in arguments:
                                ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=5,
                                                       condition="for your argument on all argument")
                                if argumentsInput in command[console_input_split[0]]["arguments"]:
                                    ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=6,
                                                           condition="if your argument in all argument")
                                    arguments = command[console_input_split[0]]["arguments"][argumentsInput]
                                    arguments_ok = True
                                    break
                                else:
                                    arguments_ok = False
                            if not arguments_ok:
                                ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=5,
                                                       condition="argument not fund set default argument")
                                arguments = command[console_input_split[0]]["arguments"]["default"][0]
                                arguments_ok = True

            if command_save and arguments_ok:  # Execute fonction for command
                ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1,
                                       condition="if your command have argument")
                command_save(arguments)

            elif command_save:
                ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1,
                                       condition="elif your command not have argument")
                command_save()
            else:
                ErrorAndLog.log_handler(f"command \"{console_input}\" no fund", True, "log")

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{fileName} {function_name}")


def start_init():
    function_name = "startInit"

    try:
        ErrorAndLog.debug_test(function=function_name, my_file=fileName, number=1, condition="Start Program")
        Console.start_init()
        console()

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{fileName} {function_name}")


start_init()
