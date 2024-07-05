import subprocess
import sys
import os

def isForced(args, os_name):
    if hasattr(args, 'f') and args.f:
        return f"os/linux/main.py"
    return f"os/{os_name}/main.py"

def isHaveArgs(args):
    if args is not None:
        return sys.argv[1:]
    return []

def runOsCode(os_name, args=None):
    if os_name != "unknown":
        command = ["python", isForced(args, os_name)] + isHaveArgs(args)
        subprocess.run(command)
    else:
        print("Program does not support this OS right now. You can try starting with '-f' to proceed, although it may run into errors.")
