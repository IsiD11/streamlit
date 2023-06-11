### This page displays the different visualisations generated from the dataset

import streamlit as st

# Set page title
st.set_page_config(
    page_title="France Road Accident Data Analysis - Data Visualizations",
    layout='wide'
)


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

