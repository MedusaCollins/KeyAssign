import os
import json
import sys

currentDir = os.path.dirname(os.path.abspath(__file__))

def getConfigName(args):
    if len(args) > 1 and args[1] == '-c':
        return args[2]
    return "config.json"

def readConfig(args):
    configFilePath = os.path.join(currentDir, '../' + getConfigName(args))
    try:
        with open(configFilePath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Invalid JSON in config file.")
        sys.exit(1);

def isForced(args):
    if hasattr(args, 'f') and args.f:
        return True
    return False

def isHaveArgs(args):
    if args is not None:
        return sys.argv[1:]
    return []
