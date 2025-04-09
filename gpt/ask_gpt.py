# gpt/ask_gpt.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(screen_text: str, question: str) -> str:
    prompt = (
        f"You are an assistant watching a user's screen. "
        f"Here is the text currently visible:\n\n{screen_text}\n\n"
        f"User asks: {question}\n\n"
        f"Answer using only what’s visible on the screen."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You answer questions based on visible screen content."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
