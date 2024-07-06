from utils.runOsCode import runOsCode
from utils.getOs import getOs
import os
import json
import sys
import jwt

def config(args):
    runOsCode(getOs(args), args)

def upload(args):
    currentDir = os.path.dirname(os.path.abspath(__file__))
    configFilePath = os.path.join(currentDir, '../' + args.u)
    try:
        with open(configFilePath, 'r') as f:
            config = json.load(f)
            encodedConfig = jwt.encode(config, "secret", algorithm="HS256")
            print(encodedConfig)
    except FileNotFoundError:
        print("Invalid JSON in config file.")
        sys.exit(1);

def download(args):
    decodedConfig = jwt.decode(args.d[1], "secret", algorithms=["HS256"])
    with open(args.d[0], 'w') as f:
        json.dump(decodedConfig, f)
        print(f"Your config file named {args.d[0]} has been created.")
