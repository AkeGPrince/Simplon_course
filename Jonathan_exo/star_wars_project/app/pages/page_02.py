import numpy as np
import json
import pandas as pd
import requests as req
import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://static1.moviewebimages.com/wordpress/wp-content/uploads/2022/04/star-wars-jedi-dont-use-force-enough-featured-image-Cropped.jpg?q=50&fit=contain&w=1140&h=&dpr=1.5");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

col1, mid, col2 = st.columns([80,40,80])
with col1:
    pick = st.selectbox('“Your path you must decide“ - Yoda', ['Make a choice', 'People', 'Planets', 'Species', 'Starships', 'Vehicles', 'Films'])
    if pick == "Films":
        cat = "title"
    elif pick == "Make a choice":
        pick = ""
    else:
        cat = "name"

names = []
site = "https://swapi.dev/api/"
page = site + pick.lower()
url = req.get(page).json()

if "next" in url:
    next_ = True
elif "next" not in url:
    next_ = False
elif "next" == None:
    next_ = False
    for i in range(len(url["results"])):
            names.append(url["results"][i][cat])

while next_:
    urls = req.get(page).json()
    for i in range(len(urls["results"])):
            names.append(urls["results"][i][cat])
    if urls["next"] != None:
        page = urls["next"]
    else:
        next_ = False

with col2:
    inp = pick
    if inp == "":
        pass
    else:
        inp = st.selectbox('“You will find only what you bring in.“ - Yoda', names)

def category(pick, inp):
    if pick == "" and inp == "":
        result = ""
    else:
        choice = pick.lower()
        url = f"https://swapi.dev/api/{choice}/?search={inp}"
        page = req.get(url).json()
        df = pd.DataFrame(page["results"])
        result = df[df[cat] == inp ]
        result = result.iloc[:,0:8:1]
    return result

st.write(category(pick, inp))
