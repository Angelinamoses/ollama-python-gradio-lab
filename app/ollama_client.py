import ollama
from config import AVAILABLE_MODELS


def get_response(messages, model_name):

    response = ollama.chat(
        model=model_name,
        messages=messages,
        stream=True
    )

    for chunk in response:
     yield chunk["message"]["content"]