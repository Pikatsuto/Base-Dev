import os
from libs.package import Console
from libs.package import ErrorAndLog

fileName = "InstallApps"


def install_exe(file_link, file_name):
    functionName = "installExe"

    try:
        ErrorAndLog.debug_test(function=functionName, my_file=file_name, number=0, condition="Initial while")
        if os.name != "posix":
            ErrorAndLog.debug_test(function=functionName, my_file=file_name, number=1, condition="If in Windows")
            filePath = Console.wget(file_link=file_link, file_name=file_name).replace("/", "\\")
            os.system(filePath)
            Console.clear()

            Console.delete_dl_folder()

    except Exception as e:
        return ErrorAndLog.error_handler(e, f"{file_name} {functionName}")
