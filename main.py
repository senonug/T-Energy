# Entry point aplikasi Streamlit
import streamlit as st
from config import DEFAULT_USERNAME, DEFAULT_PASSWORD

# Auth sederhana
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.set_page_config(page_title='Login - Auto Generate Dashboard', layout='wide')
    st.markdown("""
        <style>
        .stApp {background-color: #f0f9ff;}
        </style>
    """, unsafe_allow_html=True)
    st.title("🔐 Login Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Username atau password salah.")
else:
    st.switch_page("pages/dashboard.py")
