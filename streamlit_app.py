import streamlit

streamlit.title('Snowflake Account Info App')

streamlit.text('Use this app to quickly see high-level info about your Snowflake account.')

st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-color: #DEE0FB;
    color: #ffffff
}
</style>
""",
    unsafe_allow_html=True,
)
