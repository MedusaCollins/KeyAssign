import subprocess
from utils.handleBloat import isHaveArgs

def runOsCode(osName, args=None):
    if osName != "unknown":
        command = ["python", f"os/{osName}/main.py"] + isHaveArgs(args)
        subprocess.run(command)
    else:
        print("Program does not support this OS right now. You can try starting with '-f' to proceed, although it may run into errors.")
