import platform
from utils.handleBloat import isForced
def getOs(args=None):
    os = 'Linux' if isForced(args) else platform.system()
    if os in ["Windows", "Darwin", "Linux"]:
        if os == "Darwin":
            return "mac"
        return os.lower()
    else:
        return "unknown"
