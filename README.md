# 🎬 CineMind
### Intelligent Movie Discovery & Recommendation Platform

CineMind is an AI-powered movie recommendation platform that helps users discover movies based on their interests and preferences.

The project uses machine learning, natural language processing (NLP), and content-based filtering to recommend similar movies.

## 🚀 Features

- Content-based movie recommendation system
- Movie similarity calculation using NLP techniques
- Personalized movie discovery
- Movie dataset processing and feature engineering
- FastAPI backend for recommendation services
- Streamlit frontend for user interaction

## 🧠 How It Works

1. Movie data is collected from the TMDB 5000 dataset.
2. Data is cleaned and preprocessed.
3. Movie features such as genres, keywords, overview, cast, and director are combined.
4. Text features are transformed using CountVectorizer.
5. Cosine similarity is used to identify similar movies.
6. The recommendation engine returns movies similar to the selected title.

## 🏗️ Project Architecture

Dataset → Data Cleaning → Feature Engineering → Text Vectorization → Cosine Similarity → Recommendation Engine → FastAPI Backend → Streamlit Frontend

## 🛠️ Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **NLP:** CountVectorizer
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Tools:** Git, GitHub

## 📂 Project Structure

```text
CineMind/
├── backend/
├── data/
├── frontend/
├── notebooks/
├── src/
├── requirements.txt
└── README.md
```

## 💡 What I Learned

- Building a content-based recommendation system
- Applying NLP techniques to movie metadata
- Feature engineering for machine learning
- Computing similarity between movies
- Developing APIs using FastAPI
- Integrating a machine learning model with a frontend

## 👩‍💻 Author

**Sonal Kumari**

- GitHub: [@gsonal06](https://github.com/gsonal06)
- LinkedIn: [Sonal Kumari](https://www.linkedin.com/in/sonal-kumari-8a5761357/)
