import ollama
from config import MODEL_NAME


def get_response(messages):

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages
    )

    return response["message"]["content"]