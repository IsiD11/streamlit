
### This is the prediction subpage of streamlit webapp

import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(
    page_title="France Road Accident Data Analysis - Prediction",
    layout='wide'
)

st.markdown(f'<b><h0 style="color:#00008B;font-size:35px;">{"Prediction:"}</h0><br><br>', unsafe_allow_html=True)

# Content of the page
areaZone = st.text_input("Area Zone")
collisionType = st.text_input("Collision Type")
municipality = st.text_input("Municipality")
roadCategory = st.text_input("Road Category")
trafficRegime = st.text_input("Traffic Regime")
nrOfTrafficLanes = st.text_input("Number Of Traffic Lanes")
accidentSituation = st.text_input("Accident Situation")
struckWithFixedObject = st.text_input("Struck With Fixed Object")
struckWithMovingObject = st.text_input("Struck With MovingObject")
initialShockPoint = st.text_input("Initial Shock Point")
intersectionType = st.text_input("Intersection Type")

if st.button('Predict Accident Severity'):
    st.write('Predict Accident Severity clicked') 
else:
    st.write('Predict Accident Severity not clicked') 

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
