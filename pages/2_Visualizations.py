### This page displays the different visualisations generated from the dataset

import streamlit as st

# Set page title
st.set_page_config(
    page_title="France Road Accident Data Analysis - Data Visualizations",
    layout='wide'
)

option = st.selectbox(
    'Choose a data visualization : ',
    ('Accident severity over years', 'Accidents reported over years', 'Accidents happened in day of week',
     'Impact of lighting on road accidents', 'Impact of atmospheric conditions on road accidents',
    'Impact of road category on accidents','Impact of intersection type on accidents','Impact of accident time on severity',
    'Impact of area zone on severity','Impact of collision type on severity','Impact of surface condition on severity',
    'Impact of accident situation on severity'))

st.write('You selected:', option)

# Content of the page
st.markdown(f'<b><h0 style="color:#00008B;font-size:35px;">{"Datasets used in this project :"}</h0><br><br>', unsafe_allow_html=True)
st.markdown(f'<b><h1 style="color:#ffffff;font-size:25px;">{"https://www.data.gouv.fr/en/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/"}</h1>', unsafe_allow_html=True)
st.markdown(f'<b><h1 style="color:#ffffff;font-size:25px;">{"https://www.kaggle.com/ahmedlahlou/accidents-in-france-from-2005-to-2016/"}</h1><br><br>', unsafe_allow_html=True)

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

