import streamlit as st
from model import get_sentiment

st.title("Sentiment Analysis for Product Ratings")

st.write("Enter a product review below:")

user_input = st.text_area("Your Review")

if st.button("Analyze"):
    if user_input:
        sentiment, rating = get_sentiment(user_input)
        st.write(f"Sentiment: {sentiment}")
        st.write(f"Predicted Rating: {rating}")
    else:
        st.warning("Please enter a review")