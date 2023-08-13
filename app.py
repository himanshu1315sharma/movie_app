import streamlit as st
import pickle as p
import pandas as pd
import requests as r
def fetch(movie_id):
    response = r.get('https://api.themoviedb.org/3/movie/{}?api_key=c4c1e213e6e8f49e29d04fcdd9a991dd&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append((movies.iloc[i[0]].title))
        posters.append(fetch(movie_id))
    return recommended_movies,posters    



similarity = p.load(open('similarity.pkl','rb'))
movie_dict = p.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
st.title('Movie recommender system')
option = st.selectbox('option',movies['title'].values)
if st.button('Recommend'):
    recom,posters = recommend(option)
    col1, col2, col3, col4,col5 = st.columns(5)

    with col1:
        st.header(recom[0])
        st.image(posters[0])


    # Add chart #1
    with col2:
        st.header(recom[1])
        st.image(posters[1])

    with col3:
        st.header(recom[2])
        st.image(posters[2])

    with col4:
        st.header(recom[3])
        st.image(posters[3])

    with col5:
        st.header(recom[4])
        st.image(posters[4])
