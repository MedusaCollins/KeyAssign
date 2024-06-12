import platform
def get_os():
    os = platform.system()
    if os in ["Windows", "Darwin", "Linux"]:
        if os == "Darwin":
            return "mac"
        return os.lower()
    else:
        return "unknown"
