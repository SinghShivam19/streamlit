import streamlit as st
import pickle
import pandas as pd
import requests
st.title('Movie Recommende System')
movie_list=pickle.load(open('C:/Users/SHIVAM SINGH/Dropbox/My PC (LAPTOP-IAV1MUTT)/Downloads/movie_list (1).pkl','rb'))
similarity=pickle.load(open('C:/Users/SHIVAM SINGH/Dropbox/My PC (LAPTOP-IAV1MUTT)/Downloads/similarity.pkl','rb'))
movies = pd.DataFrame(movie_list)

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d635104c0c4bc159f1c0c3782279be57&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = []
    wanted=[]
    for i in movies1:
        movie_id=movie_list.iloc[i[0]].movie_id
        recommended.append(movie_list.iloc[i[0]].title)
        wanted.append(fetch_poster(movie_id))
    return recommended,wanted

selected_movie_name=st.selectbox('Which movie you like to choose?',movies['title'].values)
if st.button('Recommend'):
    names,poster= recommend(selected_movie_name)
    col1, col2, col3, col4, col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])