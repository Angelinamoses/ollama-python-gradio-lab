import ollama

print("=" * 60)
print("🤖 Health Informatics AI Assistant")
print("=" * 60)
print("Type your question below.")
print("You have 3 questions in this demo.\n")

for chat_number in range(1, 6):

    print("-" * 60)
    print(f"Conversation {chat_number}/3")

    user_question = input("\n👤 You: ")

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": user_question
            }
        ]
    )

    print("\n🤖 Assistant:")
    print(response["message"]["content"])
    print()

print("=" * 60)
print("Session Finished 👋")
print("=" * 60)