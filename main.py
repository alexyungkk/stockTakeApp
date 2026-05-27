import streamlit as st

st.set_page_config(page_title="Sutton Stock Page", page_icon=":hotel:", layout="centered",\
                   initial_sidebar_state="expanded", menu_items={
                       "Report a Bug": "mailto:yungkk@hotmail.com"
                   })

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("Please login")   

    with st.form("login_form", border=True):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", placeholder="Enter your password", type="password")

        col11, col12 = st.columns([1, 3])
        login = col11.form_submit_button("Login")

        if login:
            if not username or not password:
                st.warning("⚠️ Please fill in both username and password.")
            elif username in st.secrets["users"] and password == st.secrets["users"][username]:
                st.session_state.logged_in = True
                st.switch_page("pages/stockCheck.py")
            else:
                st.error("❌ Invalid username or password.")     