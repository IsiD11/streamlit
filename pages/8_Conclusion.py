### This is the conclusion page of the web app .
import streamlit as st

# Set page title
st.set_page_config(
    page_title="France Road Accident Data Analysis",
    layout='wide'
)

# Content of the page
st.markdown(f'<b><h0 style="color:#000000;font-size:35px;">{"Conclusion!"}</h0><br>', unsafe_allow_html=True)

# To insert image
st.image(
            "https://www.planetware.com/wpimages/2020/02/france-in-pictures-beautiful-places-to-photograph-eiffel-tower.jpg",
            width=900, # Manually Adjust the width of the image as per requirement
        )

# To insert textual content 

st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;"><br>{"During our comprehensive data analysis of road accident severity predictions in France, we employed four different classification models to conduct the analysis. These models allowed us to evaluate and compare the performance of each model in predicting the severity of traffic accidents. After analyzing the results, we determined that the XGBoost model outperformed the other models in terms of accuracy and overall predictive capability."}</p><br>', unsafe_allow_html=True)
st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;"><br>{"To gain a better understanding of the factors influencing the prediction outcomes, we utilized two popular interpretation techniques: LIME and SHAP. LIME (Local Interpretable Model-agnostic Explanations) provided us with local explanations for individual predictions, highlighting the specific variables that had the most influence on each prediction. By examining the LIME explanations, we were able to identify which variables contributed positively or negatively to the prediction results for each instance."}</p><br>', unsafe_allow_html=True)
st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;"><br>{"Additionally, we employed SHAP (SHapley Additive exPlanations) to gain a more comprehensive understanding of variable importance. SHAP values helped us determine the overall impact of each variable across the entire dataset. This allowed us to identify the variables that consistently had a significant positive or negative contribution to the prediction outcomes."}</p><br>', unsafe_allow_html=True)
st.markdown(f'<p align="justify" font-family: "Times New Roman" style="color:#000000;"><br>{"By combining the insights gained from LIME and SHAP, we were able to extract valuable information about the relationship between input features and the severity of road accidents. This analysis not only provided us with a deeper understanding of the underlying factors influencing accident severity but also enabled us to make more informed decisions and recommendations for accident prevention and mitigation strategies in France."}</p><br>', unsafe_allow_html=True)



