import keyboard
import time

press_times = {}
key_status = {}

def on_key_event(event, queue):
    if event.event_type == 'down' and not key_status.get(event.name, False):
        press_times[event.name] = time.time()
        key_status[event.name] = True
        queue.put((event.name, 'pressed', press_times[event.name]))
    elif event.event_type == 'up':
        release_time = time.time()
        if event.name in press_times:
            press_time = press_times.pop(event.name)
            duration = release_time - press_time
            key_status[event.name] = False
            queue.put((event.name, 'released', duration))

def start_key_capture(queue):
    keyboard.hook(lambda event: on_key_event(event, queue))
    keyboard.wait('esc')
