import streamlit as st
import pickle
import pandas as pd
import requests
import base64
from PIL import Image


# Setting the logo/favicon, title and layout of the page as wide
img = Image.open('images/logo.png')
st.set_page_config(layout="wide", page_title='Movie Recommender System', page_icon=img)


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# work-around for setting the bg-image
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
          background-image: url("data:image/png;base64,%s");
          background-size: cover;
        }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background('images/image.png')

# HTML and CSS code for the NAVIGATION BAR
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',unsafe_allow_html=True)
st.markdown('<link rel="preconnect" href="https://fonts.googleapis.com">', unsafe_allow_html=True)
st.markdown('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>', unsafe_allow_html=True)
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap" rel="stylesheet">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark nav1" style="background-color: #505054;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <a class="navbar-brand" href="#">🎬 Movie Recommender System</a>
    <ul class="navbar-nav ml-auto">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_self">Information</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_self">Requirements</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_self">Our Team</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_self">Contact Us</a>
      </li>
    </ul>
  </div>
</nav>
    <style>
     .nav1
     {
       height: 50px;
       opacity: 0.8;
       border-radius: 20px;
       width: 80%;
       margin:auto;
     }
    .font_style{
    font-family: 'Archivo Black', sans-serif;
    }
    body{
    text-align:center;
    }
    </style>
<h1 class="font_style">Movie Recommender System</h1>
""", unsafe_allow_html=True)

# Code snippet to hide the unnecessary details
hide_menu = """
<style>
#MainMenu { visibility: hidden;}
header { visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_menu, unsafe_allow_html=True)

# MAIN CODE FOR RECOMMENDATION


def show_information(title):
    try:
        url = "https://www.omdbapi.com/?t={}&apikey=fbfd239d".format(title)
        re = requests.get(url)
        re = re.json()
        st.subheader(re['Title'])
        st.caption(f"Genre: {re['Genre']}")
        st.write(f"Release Year: {re['Year']}")
        st.write(re['Plot'])
        st.text(f"Rating: {re['imdbRating']}")
        st.progress(float(re['imdbRating']) / 10)
    except:
        st.error('Oops! No Information available')


def fetch_poster(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    selected_movies = st.selectbox(
     'Enter a movie you like:', movies['title'].values)

with col3:
    st.write(' ')


if st.button('Recommend'):
    names, posters = recommend(selected_movies)
    # with hc.HyLoader('', hc.Loaders.standard_loaders, index=5):
    #     time.sleep(3)
    st.caption('Movies you may like👇')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.caption(names[0])
        with st.expander("Views Details"):
            show_information(names[0])

    with col2:
        st.image(posters[1])
        st.caption(names[1])
        with st.expander("Views Details"):
            show_information(names[1])

    with col3:
        st.image(posters[2])
        st.caption(names[2])
        with st.expander("Views Details"):
            show_information(names[2])

    with col4:
        st.image(posters[3])
        st.caption(names[3])
        with st.expander("Views Details"):
            show_information(names[3])

    with col5:
        st.image(posters[4])
        st.caption(names[4])
        with st.expander("Views Details"):
            show_information(names[4])
