import streamlit as st

if not st.session_state.get("logged_in", False):
    st.error("Please login first!")
    st.switch_page("main.py")
    st.stop()

st.title("Stock Check Page")