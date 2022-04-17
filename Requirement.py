import streamlit as st
from PIL import Image

img = Image.open('logo.png')
st.set_page_config( page_title='Requirement', page_icon=img)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',unsafe_allow_html=True)

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

st.markdown("""
   <div class="flex font-sans">
  <div class="requirement">
    <img src="/https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.analyticsvidhya.com%2Fwp-content%2Fuploads%2F2021%2F06%2F39595st.jpeg&imgrefurl=https%3A%2F%2Fwww.analyticsvidhya.com%2Fblog%2F2021%2F06%2Fbuild-web-app-instantly-for-machine-learning-using-streamlit%2F&tbnid=VYGSuXNCzxJ6aM&vet=12ahUKEwiv3pbyjZT3AhV6KbcAHYceDm8QMygGegUIARDSAQ..i&docid=ltqs0UcbEQltGM&w=1200&h=627&q=streamlit%20python&ved=2ahUKEwiv3pbyjZT3AhV6KbcAHYceDm8QMygGegUIARDSAQ" alt="" class="absolute inset-0 w-full h-full object-cover" />
  </div>
    <div class="flex flex-wrap">
      <h1 class="flex-auto text-lg text-slate-900">
        ALL ABOUT STREAMLIT AND MODULES
      </h1>
      </div>
      <div class="w-full flex-none text-sm font-medium text-slate-700 mt-2 ">
        A brief introduction to StreamLit-
Streamlit is an open source app framework in Python language. 
It helps us create web apps for data science, and machine 
learning, efficiently and in a short time. It is compatible
with major Python libraries such as scikit-learn, Keras, 
PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc.We have used
the same in our project and it has effectively chanced the
code scripts into web links, it's purely python and an advantage
to it is that it does not require prior front end experience.
It is a user friendly framework which watches for changes on
linked Git repository's updates, and that the applications
are deployed automatically in the shared link.

</div>

<style>
    D1
    {
      background-color: #ECF0F1;
      margin: 30px;
    }
</style>
""", unsafe_allow_html=True)

with st.expander('Modules'):
    st.write('Modules used were streamlit, pandas, pickle, PIL, requests, and base64')


# Code snippet to hide the unnecessary details
hide_menu = """
<style>
#MainMenu { visibility: hidden;}
header { visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_menu, unsafe_allow_html=True)