import pyautogui

def take_screenshot(save_path=None):
    """
    Takes a screenshot and returns the image object.
    If save_path is provided, saves the image to that path.
    """
    image = pyautogui.screenshot()
    if save_path:
        image.save(save_path)
    return image
