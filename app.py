from flask import Flask, render_template, request
from assistant_logic import answer_question, summarize_text, generate_creative

app = Flask(__name__)

# Global variable to hold last output before feedback
latest_output = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global latest_output
    ai_output = ""

    if request.method == "POST":
        # If feedback is submitted
        if 'feedback' in request.form:
            user_fb = request.form.get('feedback')
            save_feedback(latest_output, user_fb)
            return render_template("index.html", result="Thank you! Your feedback is saved.", feedback_mode=False)

        # If user submitted text for AI
        user_input = request.form.get("user_input")
        task = request.form.get("task")

        if task == "question":
            ai_output = answer_question(user_input)
        elif task == "summary":
            ai_output = summarize_text(user_input)
        elif task == "creative":
            ai_output = generate_creative(user_input)

        latest_output = ai_output  # store for feedback
        return render_template("index.html", result=ai_output, feedback_mode=True)

    return render_template("index.html", result="", feedback_mode=False)


def save_feedback(output, feedback):
    """Save feedback and AI response to file."""
    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write("AI Response: " + output + "\n")
        f.write("User Feedback: " + feedback + "\n")
        f.write("-" * 40 + "\n")


if __name__ == "__main__":
    app.run(debug=True)
