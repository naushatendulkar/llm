from llm import ask_ai
from prompts import SUMMARY_PROMPT
from utils.file_reader import read_text_file

while True:

    print("\n====== AI Assistant ======")
    print("1. Ask Question")
    print("2. Summarize Text File")
    print("3. Translate")
    print("4. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        question = input("\nQuestion: ")
        print("\nAI:")
        print(ask_ai(question))

    elif choice == "2":

        filename = input("\nEnter filename: ")

        text = read_text_file(filename)

        if text is None:
            print("File not found.")
            continue

        prompt = f"{SUMMARY_PROMPT}\n\n{text}"

        print("\nGenerating summary...\n")

        print(ask_ai(prompt))

    elif choice == "3":

        text = input("Enter text: ")
        language = input("Translate to: ")

        prompt = f"Translate the following text into {language}:\n\n{text}"

        print(ask_ai(prompt))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")