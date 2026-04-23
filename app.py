import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import get_sentiment, load_data

# Page config
st.set_page_config(page_title="Product Review Analysis", layout="wide")

# Header (simple, human style)
st.title("Product Review Sentiment Analysis")
st.caption("A small project to analyse customer reviews using basic NLP")

# Sidebar (clean & minimal)
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Analyse Review", "Insights"])

# Load data
df = load_data()
df["Sentiment"] = df["review_text"].apply(lambda x: get_sentiment(x)[0])

# ---------------- HOME ----------------
if page == "Home":
    st.subheader("Overview")

    st.write("This project focuses on analysing product reviews and identifying whether the sentiment is positive, negative or neutral.")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Reviews", len(df))
    col2.metric("Positive %", f"{(df['Sentiment'].value_counts(normalize=True).get('Positive',0)*100):.1f}%")
    col3.metric("Negative %", f"{(df['Sentiment'].value_counts(normalize=True).get('Negative',0)*100):.1f}%")

# ---------------- ANALYSE ----------------
elif page == "Analyse Review":
    st.subheader("Check a Review")

    user_input = st.text_area("Enter review text")

    if st.button("Check Review"):
        if user_input:
            sentiment, rating = get_sentiment(user_input)

            st.write("Sentiment:", sentiment)
            st.write("Predicted Rating:", f"{rating}/5")

            if sentiment == "Positive":
                st.success("Looks like the customer had a good experience.")
            elif sentiment == "Negative":
                st.error("The review indicates dissatisfaction.")
            else:
                st.info("This seems like a neutral or mixed review.")
        else:
            st.warning("Please enter some text")

# ---------------- INSIGHTS ----------------
elif page == "Insights":
    st.subheader("Basic Insights")

    col1, col2 = st.columns(2)

    # Bar chart
    with col1:
        st.write("Sentiment Distribution")
        fig, ax = plt.subplots()
        df["Sentiment"].value_counts().plot(kind='bar', ax=ax)
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Count")
        st.pyplot(fig)

    # Pie chart
    with col2:
        st.write("Sentiment Share")
        fig2, ax2 = plt.subplots()
        df["Sentiment"].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax2)
        st.pyplot(fig2)

    st.write("Sample Data")
    st.dataframe(df.sample(10))

# Footer
st.markdown("---")
st.caption("Developed as part of a basic NLP project")