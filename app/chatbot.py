import ollama

print("=" * 50)
print("Health Informatics AI Assistant")
print("=" * 50)

user_question = input("\nYou: ")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": user_question
        }
    ]
)

print("\nAssistant:")
print(response["message"]["content"])