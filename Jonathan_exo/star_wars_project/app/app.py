import streamlit as st

#st.image('./data/Star_Wars_Logo.svg.png')


import base64

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i0.wp.com/views.fr/wp-content/uploads/2020/05/vador-pfa.jpg?w=1200&ssl=1");
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


col1, mid, col2 = st.columns([30,1,30])
with col1:
    st.markdown("##### “Don’t be too proud of this technological terror you’ve constructed. The ability to destroy a planet is insignificant next to the power of the Force.”")
