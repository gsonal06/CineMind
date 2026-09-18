from fastapi import FastAPI, HTTPException
from src.recommender import recommend

app = FastAPI()


@app.get("/recommend/{movie_title}")
def get_recommendations(movie_title: str):
    recommendations = recommend(movie_title)

    if not recommendations:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    return {
        "movie": movie_title,
        "recommendations": recommendations
    }