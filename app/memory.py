"""
Memory management for Clinical Learning Assistant.

This module is responsible for creating and maintaining
conversation history for the chatbot.
"""

def create_memory(system_prompt: str) -> list:
    
        return [
        {
            "role": "system",
            "content": system_prompt,
        }
    ]

def add_user_message(memory: list, message: str) -> None:
    """
    Add a user message to the conversation history.
    """

    memory.append(
        {
            "role": "user",
            "content": message,
        }
    )