import ollama

print("=" * 60)
print("USING generate()")
print("=" * 60)

generate_response = ollama.generate(
    model="llama3.2",
    prompt="What is Machine Learning?"
)

print(generate_response["response"])

print("\n")

print("=" * 60)
print("USING chat()")
print("=" * 60)

chat_response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "What is Machine Learning?"
        }
    ]
)

print(chat_response["message"]["content"])