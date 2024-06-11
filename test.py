from pynput import keyboard
import speacialKey


with keyboard.Listener(on_press=speacialKey.on_press, on_release=speacialKey.on_release) as listener:
    listener.join()
