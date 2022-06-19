from libs.package import console, help, error_and_log

fileName = "Main"


def main():
    function_name = "console"

    try:
        commands = {
            "allCommand": {
                "clear": {
                    "command": console.clear,
                    "arguments": False
                },
                "?": {
                    "command": help.start_init,
                    "arguments": {
                        "default": [False],
                        "dev": True
                    }
                },
                "debug": {
                    "command": error_and_log.debug_mode,
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
            error_and_log.debug_test(function=function_name, my_file=fileName, number=0, condition="Initial")
            console_input = console.console_input_handler()

            if start:
                error_and_log.debug_test(function=function_name, my_file=fileName, number=1, condition="if first start")
                start = False
                console.clear()

            elif console_input == "":
                error_and_log.debug_test(function=function_name, my_file=fileName, number=1,
                                       condition="elif consoleInput == \"\"")
            else:  # check if console input is on command json
                error_and_log.debug_test(function=function_name, my_file=fileName, number=1,
                                       condition="else: check json command")
                console_input_split = console_input.split(" ")
                arguments = console_input_split
                command_save = False
                arguments_ok = False

                command = commands["allCommand"]
                if console_input_split[0] in command:
                    error_and_log.debug_test(function=function_name, my_file=fileName, number=2,
                                           condition="if your command in all command")
                    command_save = command[console_input_split[0]]["command"]
                    if command[console_input_split[0]]["arguments"]:
                        error_and_log.debug_test(function=function_name, my_file=fileName, number=3,
                                               condition="if your command have argument")
                        if not command[console_input_split[0]]["arguments"]["default"] and len(arguments) == 1:
                            error_and_log.debug_test(function=function_name, my_file=fileName, number=4,
                                                   condition="if your command have default argument")
                            arguments = command[console_input_split[0]]["arguments"]["default"][0]
                            arguments_ok = True
                        else:
                            error_and_log.debug_test(function=function_name, my_file=fileName, number=4,
                                                   condition="else your command not have default argument")
                            for argumentsInput in arguments:
                                error_and_log.debug_test(function=function_name, my_file=fileName, number=5,
                                                       condition="for your argument on all argument")
                                if argumentsInput in command[console_input_split[0]]["arguments"]:
                                    error_and_log.debug_test(function=function_name, my_file=fileName, number=6,
                                                           condition="if your argument in all argument")
                                    arguments = command[console_input_split[0]]["arguments"][argumentsInput]
                                    arguments_ok = True
                                    break
                                else:
                                    arguments_ok = False
                            if not arguments_ok:
                                error_and_log.debug_test(function=function_name, my_file=fileName, number=5,
                                                       condition="argument not fund set default argument")
                                arguments = command[console_input_split[0]]["arguments"]["default"][0]
                                arguments_ok = True

            if command_save and arguments_ok:  # Execute function for command
                error_and_log.debug_test(function=function_name, my_file=fileName, number=1,
                                       condition="if your command have argument")
                command_save(arguments)

            elif command_save:
                error_and_log.debug_test(function=function_name, my_file=fileName, number=1,
                                       condition="elif your command not have argument")
                command_save()
            else:
                error_and_log.log_handler(f"command \"{console_input}\" no fund", True, "log")

    except Exception as e:
        return error_and_log.error_handler(e, f"{fileName} {function_name}")


def start_init():
    function_name = "startInit"

    try:
        error_and_log.debug_test(function=function_name, my_file=fileName, number=1, condition="Start Program")
        console.start_init()
        main()

    except Exception as e:
        return error_and_log.error_handler(e, f"{fileName} {function_name}")


start_init()
