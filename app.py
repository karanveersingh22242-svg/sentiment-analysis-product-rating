import streamlit as st
import pandas as pd
from model import load_data, get_sentiment

# Page config
st.set_page_config(page_title="Sentiment Analysis", page_icon="📊", layout="wide")

# Custom CSS
st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:700;
    color:#4CAF50;
}
.card {
    background-color:#1e1e1e;
    padding:20px;
    border-radius:10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="big-title">📊 Product Review Sentiment Analysis</p>', unsafe_allow_html=True)
st.write("Analyze customer reviews using NLP (TextBlob)")

# Load data
df = load_data()

# Metrics
total = len(df)
pos = len(df[df['sentiment'] ==