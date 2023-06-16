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

st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;"><br>{"In recent years, road accidents have been a significant cause of concern worldwide, leading to tragic loss of life, injuries, and economic burden. France, like many other countries, strives to enhance road safety and reduce the severity of accidents. To achieve this goal, harnessing the power of data science methods has become increasingly important. By utilizing data-driven approaches, we can gain valuable insights into the factors contributing to the severity of road accidents in France. We believe that machine learning and deep learning are good tools to reduce or prevent road accidents by applying preventive actions using AI solutions."}</p><br>', unsafe_allow_html=True)
st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;">{"The objective of this project is to try to predict the severity of road accidents in France using historical data. By analyzing past records, the aim is to develop a predictive model that can estimate the severity of accidents. This project presents an ideal opportunity to encompass all stages of a comprehensive Data Science project. "}</p><br>', unsafe_allow_html=True)
st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;">{"The initial step involves studying and implementing methods to clean the dataset. This process includes identifying and rectifying any errors, inconsistencies, or missing values present in the dataset. By ensuring the dataquality and reliability, subsequent analysis can conduct to a greater model performance accuracy."}</p><br>', unsafe_allow_html=True)
st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;">{"The next step focuses on extracting relevant characteristics from the historical data. This involves examining the various attributes and factors associated with accidents, such as weather conditions, geographical location, and other related information. By identifying the most influential features, the objective is to develop a robust model that can effectively estimate the severity of accidents based on key features."}</p><br><br><br>', unsafe_allow_html=True)
st.markdown(f'<p align="rght" font-family: "Times New Roman" style="color:#000000;">{"TEAM - Sidi, Fan, Deepa"}</p><br>', unsafe_allow_html=True)



