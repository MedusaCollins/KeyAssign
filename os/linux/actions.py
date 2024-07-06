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
                item = config[key]
                if action == 'released' and item['durationBetween'][0] <= timestampOrDuration <= item['durationBetween'][1]:
                    if item['type'] == 'text':
                        typingDelay = item.get('typingDelay', 0)
                        for char in item['value']:
                            keyboard.press(char)
                            time.sleep(typingDelay)
                            keyboard.release(char)
                    else:
                        scriptPath = item.get('import')
                        if scriptPath:
                            runPlugin(scriptPath)
                elif action == 'released' and item['durationBetween'][0] > timestampOrDuration or action == 'released' and item['durationBetween'][1] < timestampOrDuration:
                    keyboard.press(key)
                    keyboard.release(key)

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    captureProcess = multiprocessing.Process(target=keyCaptures.startKeyCapture, args=(queue,))
    captureProcess.start()

    processKeyEvents(queue, sys.argv)
    captureProcess.join()
