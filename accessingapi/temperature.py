from accessingapi.utils import add_assistant_message, add_user_message, client

messages = []
MODEL = "claude-haiku-4-5"

def chat(messages, temperature=None):
    params = {
        "model": MODEL,
        "max_tokens": 1000,
        "messages": messages,
    }

    if temperature:
        params["temperature"] = temperature
    message = client.messages.create(**params)
    return message.content[0].text

user_input = "Tell me a joke that only has two sentences"
for i in range(3):
    add_user_message(messages, user_input)
    add_assistant_message(messages, chat(
        messages,
        temperature=i * 0.3
    ))
    print(messages[-1]["content"])