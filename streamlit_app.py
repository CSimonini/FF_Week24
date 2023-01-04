import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

st.title('Snowflake Account Info App')

st.markdown("Use this app to quickly see high-level info about your Snowflake account.")

sel_choice = st.sidebar.selectbox(
    "Select what account info you would like to see",
    ("None",
     "Shares",
     "Roles",
     "Grants",
     "Users",
     "Warehouses",
     "Databases",
     "Schemas",
     "Tables",
     "Views"     
    )
)

st.write('You selected:', sel_choice)
