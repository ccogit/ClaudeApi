from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()
MODEL = "claude-sonnet-4-0"

messages = []
answers = []

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

add_user_message(messages, "Define quantum computing in one sentence")

add_assistant_message(messages, chat(messages))

add_user_message(messages, "Write another sentence")

add_assistant_message(messages, chat(messages))

for message in messages:
    print(message)

    