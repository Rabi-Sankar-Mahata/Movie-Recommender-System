import pickle
import gzip
import streamlit as st

# Recommend top 5 similar movies
def recommend(movie):
    idx = movies[movies.title == movie].index[0]
    sim_scores = sorted(enumerate(similarity[idx]), key=lambda x: x[1], reverse=True)[1:6]
    return [movies.iloc[i].title for i, _ in sim_scores]

# App UI
st.header("🎬 Movie Recommender System")

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# Dropdown for movie selection
movie = st.selectbox("Choose a movie", movies['title'].values)

# Show recommendations
if st.button("Recommend"):
    st.subheader("Top 5 Similar Movies:")
    for title in recommend(movie):
        st.write("🎥", title)
