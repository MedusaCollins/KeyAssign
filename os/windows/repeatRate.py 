import ctypes
from ctypes import wintypes

# Constants from the Windows API
SPI_SETKEYBOARDSPEED = 0x000B
SPI_SETKEYBOARDDELAY = 0x0017
SPI_GETKEYBOARDSPEED = 0x000A
SPI_GETKEYBOARDDELAY = 0x0016

def get_current_keyboard_settings():
    delay = wintypes.UINT()
    speed = wintypes.UINT()
    
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETKEYBOARDDELAY, 0, ctypes.byref(delay), 0)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETKEYBOARDSPEED, 0, ctypes.byref(speed), 0)
    
    return delay.value, speed.value

def set_keyboard_repeat_rate(delay, speed):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETKEYBOARDDELAY, delay, 0, 0)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETKEYBOARDSPEED, speed, 0, 0)

if __name__ == "__main__":
    # Save current keyboard settings
    original_delay, original_speed = get_current_keyboard_settings()
    
    # Set new keyboard settings
    set_keyboard_repeat_rate(3, 0)
    
    print("Keyboard repeat rate and delay have been set.")

    try:
        # Keep the program running to maintain the settings
        input("Press Enter to exit and restore original settings...")
    finally:
        # Restore original keyboard settings
        set_keyboard_repeat_rate(original_delay, original_speed)
        print("\nOriginal keyboard settings restored.")
        exit(0)
