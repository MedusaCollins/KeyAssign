import keyboard
import time
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'/../../utils')
from handleBloat import readConfig

pressTimes = {}
keyStatus = {}

def onKeyEvent(event, queue):

    if event.event_type == 'down' and not keyStatus.get(event.name, False) and event.name in config:
        pressTimes[event.name] = time.time()
        queue.put((event.name, 'pressed', pressTimes[event.name]))
        keyStatus[event.name] = True
        keyboard.send('backspace')
    elif event.event_type == 'up' and event.name in pressTimes:
        releaseTime = time.time()
        pressTime = pressTimes.pop(event.name)
        duration = releaseTime - pressTime
        keyStatus[event.name] = False
        queue.put((event.name, 'released', duration))
        keyboard.send('backspace')

def startKeyCapture(queue, args):
    global config
    config = readConfig(args)
    keyboard.hook(lambda event: onKeyEvent(event, queue))
    keyboard.wait("esc")
