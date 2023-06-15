import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

# Content of the page
st.markdown(f'<b><h0 style="color:#000000;font-size:35px;">{"France Road Accidents Data Analysis & Severity Prediction !"}</h0><br>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file).sample(n=1000)
  
pr = df.profile_report()

st_profile_report(pr)
