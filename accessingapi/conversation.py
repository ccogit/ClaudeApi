from anthropic import Anthropic
from dotenv import load_dotenv

from accessingapi.utils import add_user_message, add_assistant_message, chat

load_dotenv()

client = Anthropic()
MODEL = "claude-sonnet-4-0"

messages = []
answers = []

add_user_message(messages, "Define quantum computing in one sentence")

add_assistant_message(messages, chat(messages))

add_user_message(messages, "Write another sentence")

add_assistant_message(messages, chat(messages))

for message in messages:
    print(message)

    