# 🧠 OnSight – Your AI-Powered Contextual Desktop Assistant

**OnSight** is a smart, always-available desktop assistant that helps you interact with your screen using natural language. Just press a hotkey, ask a question, and get a relevant response from **GPT-4**. It’s like having a contextual AI co-pilot for anything you’re viewing on your desktop.

---

## 🎥 Demo

https://github.com/your-username/OnSight/blob/main/demo/onsight-demo.mp4

> 📁 The video is in the `demo/` folder — feel free to check it out!

---

## ✨ Key Features

- 🖼️ Captures your screen automatically
- ⌨️ Global hotkey enabled (default: `Ctrl+Shift+A`)
- 🧠 Sends your question + screenshot context to **GPT-4**
- 💬 Displays answers instantly in a popup
- 🪟 Lightweight UI built using PySimpleGUI
- 🧵 Runs hotkey listener in a background thread

---

## 🧠 How the AI Works

Here’s what happens under the hood when you press the hotkey:

1. **Hotkey trigger:** Captured by a listener using `pynput`.
2. **Screenshot:** A snapshot of your current screen is taken using `pyautogui` and `Pillow`.
3. **User input:** A popup asks you what you want to know.
4. **Prompt creation:** Your question and screen context are combined into a GPT-4-friendly prompt.
5. **GPT-4 response:** OpenAI API returns an answer relevant to your screen and question.
6. **Popup display:** The result is shown in a simple modal window.

---

## 🗂️ Project Structure

OnSight/
├── main.py              
├── ui/
│   └── popup.py         
├── utils/
│   ├── hotkey.py         # Background hotkey listener logic
│   ├── image_utils.py    # Functions to capture and save screenshots
│   └── ai_utils.py       # Prompt generation and GPT-4 API handling
├── demo/
│   └── onsight-demo.mp4  # Screen recording of how OnSight works/ or maybe screenshots
├── .env                  # Contains your OpenAI API key (excluded from Git)
├── .gitignore
├── requirements.txt
└── README.md

---

## 🛠️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/OnSight.git
cd OnSight
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set your OpenAI API key**

Create a `.env` file in the root directory:
```ini
OPENAI_API_KEY=your_openai_key_here
```

5. **Run the app**
```bash
python3 main.py
```

---

## 🙌 Built By

**Rudresh Upadhyaya** – built with ❤️

---