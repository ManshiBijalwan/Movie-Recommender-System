import streamlit as st
from PIL import Image
import base64

img = Image.open('logo.png')
st.set_page_config(layout="wide", page_title='Our team', page_icon=img)


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
      <li class="nav-item">
        <a class="nav-link" href="http://192.168.29.89:8502" target="_self">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_self">Information</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_self">Requirements</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="http://192.168.29.89:8502" target="_self">Our Team</a>
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

st.markdown('<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css">', unsafe_allow_html=True)

st.markdown("""
<h1 class="head_style" >Our Team</h1>

<div class="wrapper">
  <div class="team">
    <div class="team_member">
      <div class="team_img">
        <img src="https://media-exp1.licdn.com/dms/image/C4E03AQHBHURXCZPt-A/profile-displayphoto-shrink_800_800/0/1649770205117?e=1655337600&v=beta&t=XPqueJJDg9qh7vPqkwp-plNzIEKl7JUMZVKR65kJ09g" alt="Team_image">
      </div>
      <h3>Kashish Jain</h3>
      <p class="role">Student</p>
        <a href="#"><i class="fa fa-lg fa-linkedin-square" style="font-size:40px;color:black"></i></a> &nbsp;&nbsp;
      <a href="#"><i class="fa fa-lg fa-twitter-square" style="font-size:40px;color:black"></i></a> &nbsp;&nbsp;
      <a href="#"><i class="fa fa-lg fa-github-square" style="font-size:40px;color:black"></i></a>   
       </div>
    <div class="team_member">
      <div class="team_img">
        <img src="https://avatars.githubusercontent.com/u/99536793?s=400&u=853b2388159e711655753d943b2ac1433a8cf1a9&v=4" alt="Team_image">
      </div>
      <h3>Mansi Dixit</h3>
      <p class="role">Student</p>
      <a href="https://www.linkedin.com/in/mansi-dixit-573106208"><i class="fa fa-lg fa-linkedin-square" style="font-size:40px;color:black"></i></a> &nbsp;&nbsp;
      <a href="https://twitter.com/13MansiDixit?t=SZeGYVdOOp2xxN3j_fAL3w&s=08"><i class="fa fa-lg fa-twitter-square" style="font-size:40px;color:black"></i></a> &nbsp;&nbsp;
      <a href="https://github.com/MansiDixit1"><i class="fa fa-lg fa-github-square" style="font-size:40px;color:black"></i></a>
    </div>
    <div class="team_member">
      <div class="team_img">
        <img src="https://i.imgur.com/jQj1I8E.png" alt="Team_image">
      </div>
      <h3>Medha Upadhyay</h3>
      <p class="role ">Student</p>
        <a href="#"><i class="fa fa-lg fa-linkedin-square" style="font-size:40px;color:black"></i></a> &nbsp;&nbsp;
      <a href="#"><i class="fa fa-lg fa-twitter-square" style="font-size:40px;color:black"></i></a> &nbsp;&nbsp;
      <a href="#"><i class="fa fa-lg fa-github-square" style="font-size:40px;color:black"></i></a>  
      </div>    
      <div class="team_member">
      <div class="team_img">
        <img src="" alt="Team_image">
      </div>
      <h3>Manshi Bijalwan</h3>
      <p class="role">Student</p>
        <a href="#"><i class="fa fa-lg fa-linkedin-square" style="font-size:40px;color:black"></i></a> &nbsp;&nbsp;
      <a href="#"><i class="fa fa-lg fa-twitter-square" style="font-size:40px;color:black"></i></a> &nbsp;&nbsp;
      <a href="#"><i class="fa fa-lg fa-github-square" style="font-size:40px;color:black"></i></a>     
      </div>
  </div>
</div>
<style>

    *{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      }
    img {
      border-radius: 50%;
      margin-top: 6px;
    }
    body{
      background: #81c644;
      font-family: 'Josefin Sans', sans-serif;
    }
    
    .wrapper{
      padding-bottom:0;
    }
    
    .head_style{
      font-family: 'Allura', cursive;
      font-size: 55px;
      margin-bottom: 60px;
      text-align: center;
      margin-top:-10px;
    }
    
    .team{
      display: flex;
      justify-content: center;
      width: auto;
      text-align: center;
      flex-wrap: wrap;
    }
    
    .team .team_member{
      background: #fff;
      margin: 26px;
      margin-bottom: 50px;
      width: 255px;
      padding: 25px;
      line-height: 20px;
      color: #8e8b8b;  
      position: relative;
    }
    
    .team .team_member h3{
      color: #9a3a3a;
      font-size: 26px;
      margin-top: 60px;
      font-family: 'Allura', cursive;
    }
    
    
    .team .team_member .team_img{
      position: absolute;
      top: -50px;
      left: 13%;
      transform: translateX(-20%);
      transform: translateY(-10%);
      width: 190px;
      height: 210px;
      border-radius: 50%;
      background: #fff;
    }
    
    .team .team_member .team_img img{
      width: 160px;
      height: 160px;
      padding: 5px;
    }
 </style>
""",unsafe_allow_html=True)


file_ = open("images/cloud.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img style= width:50px;margin-top:20px;border-radius:0%; src="data:image/png;base64,{data_url}" alt="cloud">'
    ,unsafe_allow_html=True,
)