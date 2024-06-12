import json
import os
import time
import keyboard
import subprocess

config_file_path = os.path.join(os.path.dirname(__file__), '../../config.json')

with open(config_file_path, 'r') as f:
    config = json.load(f)

def process_key_events(queue):
    while True:
        event = queue.get()
        if event:
            key, action, timestamp_or_duration = event
            if action == 'pressed':
                print(f"Key {key} pressed.")
            elif action == 'released':
                if key in config:
                    item = config[key]
                    if item['durationStart'] <= timestamp_or_duration <= item['durationEnd']:
                        if item['outputType'] == 'text':
                            typing_delay = item.get('typingDelay', 0.1)
                            for char in item['outputValue']:
                                keyboard.press(char)
                                time.sleep(typing_delay)
                                keyboard.release(char)
                        elif item['outputType'] == 'script':
                            script_path = item.get('import')
                            if script_path:
                                subprocess.run(['node', f"imports/{script_path}"])
