import keyboard
import time
import os
import json
import sys
# Path to the 'utils' directory
currentDir = os.path.dirname(os.path.abspath(__file__))
configFilePath = os.path.join(currentDir, '../../config.json')
utilsDir = os.path.join(currentDir, '../../utils')
sys.path.append(utilsDir)
import runScript

with open(configFilePath, 'r') as f:
    config = json.load(f)
# Pressed key timestamps are stored in a dictionary
pressTimes = {}
# Key status is stored in a dictionary
keyStatus = {}

def onKeyEvent(event, queue):
    if event.event_type == 'down' and not keyStatus.get(event.name, False) and event.name in config:
        # Key pressed, store the timestamp
        pressTimes[event.name] = time.time()
        queue.put((event.name, 'pressed', pressTimes[event.name]))
        if 'repeatPress' in config[event.name] and config[event.name]['repeatPress']:
            keyStatus[event.name] = True
            keyboard.send('backspace')
            # keyboard.send(event.name)
    elif event.event_type == 'up':
        # Key released, calculate the duration
        releaseTime = time.time()
        if event.name in pressTimes:
            pressTime = pressTimes.pop(event.name)
            duration = releaseTime - pressTime
            keyStatus[event.name] = False
            queue.put((event.name, 'released', duration))
        else:
            if event.name in config and 'repeatPress' in config[event.name] and config[event.name]['repeatPress']:
                # keyboard.send(event.name)
                #keyboard.release(event.name)
                print("test")

def startKeyCapture(queue):
    keyboard.hook(lambda event: onKeyEvent(event, queue))
    keyboard.wait('esc')
