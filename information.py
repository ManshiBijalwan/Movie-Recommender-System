import streamlit as st
from PIL import Image


img = Image.open('logo.png')
st.set_page_config( page_title='Information', page_icon=img)


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
      <li class="nav-item active">
        <a class="nav-link" href="#" target="_self">Information</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_self">Requirements</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" target="_self">Our Team</a>
      </li>
      <li class="nav-item ">
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


st.markdown("<h1 style='text-align: center; color: Black;'>Recommendation System</h1>", unsafe_allow_html=True)
st.image('https://www.mdpi.com/applsci/applsci-10-05510/article_deploy/html/images/applsci-10-05510-g001.png')


st.subheader('What is Recommendation System')
st.write('Recommender System is a system that seeks to predict or filter preferences according to the user’s '
         'choices.Recommender systems are utilized in a variety of areas including movies music, news, books,'
         ' research articles, search queries, social tags, and products in general.')

st.markdown(""" #### Types of Recommendation System """)
st.write('The recommendation system is classified into three types Content-Based , Collaborative based  '
         'Hybrid bases recommendation system. Let’s try to understand each one by one:-')

#content-based filtering
st.markdown(""" ##### **1.Content-based filtering**""" )
st.markdown(""" *The idea behind Content-based filtering recommendation system is to recommend an item'
        based on a comparison between the content of the items and a user profile.For instance, if a user
        likes to watch movies such as Iron Man, the recommender system recommends movies of the superhero
        genre or films describing Tony Stark.The central assumption of content-based filtering is that you 
        will also like a similar item if you like a particular item*.""")
st.image("https://miro.medium.com/max/828/1*1b-yMSGZ1HfxvHiJCiPV7Q.png")

st.markdown("""**COSINE SIMILARITY**""")
st.write('-Cosine similarity among two objects measures the angle of cosine between the two objects. It'
         'compares two documents on a normalized scale. It can be done by finding the dot product between'
         'the two identities.Lesser the angle between the two vectors more is the similarity. It means if '
         'the angle between two vectors is small, they are almost alike each other and if the angle between '
         'the two vectors is large then the vectors are very different from each other.')
st.image('https://assets.datacamp.com/production/repositories/4966/datasets/ec0fa4795484baf3a19c3f345755a85457a2aae4/cosine.png',caption='cosine vectors' )

st.write('In this filtering, two types of data are used. First, the likes of the user, the user’s interest, user’s'
         ' personal information such as age or, sometimes the user’s history too. This data is represented by the user'
         ' vector. Second, information related to the product’s known as an item vector. The item vector contains the '
         'features of all items based on which similarity between them can be calculated.The recommendations are calculated'
         ' using cosine similarity. If ‘A’ is the user vector and ‘B’ is an item vector then cosine similarity is given by')

st.image('https://miro.medium.com/max/1400/1*pZMivuSRUnOhp2iu7g-RTg.png', caption='cosine similarity formula')
st.image('https://miro.medium.com/max/1400/1*a8QSlP5W4vmhxhrvIxaxhg.png' ,caption='cosine similarity calculations')

st.markdown(""" ##### **Advantages**""")
st.write('1.The user gets recommended the types of items they love.')
st.write('2.The user is satisfied by the type of recommendation')
st.write('3.New items can be recommended; just data for that item is required.')

st.markdown(""" ##### **Disadvantages**""")
st.write('1.The user will never be recommended for different items.')
st.write('2.Business cannot be expanded as the user does not try a different type of product.')
st.write('3.If the user matrix or item matrix is changed the cosine similarity matrix needs to be calculated again')

# collaborative filtering
st.markdown(""" ##### **2.Collaborative Filtering**""" )
st.markdown(""" *The collaborative filtering method is based on gathering and analyzing data on user’s behavior. 
        This includes the user’s online activities and predicting what they will like based on the similarity with
        other users.The theory behind collaborative filtering to work with collaboration with user or movie id.For 
        example, there are two user A and B, user A likes movie P,Q,R,S and user B like movies Q,R,S,T. Since movies
        Q, R and S are similar to both user, therefore, movie P will be recommended to user B and movie T will be 
        recommended to used A*.""")
st.image('https://miro.medium.com/max/706/1*DYJ-HQnOVvmm5suNtqV3Jw.png')

st.markdown(""" ##### **Advantages**""")
st.write('1.New products can be introduced to the user.')
st.write('2.Business can be expanded and can popularise new products.')

st.markdown(""" ##### **Disadvantages**""",)
st.write('1.User’s previous history is required or data for products is required based on the type of collaborative method used.')
st.write('2.The new item cannot be recommended if no user has purchased or rated it.')

# Hybrid filtering
st.markdown(""" ##### **3.Hybrid Recommendation Systems**""",)
st.markdown(""" *In hybrid recommendation systems, products are recommended using both content-based and collaborative
        filtering simultaneously to suggest a broader range of products to customers. This recommendation system is up-and-coming
        and is said to provide more accurate recommendations than other recommender systems.*""")

st.image('https://dataconomy.com/wp-content/uploads/2015/03/Introduction-What-is-a-Recommendation-Engine-Hybrid-Recommender-Systems.jpg')
st.markdown(""" *Netflix is an excellent case in point of a hybrid recommendation system. It makes recommendations by juxtaposing users
        watching and searching habits and finding similar users on that platform. This way, Netflix uses collaborative filtering
        By recommending such shows/movies that share similar traits with those rated highly by the user, Netflix uses content-based 
        filtering. They can also veto the common issues in recommendation systems, such as cold start and data insufficiency issues.*""")
st.write('To make more accurate recommendations nowadays the hybrid recommendation algorithm is used; that is products are recommended using'
         ' both content-based and collaborative filtering together. The hybrid recommendation algorithm is more efficient and more useful.')

st.markdown(""" #### Need of Recommendation System """)
st.write('Recommender systems help the users to get personalized recommendations, helps users to take correct decisions in their online transactions,'
         ' increase sales and redefine the users web browsing experience, retain the customers, enhance their shopping experience.')


