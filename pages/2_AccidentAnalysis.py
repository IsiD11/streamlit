### This is the data visualization subpage of streamlit webapp

import streamlit as st

# Set page title
st.set_page_config(
    page_title="France Road Accident Data Analysis - Visualization",
    layout='wide'
)

st.markdown(f'<b><h0 style="color:#00008B;font-size:35px;">{"Data Visualizations:"}</h0><br>', unsafe_allow_html=True)

# Content of the page
option = st.selectbox(
    'Choose a data visualization:',
    ('Accident severity over years', 'Accidents reported over years', 'Accidents happened in day of week',
     'Impact of lighting on road accidents', 'Impact of atmospheric conditions on road accidents',
    'Impact of road category on accidents','Impact of intersection type on accidents','Impact of accident time on severity',
    'Impact of area zone on severity','Impact of collision type on severity','Impact of surface condition on severity',
    'Impact of accident situation on severity'))

st.markdown(f'<br>', unsafe_allow_html=True)
if option == 'Accident severity over years':
    # List down the observations
    st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;"><b>{"Observations:"}</b></p>', unsafe_allow_html=True)
    st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;">{"- Death rate in accidents is slightly getting reduced over years."}</p>', unsafe_allow_html=True)
    st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;">{"- Number of accidents also show a reducing trend over years."}</p>', unsafe_allow_html=True)
    
    st.image('visualizations/Accident Severity over years.png')
elif option == 'Accidents reported over years':
    st.image('visualizations/Accident reported over years.png')
elif option == 'Accidents happened in day of week':
    st.image('visualizations/Accident happened in day of week - Copy.png')
elif option == 'Impact of lighting on road accidents':
    st.image('visualizations/Impact of lighting on accidents.png')
elif option == 'Impact of atmospheric conditions on road accidents':
    st.image('visualizations/Impact of atmospheric condition on accidents.png')
elif option == 'Impact of road category on accidents':
    st.image('visualizations/Impact of road category on accidents.png')    
elif option == 'Impact of intersection type on accidents':
    st.image('visualizations/Impact of intersection type on accidents.png')   
elif option == 'Impact of accident time on severity':
    st.image('visualizations/Impact of accident time severity.png')
elif option == 'Impact of area zone on severity':
    st.image('visualizations/Impact of areazone on severity.png')
elif option == 'Impact of collision type on severity':
    st.image('visualizations/Impact of collission type on severity.png')
elif option == 'Impact of surface condition on severity':
    st.image('visualizations/Impact of surface condition on severity.png')
elif option == 'Impact of accident situation on severity':
    st.image('visualizations/Impact of accident situation on severity.png')

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











