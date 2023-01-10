
import pandas
import numpy
import seaborn
import matplotlib
import sklearn
import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.lemagducine.fr/wp-content/uploads/2019/12/code-heritage-jedi-ma%C3%AEtre-yoda-1168x778.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# st.markdown("# Hemon GNAMBE \n ## Consultant Data Junior \n ##### Email: Simplonia3@gmail.com")
# st.image('./data/avatar.png', caption="Myself", width=500 )

# st.markdown("<h1 style='color:black';>STAR \n WARS </h1>", unsafe_allow_html=True)
# st.image('./data/Star_Wars_Logo.svg.png')

# st.text("")
# st.text("")
# st.text("")
# st.text("")


col1, mid, col2 = st.columns([30,1,30])
with col2:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    st.markdown("##### “Do or do not. There is no try.“")
    infos = st.button('Display my POWER',)
    st.write(infos)
    if infos:
        st.markdown("##### “If you ask, I will find.“ ")
    else :
        st.write("You definitely should click if you want to see magics")
