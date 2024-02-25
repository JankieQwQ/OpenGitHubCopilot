import openai

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

try:
    with open('openai.key') as f:
        key = f.read().strip()
except FileNotFoundError:
    inputKey = input('Please enter your OpenAI Key:')
    with open('openai.key', 'w') as f:
        f.write(inputKey)
    key = inputKey

with open('prompt.md') as f:
    prompt = f.read() + input('Ask me anything...:')
    
copilot = ChatGPT(key)
print(copilot.ask(prompt))
