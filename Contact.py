import streamlit as st
from PIL import Image
import base64

img = Image.open('images/logo.png')
st.set_page_config(layout="wide", page_title='Movie Recommender System', page_icon=img)


st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',unsafe_allow_html=True)
st.markdown('<link rel="preconnect" href="https://fonts.googleapis.com">', unsafe_allow_html=True)
st.markdown('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>', unsafe_allow_html=True)
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap" rel="stylesheet">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark nav1" style="background-color: #505054;">
  <div class="collapse navbar-collapse" id="navbarNav">
  <a class="navbar-brand" href="#">🎬 Movie Recommender System</a>
    <ul class="navbar-nav ml-auto">
      <li class="nav-item ">
        <a class="nav-link" href=" " target="_self">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_self">Information</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_self">Requirements</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" target="_self">Our Team</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="" target="_self">Contact Us</a>
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
""", unsafe_allow_html=True)

hide_menu = """
<style>
#MainMenu { visibility: hidden;}
header { visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)


file_ = open("images/contact-logo.jpg", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img style= width:90px;margin-left:450px; src="data:image/png;base64,{data_url}" alt="Contact-logo">'
    ,unsafe_allow_html=True,
)


st.markdown("""
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
</head>

<body>
    <div class="container mt-5 D1">
        <h1 class="head_style">Contact Us!</h1>
        <form class="row g-3" action="https://formsubmit.co/1a8f0038d25904380d52672728979434" method="POST">
          <div class="col-md-6 D2">
            <label for="firstName" class="form-label">First Name</label>
            <input type="text" class="form-control" name="Name" id="firstName" required>
          </div>
          <div class="col-md-6 D2">
            <label for="lastName" class="form-label">Last Name</label>
            <input type="text" class="form-control" name="Last&nbsp;Name" id="lastName" required>
          </div>
          <div class="col-md-8 D2">
            <label for="emailInfo" class="form-label">E-mail</label>
            <input type="email" class="form-control" name="Email" id="emailInfo" required>
          </div>
          <br>
          <div class="col-md-12 D2">
            <label for="comments" class="form-label">Message</label>
            <textarea class="form-control" name="Message" id="comments" rows="3" required></textarea>
          </div>
          <div class="col-md-12 ">
            <button type="submit" class="btn">Submit</button>
          </div>
        </form>
    </div>
</body>
<style>

.head_style{
 font-family: 'Archivo Black', sans-serif;
 margin-top:-130px;
}
.btn:hover {
      background-color:#FADBD8;
      transition: 0.3s;
  }
.D1
{
border-radius: 5%;
width: 800px;
height 1200px;
text-align: center;
}
.D2
{
padding: 15px;
margin-top: 20px;
margin-down:20px;
text-align: left;
}
.btn
{
color:#ECF0F1;
font-size: 20px;
position: relative;
background-color:#641E16;
width:150px;
height: 50px;
border-radius: 40px;
}
</style>
</html>
""", unsafe_allow_html=True)

