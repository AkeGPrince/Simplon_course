import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import sklearn
import streamlit as st




st.markdown("# Tell me about you:")
# st.markdown("## Récupération de la Database: ")

# lines_number = st.slider("Display lines", 1,10,3)

# df = pd.read_csv("./data/insurance.csv")
# df = df.head(lines_number)

# st.dataframe(df)

st.text_input('First name')
st.text_input('Last name')
st.text_input('Company')
st.text_input('Email address')
st.text('')
st.text('')

st.multiselect('Select what you need', ['Data analysis', 'Data visualisation', 'Web development', 'Robotic process automation', 'Chatbot'])


# st.radio('Select model', ['Lasso', 'Ridge', 'Linear Regression'])
# st.button('Click me')
# st.checkbox('I agree')
# st.radio('Pick one', ['cats', 'dogs'])
# st.selectbox('Pick one', ['cats', 'dogs'])
# st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
# st.slider('Pick a number', 0, 100)
# st.select_slider('Pick a size', ['S', 'M', 'L'])
# st.text_input('First name')
# st.number_input('Pick a number', 0, 10)
# st.text_area('Text to translate')
# st.time_input('Meeting time')
# st.file_uploader('Upload a CSV')
# st.color_picker('Pick a color')
