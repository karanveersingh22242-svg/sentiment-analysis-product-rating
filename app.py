import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import get_sentiment, load_data

st.set_page_config(page_title="Sentiment Analysis for Product Ratings", layout="wide")

st.title("Sentiment Analysis for Product Ratings")
st.caption("A simple NLP-based system to understand customer feedback")

st.sidebar.title("Navigation")
option = st.sidebar.radio("Choose", ["Home","Analyze","Dashboard"])

df = load_data()
df["Sentiment"] = df["review_text"].apply(lambda x: get_sentiment(x)[0])

if option == "Home":
    st.subheader("Overview")
    st.write("This project analyses customer reviews and predicts sentiment.")

elif option == "Analyze":
    st.subheader("Check Review")
    user_input = st.text_area("Enter review")

    if st.button("Check Review"):
        if user_input:
            sentiment, rating = get_sentiment(user_input)
            st.write("Sentiment:", sentiment)
            st.write("Predicted Rating:", rating)

elif option == "Dashboard":
    st.subheader("Insights")
    fig, ax = plt.subplots()
    df["Sentiment"].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)
