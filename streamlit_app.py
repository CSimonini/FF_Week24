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

if sel_choice == "Grants":
    string_choice = "show " + sel_choice + " on account"
else:
    string_choice = "show " + sel_choice + " in account"
 
if sel_choice == "None":
    ""
else:
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute(string_choice)
    my_data_rows = my_cur.fetchall()
    st.dataframe(my_data_rows)
    
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/200/200);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
