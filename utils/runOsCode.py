import subprocess

def runOsCode(os):
    if os != "unknown":
        subprocess.run(["python", f"os/{os}/main.py"])
    else:
        print("Program does not support this OS right now. You can try starting with '-force osName' to proceed, although it may run into errors.")
