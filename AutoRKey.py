from pynput import keyboard
from pynput.keyboard import Controller

kbd = Controller()

mapping = {
    "oo": "ö",
    "ae": "ä",
    "ue": "ü"
}

buffer = ""

def on_press(key):
    global buffer

    try:
        char = key.char
    except:
        return

    buffer += char

    for trigger, replacement in mapping.items():
        if buffer.endswith(trigger):
            # clear the trigger and print the result
            for _ in trigger:
                kbd.press(keyboard.Key.backspace)
                kbd.release(keyboard.Key.backspace)
            for c in replacement:
                kbd.press(c)
                kbd.release(c)

def on_release(key):
    pass

# create a listener and call join on it
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
