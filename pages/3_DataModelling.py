
### This is the data modelling subpage of streamlit webapp

import streamlit as st

# Set page title
st.set_page_config(
    page_title="France Road Accident Data Analysis - Modelling",
    layout='wide'
)

st.markdown(f'<b><h0 style="color:#00008B;font-size:35px;">{"Data Modelling:"}</h0><br><br>', unsafe_allow_html=True)

# Content of the page
option = st.selectbox(
    'Choose a data modelling: ',
    ('XGBoost', 'Gradient Boost', 'Random Forest','AdaBoost'))

if option == 'XGBoost':
    st.write('XGBoost')
elif option == 'Gradient Boost':
    st.write('Gradient Boost')
elif option == 'Random Forest':
    st.write('Random Forest')
elif option == 'AdaBoost':
    st.write('AdaBoost')

# To set the background image of the page
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-photo/abstract-luxury-gradient-blue-background-smooth-dark-blue-with-black-vignette-studio-banner_1258-63452.jpg?size=626&ext=jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
