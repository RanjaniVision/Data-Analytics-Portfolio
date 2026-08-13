from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("gemini_apikey")
print("API key loaded:", bool(api_key))

if not api_key:
    raise ValueError("GEMINI API key not found. Check your .env file.")

client = genai.Client(api_key=api_key)


def generate_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    return response.text