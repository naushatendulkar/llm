from llm import ask_ai

while True:
    print("\n====== AI Assistant ======")
    print("1. Ask Question")
    print("2. Summarize")
    print("3. Translate")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        text = input("Question: ")
        print(ask_ai(text))

    elif choice == "2":
        text = input("Paste text:\n")
        print(ask_ai(f"Summarize this:\n\n{text}"))

    elif choice == "3":
        text = input("Enter text:\n")
        language = input("Translate to: ")
        print(ask_ai(f"Translate this into {language}:\n\n{text}"))

    elif choice == "4":
        break

    else:
        print("Invalid choice")