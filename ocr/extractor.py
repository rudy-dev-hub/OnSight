# ocr/extractor.py

import easyocr
import numpy as np

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image):
    """
    Accepts a PIL Image object.
    Returns extracted visible text as a single string.
    """
    img_array = np.array(image)
    result = reader.readtext(img_array)
    text_blocks = [entry[1] for entry in result]
    return "\n".join(text_blocks)
