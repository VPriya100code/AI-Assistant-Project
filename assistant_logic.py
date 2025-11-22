import os
from groq import Groq
from prompts import question_prompt, summary_prompt, creative_prompt

# Load API key from environment variable (SAFE for deployment)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Working models (2025)
MODEL = "llama-3.1-8b-instant"   # or "llama-3.1-70b-versatile"

def answer_question(user_text):
    prompt = question_prompt(user_text)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"]


def summarize_text(user_text):
    prompt = summary_prompt(user_text)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"]


def generate_creative(user_text):
    prompt = creative_prompt(user_text)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"]
