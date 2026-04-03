from accessingapi.utils import add_user_message, client, add_assistant_message

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


prompt = """
Generate three different sample AWS CLI commands. Each should be very short.
"""

add_user_message(messages, prompt)

add_assistant_message(messages, "Here are all three commands in a single block without any comments:\n```bash")

print(chat(messages, stop_sequences=["```"]))
