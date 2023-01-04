import streamlit as st
import snowflake.connector

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

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("show databases")
my_data_rows = my_cur.fetchall()
streamlit.dataframe(my_data_rows)
