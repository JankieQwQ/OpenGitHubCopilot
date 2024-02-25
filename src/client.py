import openai
import tkinter as tk

class ChatGPT:
    def __init__(self, key):
        openai.api_key = key

    def ask(self, prompt: str) -> str:
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        return message

def on_ask_clicked():
    prompt = default_prompt + prompt_text.get("1.0", tk.END).strip()
    response = copilot.ask(prompt)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, response)

try:
    with open('openai.key') as f:
        key = f.read().strip()
except FileNotFoundError:
    inputKey = input('Please enter your OpenAI Key:')
    with open('openai.key', 'w') as f:
        f.write(inputKey)
    key = inputKey

with open('prompt.md') as f:
    default_prompt = f.read()

copilot = ChatGPT(key)

window = tk.Tk()
window.title("Copilot Mini")

prompt_label = tk.Label(window, text="Enter your prompt:")
prompt_label.pack()

prompt_text = tk.Text(window, height=4, width=50)
prompt_text.insert(tk.END, default_prompt)
prompt_text.pack()

ask_button = tk.Button(window, text="Ask", command=on_ask_clicked)
ask_button.pack()

result_label = tk.Label(window, text="Response:")
result_label.pack()

result_text = tk.Text(window, height=6, width=50)
result_text.pack()

window.mainloop()
