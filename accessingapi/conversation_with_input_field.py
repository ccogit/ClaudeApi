from accessingapi.utils import chat, add_assistant_message, add_user_message

messages = []

while True:
    user_input = input("> ")
    add_user_message(messages, user_input)
    add_assistant_message(messages, chat(messages))
    print(messages[-1]["content"])
