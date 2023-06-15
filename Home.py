### This is the main page of the web app .
import streamlit as st

# Set page title
st.set_page_config(
    page_title="France Road Accident Data Analysis",
    layout='wide'
)

# Content of the page
st.markdown(f'<b><h0 style="color:#000000;font-size:35px;">{"France Road Accidents Data Analysis & Severity Prediction !"}</h0><br>', unsafe_allow_html=True)

# To insert image
st.image(
            "https://www.planetware.com/wpimages/2020/02/france-in-pictures-beautiful-places-to-photograph-eiffel-tower.jpg",
            width=900, # Manually Adjust the width of the image as per requirement
        )

# To insert textual content 

st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;"><br>{"In recent years, road accidents have been a significant cause of concern worldwide, leading to tragic loss of life, injuries, and economic burden. France, like many other countries, strives to enhance road safety and reduce the severity of accidents. To achieve this goal, harnessing the power of data science methods has become increasingly important. By utilizing data-driven approaches, we can gain valuable insights into the factors contributing to the severity of road accidents in France. We believe that machine learning and deep learning are good tools to reduce or prevent road accidents by applying preventive actions using AI solutions."}</p><br><br>', unsafe_allow_html=True)
st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;"><br>{"The objective of this project is to try to predict the severity of road accidents in France using historical data. By analyzing past records, the aim is to develop a predictive model that can estimate the severity of accidents. This project presents an ideal opportunity to encompass all stages of a comprehensive Data Science project. "}</p><br><br>', unsafe_allow_html=True)


