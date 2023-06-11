### This is the main page of the web app .
import streamlit as st

st.set_page_config(
    page_title="France Road Accident Data Analysis",
    page_icon="👋",
)

st.write("# France Road Accidents Data Analysis & Severity Prediction ! 👋")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iB8ty6.RHr8M/v1/800x-1.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
