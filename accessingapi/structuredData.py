import json

from accessingapi.utils import add_user_message, add_assistant_message, client

messages = []
MODEL = "claude-haiku-4-5"


def chat(messages, stop_sequences=None):
    message = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        messages=messages,
        stop_sequences=stop_sequences
    )
    return message.content[0].text


add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])
clean_json = json.loads(text.strip())
print(clean_json)
