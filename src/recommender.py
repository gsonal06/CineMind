import pandas as pd
import pickle
from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load movie data
movies = pd.read_csv(
    BASE_DIR / "data" / "clean_movies.csv"
)

# Load vectorizer
with open(BASE_DIR / "data" / "vectorizer.pkl", "rb") as file:
    _vectorizer = pickle.load(file)

# Load similarity matrix
with open(BASE_DIR / "data" / "similarity.pkl", "rb") as file:
    similarity = pickle.load(file)


def recommend(movie_title):
    movie_matches = movies[
        movies["title"].str.lower() == movie_title.lower()
    ]

    if movie_matches.empty:
        return []

    movie_index = movie_matches.index[0]

    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    top_movies = similarity_scores[1:6]

    recommendations = []

    for index, score in top_movies:
        recommendations.append({
            "title": movies.iloc[index]["title"],
            "similarity": round(float(score), 3)
        })

    return recommendations