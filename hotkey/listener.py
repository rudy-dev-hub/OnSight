# hotkey/listener.py

from pynput import keyboard

def start_hotkey_listener(callback):
    def on_activate():
        print("Hotkey triggered!")
        callback()

    hotkey = keyboard.GlobalHotKeys({
        '<ctrl>+<shift>+a': on_activate
    })
    hotkey.start()
