from google import genai
from config import API_KEY, MODEL
from prompts import SYSTEM_PROMPT

client = genai.Client(api_key=API_KEY)


def ask_ai(user_input):
    response = client.models.generate_content(
        model=MODEL,
        contents=f"{SYSTEM_PROMPT}\n\nUser: {user_input}"
    )

    return response.text