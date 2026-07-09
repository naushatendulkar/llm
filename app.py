from llm import ask_ai

print("=" * 40)
print("🤖 AI Text Assistant")
print("=" * 40)

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    answer = ask_ai(user)

    print("\nAI:")
    print(answer)