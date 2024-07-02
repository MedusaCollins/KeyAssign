import json
import os
import time
import keyboard
import subprocess
import sys

# Path to the 'utils' directory
currentDir = os.path.dirname(os.path.abspath(__file__))
configFilePath = os.path.join(currentDir, '../../config.json')
utilsDir = os.path.join(currentDir, '../../utils')
sys.path.append(utilsDir)
import runScript

with open(configFilePath, 'r') as f:
    config = json.load(f)

def processKeyEvents(queue):
    while True:
        event = queue.get()
        if event:
            key, action, timestampOrDuration = event
            if action == 'pressed':
                print(f"Key {key} pressed.")
                if key in config:
                    item = config[key]
            elif action == 'released':
                if key in config:
                    item = config[key]
                    if item['durationBetween'][0] <= timestampOrDuration <= item['durationBetween'][1]:
                        if item['type'] == 'text':
                            typingDelay = item.get('typingDelay', 0.1)
                            for char in item['value']:
                                keyboard.press(char)
                                time.sleep(typingDelay)
                                keyboard.release(char)
                        elif item['type'] == 'script':
                            scriptPath = item.get('import')
                            if scriptPath:
                                runScript.runScript(scriptPath)

if __name__ == "__main__":
    import multiprocessing
    import keyCaptures

    queue = multiprocessing.Queue()
    captureProcess = multiprocessing.Process(target=keyCaptures.startKeyCapture, args=(queue,))
    captureProcess.start()

    processKeyEvents(queue)
    captureProcess.join()
