from accessingapi.utils import add_assistant_message, add_user_message, client, MODEL

messages = []

def chat(messages, system=None):
    params = {
        "model": MODEL,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system:
        params["system"] = system
    message = client.messages.create(**params)
    return message.content[0].text


system_prompt = """
Whenever you write a Python code snippet, make sure it is as concise as possible and easy to understand.
"""

user_input = "Write a Python function that checks a string for duplicate characters"

add_user_message(messages, user_input)
add_assistant_message(messages, chat(
    messages,
    system_prompt
))
print(messages[-1]["content"])
