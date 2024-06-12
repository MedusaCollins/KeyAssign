import subprocess

def runOsCode(os):
    if os != "unknown":
        subprocess.run(["python", f"os/{os}/main.py"])
    else:
        print("Bilinmeyen işletim sistemi")
