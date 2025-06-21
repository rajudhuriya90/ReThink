from flask import Flask, render_template, request
from transformers import pipeline
import random

app = Flask(__name__)

# Load local model
generator = pipeline("text-generation", model="distilgpt2")

# Data
songs = [
    {"title": "Fight Song", "link": "https://youtu.be/xo1VInw-SKc"},
    {"title": "Believer – Imagine Dragons", "link": "https://youtu.be/7wtfhZwyrcc"},
    {"title": "Stronger – Kanye West", "link": "https://youtu.be/PsO6ZnUZI0g"},
    {"title": "Hall of Fame – The Script", "link": "https://youtu.be/mk48xRzuNvA"},
]

quotes = [
    "“You have power over your mind – not outside events.” – Marcus Aurelius",
    "“Start where you are. Use what you have. Do what you can.” – Arthur Ashe",
    "“You don't have to control your thoughts. You just have to stop letting them control you.” – Dan Millman",
]

tips = [
    "Take a walk outside and breathe deeply.",
    "Write down 3 things you're grateful for.",
    "Drink a glass of water and relax your shoulders.",
    "Text or call someone you trust.",
]

@app.route("/", methods=["GET", "POST"])
def index():
    reframed_text = None
    song = tip = quote = None

    if request.method == "POST":
        user_input = request.form["thought"]
        prompt = f"Reframe this thought positively: {user_input}"
        result = generator(prompt, max_length=50, num_return_sequences=1)
        reframed_text = result[0]["generated_text"].replace(prompt, "").strip()

        song = random.choice(songs)
        tip = random.choice(tips)
        quote = random.choice(quotes)

    return render_template("index.html", reframed=reframed_text, song=song, tip=tip, quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
