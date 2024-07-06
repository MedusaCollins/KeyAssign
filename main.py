from utils.getOs import getOs
from utils.runOsCode import runOsCode
from utils.handleArgumentParser import createParser, processArgs

def main():
    parser = createParser()
    args = parser.parse_args()

    if not processArgs(args):
        osName = getOs(args)
        runOsCode(osName)

if __name__ == "__main__":
    main()
