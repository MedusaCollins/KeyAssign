import json
import time
import keyboard
from collections import deque

pressTimes = {}
key_states = {}
key_order = deque()

def read_config(keypress, duration):
    try:
        with open('config.json') as file:
            config = json.load(file)
            for key, value in config.items():
                if key == keypress and float(duration) >= float(value["durationStart"]) and float(duration) <= float(value["durationEnd"]):
                    if value.get("outputType") == "text":
                        keyboard.write(value["outputValue"])
    except FileNotFoundError:
        print("config.json file not found.")
    except json.JSONDecodeError:
        print("Error decoding config.json.")
def on_action(event):
    if event.event_type == keyboard.KEY_DOWN:
        on_press(event.name)
    elif event.event_type == keyboard.KEY_UP:
        on_release(event.name)

def on_press(key):
    global pressTimes, key_states, key_order
    if key not in key_states or not key_states[key]:

        key_states[key] = True
        key_order.append(key)
        pressTimes[key] = time.time()
        if is_special_key(key):
            print(f"Special key pressed: {key}")
        else:
            print(f"Pressed:  {key}")

def on_release(key):
    global pressTimes, key_states
    if key in pressTimes:
        releaseTime = time.time()
        duration = releaseTime - pressTimes[key]
        read_config(key, duration.__format__(".2f"))
        if is_special_key(key):
            print(f"Special key released: {key}, duration: {duration:.2f}")
        else:
            print(f"Released: {key}, duration: {duration:.2f}")
        del pressTimes[key]
    key_states[key] = False

def is_special_key(key):
    # List of special keys
    special_keys = ["shift", "ctrl", "alt", "space", "enter", "tab", "backspace", 
                    "caps lock", "esc", "page up", "page down", "home", "end", 
                    "insert", "delete", "up", "down", "left", "right", 
                    "num lock", "scroll lock", "pause", "print screen"]
    
    return key in special_keys

# Start listening to keyboard events
keyboard.hook(lambda e: on_action(e))

print("Press ESC to stop.")

if __name__ == "__main__":
    print("hello world")