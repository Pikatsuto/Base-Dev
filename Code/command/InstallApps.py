import os
from command import ErrorAndLog, Console

def installExe(fileLink, fileName):
    try:
        if os.name != "posix":            
            filePath = Console.wget(fileLink=fileLink, fileName=fileName).replace("/", "\\")
            os.system(filePath)
            Console.clear()

            Console.deleteDlFolder()
    
    except Exception as e:
        return ErrorAndLog.error(e, "InstallApps installJava")

def installPythonLibs(libs):
    try:
        if os.name == "posix":
            os.system(f"python -m pip install {libs}")
        else:
            os.system(f"py -m pip install {libs}")
    except Exception as e:
        return ErrorAndLog.error(e, "InstallApps installPythonLibs")
