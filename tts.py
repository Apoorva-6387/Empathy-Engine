import pyttsx3

engine = pyttsx3.init()

def generate_voice(text, emotion):

    if emotion == "very_positive":
        engine.setProperty('rate', 200)
        engine.setProperty('volume', 1.0)

    elif emotion == "positive":
        engine.setProperty('rate', 180)
        engine.setProperty('volume', 0.95)

    elif emotion == "neutral":
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)

    elif emotion == "negative":
        engine.setProperty('rate', 130)
        engine.setProperty('volume', 0.85)

    elif emotion == "very_negative":
        engine.setProperty('rate', 110)
        engine.setProperty('volume', 0.8)

    engine.save_to_file(text, "static/output.mp3")
    engine.runAndWait()