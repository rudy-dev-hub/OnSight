import PySimpleGUI as sg

def ask_user_question():
    layout = [[sg.Text("What would you like to ask?")],
              [sg.InputText(key='-QUESTION-')],
              [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Ask About My Screen", layout, modal=True, keep_on_top=True)
    event, values = window.read()
    window.close()

    if event == "Submit":
        return values['-QUESTION-']
    return None

def show_answer(answer: str):
    sg.popup("GPT-4 Answer", answer, keep_on_top=True, modal=True)
