from accessingapi.utils import add_user_message, client

messages = []
MODEL = "claude-haiku-4-5"

add_user_message(messages, "Write a 1 sentence description of a fake database")

with (client.messages.stream(model=MODEL,
                             max_tokens=1000,
                             messages=messages,
                             ) as stream):
    for text in stream.text_stream:
        print(text, end="")

# print(stream.get_final_message())
