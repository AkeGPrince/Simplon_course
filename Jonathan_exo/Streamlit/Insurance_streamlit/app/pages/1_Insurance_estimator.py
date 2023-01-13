
import pandas as pd
import streamlit as st
import requests as req
from datetime import datetime, date, time, timezone

st.markdown("# Welcome to Hemon Insurance")

st.text("")
st.text("")
st.text("")

st.markdown("### If you need to estimate your total cost insurance, please fill the form.")

birthday = st.date_input(label= "When's your birthday",
                         value=date(2000, 1, 1),
                         min_value=date(1930, 1, 1))
today = date.today()
age = today - birthday
age = age.days //365


col1, mid, col2 = st.columns([30,1,30])
with col1:
    sex = st.radio("Genre",('female', 'male'))
with col2:
    smoker = st.radio("Do you smoke ?",('no', 'yes'))


children = st.number_input('Number of children', 0, 10)

taille = st.slider('What is your size ? (meter)', 1.0, 2.1, value=1.60)

taille = taille**2

poids = st.number_input("What is your weight ? (kg)", 40, 150, value=70)

bmi = poids / taille


def prediction(ages, bmis, childrens, smokers, sexs):
    url= f"https://96ac-2a02-8440-6141-3350-21d9-75e7-41b0-518e.eu.ngrok.io/?age={ages}&bmi={bmis}&children={childrens}&smoker={smokers}&sex={sexs}"
    response = req.get(url).json()["prédiction"]
    return f"The estimate cost of your insurance is: {response}$ "

if st.button("Estimate"):
    st.write(prediction(age, bmi, children, smoker, sex))
else:
    st.write("You need to click button to get your estimation.")
