import streamlit as st
import pandas as pd
import requests
from urllib.parse import quote


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="CineMind",
    page_icon="🎬",
    layout="centered"
)


# -----------------------------
# Custom styling
# -----------------------------

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
</style>
""", unsafe_allow_html=True)


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
    '<div class="subtitle">'
    'Content-Based Movie Recommendation System'
    '</div>',
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

    api_url = (
        "http://127.0.0.1:8000/recommend/"
        + quote(movie)
    )

    try:
        response = requests.get(
            api_url,
            timeout=10
        )

        if response.status_code == 200:

            data = response.json()

            st.success(
                f"Recommendations for {data['movie']}:"
            )

            for item in data["recommendations"]:

                st.write(
                    f"🍿 **{item['title']}** "
                    f"— Similarity: {item['similarity']}"
                )

        elif response.status_code == 404:

            st.error("Movie not found.")

        else:

            st.error("Something went wrong with the API.")

    except requests.exceptions.RequestException:

        st.error(
            "Could not connect to the CineMind API. "
            "Make sure the FastAPI server is running."
        )