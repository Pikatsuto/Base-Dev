import os
from libs.package import console
from libs.package import error_and_log

fileName = "InstallApps"


def install_exe(file_link, file_name):
    func = "installExe"

    try:
        error_and_log.debug_test(
            function=func, my_file=file_name, number=0, condition="Initial while"
        )
        if os.name != "posix":
            error_and_log.debug_test(
                function=func, my_file=file_name, number=1, condition="If in Windows"
            )
            file_path = console.wget(file_link=file_link, file_name=file_name).replace(
                "/", "\\"
            )
            os.system(file_path)
            console.clear()

            console.delete_dl_folder()

    except Exception as e:
        return error_and_log.error_handler(e, f"{file_name} {func}")
