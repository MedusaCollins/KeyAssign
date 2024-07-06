import argparse
from utils.argList import upload, download, config


argList = [
    ["v", "Display the program's version information.", lambda args: print("Version 0.0.1"), 'store_true'],
    ["d", "Download and convert the JWT format back into a config file. (usage: -d <fileName.json> <JwtToken>)", download, 'multipleStore'],
    ["u", "Upload and convert the config file into JWT format for others to download. (usage: -u <fileName.json>)", upload, 'store'],
    ["c", "Allow the user to specify a configuration file (usage: -c <fileName.json>).", config, 'store'],
    ["f", "Force the program to run. Note that this may result in unexpected behavior or errors.", config, 'store_true']
    # ["d", "Enable debugging mode for the program.", inprogress, 'store_true'],
]

def createParser():
    parser = argparse.ArgumentParser(description='KeyAssign, an open-source tool, simplifies computer control by adding a programmable layer between your keyboard and computer, allowing customization of actions for each key press, distinguishing it from standard macros.')

    for param, description, detail, action in argList:
        if action == 'store_true':
            parser.add_argument('-'+param, action=action, help=description)
        elif action == 'multipleStore':
            parser.add_argument('-'+param, nargs='+', action='store', help=description)
        else:
            parser.add_argument('-'+param, action=action, help=description)
    return parser

def processArgs(args):
    for param, description, detail, action in argList:
        if getattr(args, param):
            detail(args)
            return True
    return False
