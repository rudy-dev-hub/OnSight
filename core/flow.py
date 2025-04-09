# core/flow.py

from utils.screenshot import take_screenshot
from ocr.extractor import extract_text_from_image
from ui.popup import ask_user_question, show_answer
from gpt.ask_gpt import ask_gpt

def main_flow(question):
    image = take_screenshot("latest_screenshot.png")
    screen_text = extract_text_from_image(image)
    question = ask_user_question()
    if question:
        response = ask_gpt(screen_text, question)
        show_answer(response)

    return f"You asked: {question}"