import ollama


print("=" * 60)
print("My First Ollama Program")
print("=" * 60)

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Hello! Introduce yourself in two sentences."
        }
    ]
)

print("\nAI Response:\n")
print(response["message"]["content"])

print("\n" + "=" * 60)
print("FULL RESPONSE OBJECT")
print("=" * 60)

print(response)