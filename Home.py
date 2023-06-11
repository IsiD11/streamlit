#### This is the home page of France Road Accidents Data project

import streamlit as st

st.set_page_config(
    page_title="Road Accident Severity Prediction",
    page_icon="👋",
)

st.write("# Road Accidents in France ! 👋")
st.markdown(
        """
        The objective of this project is to try to predict the severity of road accidents in France. Predictions will be based on historical data.
        """
)

st.sidebar.success("Home")
