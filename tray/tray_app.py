# tray/tray_app.py

import threading
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item
from core.flow import main_flow  # Now we import from here

def create_icon():
    image = Image.new("RGB", (64, 64), color="white")
    d = ImageDraw.Draw(image)
    d.text((10, 25), "👁", fill="black")

    def on_quit(icon, item):
        icon.stop()

    def on_ask(icon, item):
        threading.Thread(target=main_flow).start()

    icon = pystray.Icon("onsight")
    icon.icon = image
    icon.menu = (
        item("Ask a Question", on_ask),
        item("Quit", on_quit)
    )

    icon.run()
