import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'/../../utils')
import multiprocessing
import keyCaptures
from runPlugin import runPlugin
from handleBloat import readConfig
import keyboard
import time

def processKeyEvents(queue, args):
    config = readConfig(args)
    while True:
        event = queue.get()
        if event:
            key, action, timestampOrDuration = event
            if key in config:
                items = config[key]
                actionExecuted = False
                for item in items:
                    if action == 'released' and item['durationBetween'][0] <= timestampOrDuration <= item['durationBetween'][1]:
                        actionExecuted = True
                        if "typingValue" in item:
                            typingDelay = item.get('typingDelay', 0)
                            for char in item['typingValue']:
                                keyboard.press(char)
                                time.sleep(typingDelay)
                                keyboard.release(char)
                        elif "import" in item:
                            scriptPath = item.get('import')
                            if scriptPath:
                                runPlugin(scriptPath)
                        elif "pressingValues" in item:
                            pressingValues = item.get('pressingValues')
                            for char in pressingValues:
                                keyboard.press(char['key'])
                                time.sleep(char['duration'])
                                keyboard.release(char['key'])
                if not actionExecuted:
                    keyboard.press(key)
                    keyboard.release(key)

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    captureProcess = multiprocessing.Process(target=keyCaptures.startKeyCapture, args=(queue,))
    captureProcess.start()

    processKeyEvents(queue, sys.argv)
    captureProcess.join()
