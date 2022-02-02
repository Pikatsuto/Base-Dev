import os
from command import Console, ErrorAndLog

def installExe(fileLink, fileName):
    try:
        if os.name != "posix":            
            filePath = Console.wget(fileLink=fileLink, fileName=fileName).replace("/", "\\")
            os.system(filePath)
            Console.clear()

            Console.deleteDlFolder()
    
    except Exception as e:
        return ErrorAndLog.error(e, "InstallApps installJava")
