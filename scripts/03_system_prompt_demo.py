import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a Comedian"
                "Explain every answer simply with one hilarious example healthcare example."
            )
        },
        {
            "role": "user",
            "content": "What is digital twins"
        }
    ]
)

print(response["message"]["content"])