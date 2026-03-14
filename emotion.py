from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):

    score = analyzer.polarity_scores(text)
    compound = score["compound"]

    if compound >= 0.5:
        return "very_positive"

    elif compound > 0.1:
        return "positive"

    elif compound <= -0.5:
        return "very_negative"

    elif compound < -0.1:
        return "negative"

    else:
        return "neutral"