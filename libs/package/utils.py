import os
import shutil
import sys
import psutil
import requests
import console


def wget(file_name, file_link):
    if os.path.exists("database/dl"):
        shutil.rmtree("database/dl")
    os.mkdir("database/dl")

    file_name = f"database/dl/{file_name}"
    with open(file_name, "wb") as f:
        print(f"Downloading {file_name}")
        response = requests.get(file_link, stream=True)
        total_length = response.headers.get("content-length")

        if total_length is None:
            f.write(response.content)

        else:
            dl = 0
            total_length = int(total_length)

            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ("=" * done, " " * (50 - done)))
                sys.stdout.flush()

    return file_name


def delete_dl_folder():
    if not os.path.exists("database/dl"):
        return False
    shutil.rmtree("database/dl")
    return True


def get_memory():
    vm = psutil.virtual_memory()
    mb = 1024 * 1024

    return {
        "used": (vm.used / mb),
        "percent_user": vm.percent,
        "total": (vm.total / mb),
        "free": ((vm.total / mb) - (vm.used / mb))
    }


def get_cpu():
    cpu_freq = psutil.cpu_freq()

    return {
        "core": psutil.cpu_count(logical=False),
        "thread": psutil.cpu_count(),
        "actual_frequency": (cpu_freq.current / 1000),
        "max_frequency": (cpu_freq.max / 1000),
        "usage": psutil.cpu_percent(),
        "usage_per_core": psutil.cpu_percent(percpu=True)
    }


def install_exe(file_link, file_name):
    if os.name != "posix":
        file_path = wget(file_link=file_link, file_name=file_name).replace(
            "/", "\\"
        )
        os.system(file_path)
        console.clear()

        delete_dl_folder()
