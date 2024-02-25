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

class ChatGPTApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Copilot Mini")

        self.default_prompt = ""
        with open('prompt.md') as f:
            self.default_prompt = f.read()

        self.copilot = ChatGPT(self.load_api_key())

        self.create_widgets()

    def load_api_key(self):
        try:
            with open('openai.key') as f:
                return f.read().strip()
        except FileNotFoundError:
            inputKey = input('Please enter your OpenAI Key:')
            with open('openai.key', 'w') as f:
                f.write(inputKey)
            return inputKey

    def create_widgets(self):
        self.prompt_label = tk.Label(self.master, text="Enter your prompt:")
        self.prompt_label.pack()

        self.prompt_text = tk.Text(self.master, height=4, width=50)
        self.prompt_text.insert(tk.END, 'Ask me anything...')
        self.prompt_text.pack()

        self.ask_button = tk.Button(self.master, text="Ask", command=self.on_ask_clicked)
        self.ask_button.pack()

        self.result_label = tk.Label(self.master, text="Response:")
        self.result_label.pack()

        self.result_text = tk.Text(self.master, height=6, width=50)
        self.result_text.pack()

    def on_ask_clicked(self):
        prompt = self.default_prompt + self.prompt_text.get("1.0", tk.END).strip()
        response = self.copilot.ask(prompt)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, response)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGPTApp(root)
    root.mainloop()
