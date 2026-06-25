import ollama
from config import AVAILABLE_MODELS


def get_response(messages, model_name):

    response = ollama.chat(
        model=model_name,
        messages=messages
    )

    return response["message"]["content"]