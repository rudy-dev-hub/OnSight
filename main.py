# main.py
import threading
from tray.tray_app import create_icon
from hotkey.listener import start_hotkey_listener
from core.flow import main_flow
import PySimpleGUI as sg

from ui.popup import ask_user_question, show_answer

popup_event = threading.Event()

def trigger_main_flow():
    popup_event.set()

def main_loop():
    sg.theme("SystemDefault")
    window = sg.Window("OnSight", [[sg.Text("Running in tray...")]], finalize=True, keep_on_top=False)

    while True:
        event, values = window.read(timeout=100)
        if popup_event.is_set():
            popup_event.clear()
            question = ask_user_question()
            if question:
                answer = main_flow(question)
                show_answer(answer)

        if event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    # Start hotkey listener in background
    hotkey_thread = threading.Thread(target=start_hotkey_listener, args=(trigger_main_flow,), daemon=True)
    hotkey_thread.start()

    # Run GUI main loop on main thread
    main_loop()

    # Optional: start tray icon in background if it's not blocking
    create_icon()
