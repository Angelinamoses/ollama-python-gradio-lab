from config import AVAILABLE_MODELS
from conversation_memory import messages
from ollama_client import get_response


print("=" * 60)
print("🤖 Health Informatics AI Assistant")
print("=" * 60)
print("Type 'quit' or 'exit' to end the conversation.\n")


# Model Selection
print("Available Models:\n")

for key, value in AVAILABLE_MODELS.items():
    print(f"{key}. {value}")

choice = input("\nSelect model: ").strip()

if choice not in AVAILABLE_MODELS:
    print("\n❌ Invalid selection.")
    exit()

selected_model = AVAILABLE_MODELS[choice]

print(f"\n✅ Using model: {selected_model}")
print("-" * 60)

question_count = 0

# Chat Loop
while True:

    user_question = input("\n👤 You: ").strip()

    if user_question.lower() in ["quit", "exit"]:
        print("\n👋 Goodbye!")
        break
    
    question_count += 1
    
    messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    assistant_reply = get_response(
        messages,
        selected_model
    )

    print("\n🤖 Assistant:")
    print(assistant_reply)

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )
print("=" * 60)
print("Session Summary")
print("=" * 60)

print(f"Model Used      : {selected_model}")
print(f"Questions Asked : {question_count}")
print(f"Total Messages  : {len(messages)}")

