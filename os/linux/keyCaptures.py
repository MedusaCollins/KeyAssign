import keyboard
import time

# Tuş basış zamanlarını saklamak için bir sözlük
press_times = {}
# Tuşun basılı olup olmadığını kontrol etmek için bir sözlük
key_status = {}

def on_key_event(event, queue):
    if event.event_type == 'down' and not key_status.get(event.name, False):
        # Tuşa basıldığında ve daha önce basılmadığında zaman damgasını kaydet
        press_times[event.name] = time.time()
        key_status[event.name] = True
        queue.put((event.name, 'pressed', press_times[event.name]))
    elif event.event_type == 'up':
        # Tuş serbest bırakıldığında zaman damgasını al
        release_time = time.time()
        if event.name in press_times:
            press_time = press_times.pop(event.name)
            duration = release_time - press_time
            key_status[event.name] = False
            queue.put((event.name, 'released', duration))

def start_key_capture(queue):
    keyboard.hook(lambda event: on_key_event(event, queue))
    keyboard.wait('esc')
