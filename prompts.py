# prompts.py

def question_prompt(question):
    return f"Answer the following factual question clearly and accurately:\n{question}"

def summary_prompt(text):
    return f"Summarize the following text into clear key points:\n{text}"

def creative_prompt(topic):
    return f"Write a creative short story based on the topic:\n{topic}"