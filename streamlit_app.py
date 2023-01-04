import streamlit as st

st.title('Snowflake Account Info App')

st.text('Use this app to quickly see high-level info about your Snowflake account.')

add_selectbox = st.sidebar.selectbox(
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
