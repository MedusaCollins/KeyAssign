import os
import keyboard

def getText():
    return os.popen('xclip -o -selection primary').read()
def readText():
    selected_text = getText()
    return(selected_text)
