import streamlit as st

st.title('Snowflake Account Info App')

st.text('Use this app to quickly see high-level info about your Snowflake account.')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
