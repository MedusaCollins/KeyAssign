import keyboard
import time

# Pressed key timestamps are stored in a dictionary
pressTimes = {}
# Key status is stored in a dictionary
keyStatus = {}

def onKeyEvent(event, queue):
    if event.event_type == 'down' and not keyStatus.get(event.name, False):
        # Key pressed, store the timestamp
        pressTimes[event.name] = time.time()
        keyStatus[event.name] = True
        queue.put((event.name, 'pressed', pressTimes[event.name]))
    elif event.event_type == 'up':
        # Key released, calculate the duration
        releaseTime = time.time()
        if event.name in pressTimes:
            pressTime = pressTimes.pop(event.name)
            duration = releaseTime - pressTime
            keyStatus[event.name] = False
            queue.put((event.name, 'released', duration))

def startKeyCapture(queue):
    keyboard.hook(lambda event: onKeyEvent(event, queue))
    keyboard.wait('esc')
