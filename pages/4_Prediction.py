

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
areaZone = st.text_input("Area Zone", default_value_goes_here)
collisionType = st.text_input("Collision Type", default_value_goes_here)
municipality = st.text_input("Municipality", default_value_goes_here)
roadCategory = st.text_input("Road Category", default_value_goes_here)
trafficRegime = st.text_input("Traffic Regime", default_value_goes_here)
nrOfTrafficLanes = st.text_input("Number Of Traffic Lanes", default_value_goes_here)
accidentSituation = st.text_input("Accident Situation", default_value_goes_here)
struckWithFixedObject = st.text_input("Struck With Fixed Object", default_value_goes_here)
struckWithMovingObject = st.text_input("Struck With MovingObject", default_value_goes_here)
initialShockPoint = st.text_input("Initial Shock Point", default_value_goes_here)
intersectionType = st.text_input("Intersection Type", default_value_goes_here)

    
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
