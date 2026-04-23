import pandas as pd
from textblob import TextBlob

def load_data():
    return pd.read_csv("reviews.csv")

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "Positive", 5
    elif polarity < -0.2:
        return "Negative", 1
    else:
        return "Neutral", 3
