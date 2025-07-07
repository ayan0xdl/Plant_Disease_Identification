import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_disease(query: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        # You can still lightly guide Gemini while keeping it open-ended
        prompt = (
            f"You are a helpful plant disease expert chatbot named BotaniQ. "
            f"A user has asked: \"{query}\".\n"
            "Give clear, short, accurate responses suitable for farmers or gardeners.\n"
            "If the question relates to a plant disease, cover the cause, treatment, and prevention."
        )

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"
