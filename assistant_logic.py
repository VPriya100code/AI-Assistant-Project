import os
from groq import Groq
from prompts import question_prompt, summary_prompt, creative_prompt

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def answer_question(user_input):
    prompt = question_prompt(user_input)   # <-- FIXED
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def summarize_text(user_input):
    prompt = summary_prompt(user_input)    # <-- FIXED
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def generate_creative(user_input):
    prompt = creative_prompt(user_input)   # <-- FIXED
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
