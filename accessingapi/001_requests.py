"""Module for making requests to the Anthropic Claude API."""

import logging

from anthropic import Anthropic, APIError
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

client = Anthropic()
MODEL = "claude-sonnet-4-0"


def ask_claude(prompt: str, max_tokens: int = 1000) -> str | None:
    """Send a prompt to Claude and return the response.

    Args:
        prompt: The user prompt to send to Claude.
        max_tokens: Maximum number of tokens in the response.

    Returns:
        The response text from Claude, or None if an error occurred.
    """
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )
        return message.content[0].text
    except APIError as e:
        logger.error("API error: %s", e)
    except Exception as e:
        logger.error("Unexpected error: %s", e)
    return None


if __name__ == "__main__":
    question = "What is quantum computing? Answer in one sentence"
    response = ask_claude(question)
    if response:
        print(response)

    question2 = "Write another sentence"
    response2 = ask_claude(question2)
    if response2:
        print(response2)
