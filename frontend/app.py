import streamlit as st
import pandas as pd
import requests
from urllib.parse import quote

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .movie-card {
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        border: 1px solid #444;
    }
</style>
""", unsafe_allow_html=True)



# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="CineMind",
    page_icon="🎬",
    layout="centered"
)


# -----------------------------
# Load movie data
# -----------------------------

movies = pd.read_csv("data/clean_movies.csv")

movie_titles = sorted(movies["title"].dropna().unique())


# -----------------------------
# UI
# -----------------------------

st.markdown(
    '<div class="main-title">🎬 CineMind</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Content-Based Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.write(
    "Select a movie and CineMind will recommend "
    "similar movies based on their content."
)

movie = st.selectbox(
    "Choose a movie:",
    movie_titles
)


# -----------------------------
# Get recommendations
# -----------------------------

if st.button("🎯 Recommend Movies"):

    api_url = "http://127.0.0.1:8000/recommend/" + quote(movie)

    response = requests.get(api_url)

    if response.status_code == 200:

        data = response.json()

        st.success(f"Recommendations for {data['movie']}:")

        for item in data["recommendations"]:

            st.write(
                f"🍿 **{item['title']}**  "
                f"— Similarity: {item['similarity']}"
            )

    else:

        st.error("Movie not found.")