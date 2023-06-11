### This is the data visualization subpage of streamlit webapp

import streamlit as st

# Set page title
st.set_page_config(
    page_title="France Road Accident Data Analysis - Visualization",
    layout='wide'
)

st.markdown(f'<b><h0 style="color:#00008B;font-size:35px;">{"Data Visualizations:"}</h0><br><br>', unsafe_allow_html=True)

# Content of the page
option = st.selectbox(
    'Choose a data visualization: ',
    ('Accident severity over years', 'Accidents reported over years', 'Accidents happened in day of week',
     'Impact of lighting on road accidents', 'Impact of atmospheric conditions on road accidents',
    'Impact of road category on accidents','Impact of intersection type on accidents','Impact of accident time on severity',
    'Impact of area zone on severity','Impact of collision type on severity','Impact of surface condition on severity',
    'Impact of accident situation on severity'))

if option == 'Accident severity over years':
st.image(image_list[0])
elif option == item_list[0]:
st.image(image_list[0])
elif option == item_list[1]:
st.image(image_list[1])
elif option == item_list[2]:
st.image(image_list[2])
elif option == item_list[3]:
st.image(image_list[3])
elif option == item_list[4]:
st.image(image_list[4])


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
