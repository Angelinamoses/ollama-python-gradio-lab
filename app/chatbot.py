import ollama

# Conversation Memory
messages = []

print("=" * 60)
print("🤖 Health Informatics AI Assistant")
print("=" * 60)
print("Type 'quit' or 'exit' to end the conversation.\n")

while True:

    user_question = input("👤 You: ")

    # Exit Condition
    if user_question.lower() in ["quit", "exit"]:
        print("\n👋 Goodbye!")
        break

    # Store User Message
    messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # Send Conversation History to Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    assistant_reply = response["message"]["content"]

    print("\n🤖 Assistant:")
    print(assistant_reply)

    # Store Assistant Response
    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

print()