from pynput import keyboard
import time

# Set to keep track of pressed keys and their press times
keys_pressed = {}
press_times = {}

def on_press(key):
    try:
        if key.char not in keys_pressed:
            keys_pressed[key.char] = time.time()
            print(f'Key {key} pressed')
        else:
            keyboard.Controller().press(keyboard.Key.backspace)
            keyboard.Controller().release(keyboard.Key.backspace)
    except AttributeError:
        if key not in keys_pressed:
            keys_pressed[key] = time.time()
            print(f'Special Key {key} pressed')
def on_release(key):
    try:
        if key.char in keys_pressed:
            press_time = keys_pressed.pop(key.char)
            duration = time.time() - press_time
            if duration > 0.01:
                print(f'Key {key} released after {duration:.2f} seconds')
    except AttributeError:
        if key in keys_pressed:
            press_time = keys_pressed.pop(key)
            duration = time.time() - press_time
            if duration > 0.01:
                print(f'Special Key {key} released after {duration:.2f} seconds')
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
