from pynput import keyboard
import time

# Set to keep track of pressed keys and their press times
keys_pressed = {}
press_times = {}

def on_press(key):
    try:
        if key.char not in keys_pressed:
            keys_pressed[key.char] = time.time()
            print(f'Key {key.char} pressed')
    except AttributeError:
        if key not in keys_pressed:
            keys_pressed[key] = time.time()
            print(f'Special Key {key} pressed')

def on_release(key):
    try:
        if key.char in keys_pressed:
            press_time = keys_pressed.pop(key.char)
            duration = time.time() - press_time
            print(f'Key {key.char} released after {duration:.2f} seconds')
    except AttributeError:
        if key in keys_pressed:
            press_time = keys_pressed.pop(key)
            duration = time.time() - press_time
            print(f'Special Key {key} released after {duration:.2f} seconds')

