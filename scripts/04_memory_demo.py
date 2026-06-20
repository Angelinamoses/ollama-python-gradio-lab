import ollama

messages = [
    {
        "role": "system",
        "content": "You are a helpful Python tutor."
    }
]

while True:
    question = input("You: ").strip()

    if question.lower() == "quit":
        break

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    answer = response["message"]["content"]

    print(f"\nAssistant: {answer}\n")

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )