````markdown
# 🤖 AI Text Assistant

A simple AI-powered text assistant built with **Python** and **Google Gemini API**. This project demonstrates the basics of integrating a Large Language Model (LLM) into a Python application. It can answer questions, summarize text, translate content, and explain concepts in simple language.

---

## 🚀 Features

- 💬 Ask any question
- 📝 Summarize text
- 🌍 Translate text
- 📂 Summarize content from a text file
- 📖 Explain concepts in simple language

---

## 📁 Project Structure

```
ai-text-assistant/
│
├── app.py
├── llm.py
├── prompts.py
├── config.py
├── requirements.txt
├── .env
├── README.md
│
├── utils/
│   └── file_reader.py
│
└── notes.txt
```
## 📂 File Summarization

The application can summarize the contents of a text file.

### Example

Choose: 2

Enter filename:

notes.txt

Output:

• Artificial Intelligence simulates human intelligence.
• Machine Learning is a subset of AI.
• Deep Learning uses neural networks.

---

## 🛠️ Tech Stack

- Python 3.x
- Google Gemini API
- google-genai SDK
- python-dotenv

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-text-assistant.git

cd ai-text-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
GEMINI_API_KEY=your_api_key_here
```

You can generate a free API key from **Google AI Studio**.

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 💻 Example

```
========================================
🤖 AI Text Assistant
========================================

You: Explain recursion simply

AI:
Recursion is a programming technique where a function solves a problem by calling itself on a smaller version of the same problem until it reaches a base case.
```

---

## 📚 What You'll Learn

- Working with Large Language Models (LLMs)
- Integrating the Gemini API into Python
- Prompt Engineering
- Environment variable management
- Organizing a Python project

---

## 🔮 Future Improvements

- Chat history (conversation memory)
- PDF summarization
- File upload support
- Voice input/output
- Streamlit web interface
- Tool calling (Calculator, Weather, etc.)
- Retrieval-Augmented Generation (RAG)

---

## 📄 Requirements

```
google-genai
python-dotenv
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome! Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, consider giving it a star!
````
