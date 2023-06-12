
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
    colsToDisplay = ['Model Name',
                     'Training set score',
                     'Test set score'
                    ]
    
    df = pd.DataFrame(np.random.randn(4, 3), columns=colsToDisplay )
    st.table(df)


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
