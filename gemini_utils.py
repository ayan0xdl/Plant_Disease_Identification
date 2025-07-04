# api/gemini_utils.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_disease(disease_name: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = (
            f"You are a plant disease expert. Explain the plant disease '{disease_name}'.\n"
            "Include the following:\n"
            "- What is this disease?\n"
            "- How to treat/recover the plant?\n"
            "- How to prevent it in the future?\n"
            "Be clear, short, and helpful for farmers or garden owners."
        )

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"
