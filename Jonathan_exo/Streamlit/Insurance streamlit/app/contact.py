import pandas
import numpy
import seaborn
import matplotlib
import sklearn
import streamlit as st


# st.markdown("# Hemon GNAMBE \n ## Consultant Data Junior \n ##### Email: Simplonia3@gmail.com")
# st.image('./data/avatar.png', caption="Myself", width=500 )

st.markdown("<h1 style='text-align: center;'>Me, Myself & I : </h1>", unsafe_allow_html=True)

st.text("")
st.text("")
st.text("")



col1, mid, col2 = st.columns([30,1,30])
with col2:
    st.image('./data/avatar.png', width=400)
with col1:
    st.markdown("# Hemon GNAMBE \n ## Consultant Data Junior")
    infos = st.button('Display my informations',)
    if infos:
        st.markdown("##### Contact: \n ###### Simplonia3@gmail.com \n 06.67.76.28.xx")
    else :
        st.write("You definitely should click display informations to get the best analysis")
