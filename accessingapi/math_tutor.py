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
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

while True:
    user_input = input("> ")
    add_user_message(messages, user_input)
    add_assistant_message(messages, chat(
        messages,
        system_prompt
    ))
    print(messages[-1]["content"])
