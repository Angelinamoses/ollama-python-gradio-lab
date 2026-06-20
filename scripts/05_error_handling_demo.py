"""
05_error_handling_demo.py

Purpose:
--------
Demonstrates how to handle exceptions gracefully while interacting
with a local Large Language Model (LLM) using the Ollama Python library.

Concepts Covered:
-----------------
- try-except blocks
- Exception handling
- User input validation
- Conversation memory
- Friendly error messages
"""

import ollama

print("=" * 60)
print("          Ollama Error Handling Demo")
print("=" * 60)
print("Type 'quit' to exit.\n")

# Conversation history
messages = [
    {
        "role": "system",
        "content": (
            "You are a friendly AI tutor. "
            "Explain concepts clearly and professionally."
        )
    }
]

while True:

    # Take user input
    question = input("You: ").strip()

    # Exit condition
    if question.lower() == "quit":
        print("\n👋 Thank you for using the chatbot. Goodbye!")
        break

    # Store user message
    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    try:

        # Send request to Ollama
        response = ollama.chat(
            model="llama3.2",
            messages=messages
        )

        # Extract assistant response
        answer = response["message"]["content"]

        print(f"\nAssistant:\n{answer}\n")

        # Store assistant response for conversation memory
        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:

        error_message = str(e)

        print("\n" + "=" * 60)
        print("❌ ERROR")
        print("=" * 60)

        # Model not found
        if "not found" in error_message.lower():

            print("The requested model could not be found.\n")
            print("Possible Solution:")
            print(" • Run: ollama list")
            print(" • Verify the model name.")
            print(" • Download the model if necessary.")
            print("   Example: ollama pull llama3.2")

        # Server connection problem
        elif "connection" in error_message.lower():

            print("Unable to connect to the Ollama server.\n")
            print("Possible Solution:")
            print(" • Ensure Ollama is running.")
            print(" • Restart the Ollama service.")

        # Any other unexpected error
        else:

            print("An unexpected error occurred.")
            print("\nTechnical Details:")
            print(error_message)

        print("=" * 60)