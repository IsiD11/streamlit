
### This is the data modelling subpage of streamlit webapp

import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(
    page_title="France Road Accident Data Analysis - Modelling",
    layout='wide'
)

st.markdown(f'<b><h0 style="color:#00008B;font-size:35px;">{"Data Modelling:"}</h0><br><br>', unsafe_allow_html=True)

# Content of the page
option = st.selectbox(
    'Choose a data modelling result criteria: ',
    ('Accuracy Score', 
     'Training Time',
     'RMSE', 
     'Precision',
     'Recall',
     'F1 Score'
    ))
    
if option == 'Accuracy Score':
    dict = {'Model Name':['XGBoost', 'Gradient Boost', 'Random Forest', 'AdaBoost'],
            'Training set score':[71.99, 71.89, 91.1, 69.5],
            'Test set score':[71.4, 71.4, 66.7, 69.7]
       }
    df_AccuracyScore = pd.DataFrame(dict)
    st.table(df_AccuracyScore)

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
