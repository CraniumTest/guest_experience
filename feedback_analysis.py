from textblob import TextBlob

def analyze_feedback(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity >= 0:
        return "Positive"
    else:
        return "Negative"
