from flask import Flask, render_template, request
from emotion import detect_emotion
from tts import generate_voice

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    emotion = None

    if request.method == "POST":
        text = request.form["text"]

        emotion = detect_emotion(text)

        generate_voice(text, emotion)

    return render_template("index.html", emotion=emotion)

if __name__ == "__main__":
    app.run(debug=True)