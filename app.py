import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e2d359148c85e30f533dea9162802ae7&language=en-US".format(
        movie_id)
    data = requests.get(url)

    #api_key=e2d359148c85e30f533dea9162802ae7
    data = data.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_posters = []
    recommended_movies = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id #this is movie_id
        #fetch movie through api
        recommended_movies.append(movies.iloc[i[0]].title)  #here title is fetched through index
        recommended_movies_posters.append((fetch_poster(movie_id)))  #here poster is fetched through movie_id
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Select a movie you liked',
movies['title'].values)

if st.button('Show Recommendations'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.beta_columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
