# AI Assistant — Flask + Groq (LLaMA 3)🚀🚀✨✨✨

A simple, lightweight AI chatbot built with Flask and the Groq LLaMA models. This project demonstrates how to integrate an LLM API into a small web app, design prompts, and build a minimal feedback loop.

## Features🚀🚀✨✨

- Ask questions and get AI-powered responses
- Uses Groq's fast LLaMA models
- Clean Flask UI with background & favicon
- Feedback system (yes/no saved to feedback.txt)
- Secure-by-design: API key is NOT stored in the repository

## Project structure

AIASSISTANT/
├── app.py  
├── assistant_logic.py        (NOT included in GitHub — contains API key)  
├── prompts.py  
├── requirements.txt  
├── feedback.txt              (ignored by Git)  
├── static/  
│   ├── bg.png  
│   └── favicon.png  
└── templates/  
    └── index.html  
└── .gitignore

## Installation & Setup🔥🔥🔥🔥🔥🔥🔥

1. Clone the repository
   ```
   git clone https://github.com/YOUR_USERNAME/AIASSISTANT.git
   cd AIASSISTANT
   ```

2. Create a virtual environment (recommended)
   ```
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Create assistant_logic.py

   assistant_logic.py is intentionally excluded from the repository to protect your API key. Create it manually in the project folder. Example:

   ```python
   from groq import Groq

   client = Groq(api_key="YOUR_API_KEY_HERE")

   def answer_question(user_input):
       response = client.chat.completions.create(
           messages=[{"role": "user", "content": user_input}],
           model="llama-3.2-1b-preview"
       )
       return response.choices[0].message["content"]
   ```

   Replace `"YOUR_API_KEY_HERE"` with your Groq API key.

   Optional — use environment variables instead:
   ```python
   import os
   from groq import Groq

   client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

   def answer_question(user_input):
       response = client.chat.completions.create(
           messages=[{"role": "user", "content": user_input}],
           model="llama-3.2-1b-preview"
       )
       return response.choices[0].message["content"]
   ```

## Run the project

Start the Flask app:
```
python app.py
```

Open the app in your browser:
http://127.0.0.1:5000/

## Feedback system

After each AI response the UI asks:
Was this helpful? (yes / no)

Responses are appended to `feedback.txt` (this file is ignored by Git to avoid storing user data in the repo).

## Security notes

- assistant_logic.py is intentionally excluded using `.gitignore` — do not commit your API keys.
- Prefer storing secrets in environment variables or a secrets manager.
- Do NOT publish your Groq API key in public repos.

## Requirements

- Python 3.8+
- Packages in requirements.txt (example)
  - flask
  - groq

Install them with:
```
pip install -r requirements.txt
```

## Customization & Extensions

- Replace the LLM model or tweak prompts in `prompts.py`.
- Add authentication if exposing to the public internet.
- Expand feedback handling (store in a DB, add analytics).
- Add UI/UX improvements and screenshots in this README.

## Author

Priyadharshini V  
B.E CSE
