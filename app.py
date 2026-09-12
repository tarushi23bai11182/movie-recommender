import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

@st.cache_data
def load_data():
    df = pd.read_csv("movielens_100k.csv")
    df["genres"] = df["genres"].fillna("")
    df["genres_clean"] = df["genres"].str.replace("|", " ", regex=False)
    return df

@st.cache_data
def compute_similarity(df):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["genres_clean"])
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

df = load_data()
cosine_sim = compute_similarity(df)

def get_recommendations(title, df, cosine_sim, top_n=5):
    try:
        idx = df[df["title"] == title].index[0]
    except IndexError:
        return pd.DataFrame()

    sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df.iloc[movie_indices][["title", "genres"]]

st.title("🎬 Movie Recommendation Engine")
st.write("Select a movie you like to get 5 similar suggestions!")

selected_movie = st.selectbox("Select a movie:", options=df["title"].values)

if st.button("Get Recommendations"):
    recommendations = get_recommendations(selected_movie, df, cosine_sim, top_n=5)
    st.subheader(f"Recommended for fans of **{selected_movie}**:")
    for _, row in recommendations.iterrows():
        st.markdown(f"👉 **{row['title']}** *(Genres: {row['genres']})*")